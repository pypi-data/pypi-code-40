# -*- coding: utf-8 -*-
"""
This module contains the entity resolver component of the Workbench natural language processor.
"""
import copy
import logging
import hashlib
import os

from ..core import Entity
from ._config import (get_app_namespace, get_classifier_config, DOC_TYPE,
                      DEFAULT_ES_SYNONYM_MAPPING, PHONETIC_ES_SYNONYM_MAPPING)

from ._elasticsearch_helpers import (create_es_client, load_index, get_scoped_index_name,
                                     delete_index, does_index_exist, get_field_names,
                                     INDEX_TYPE_KB, INDEX_TYPE_SYNONYM)

from elasticsearch5.exceptions import ConnectionError, TransportError, ElasticsearchException
from ..exceptions import EntityResolverConnectionError, EntityResolverError

logger = logging.getLogger(__name__)


class EntityResolver:
    """An entity resolver is used to resolve entities in a given query to their canonical values
    (usually linked to specific entries in a knowledge base).
    """
    # prefix for Elasticsearch indices used to store synonyms for entity resolution
    ES_SYNONYM_INDEX_PREFIX = "synonym"

    def __init__(self, app_path, resource_loader, entity_type, es_host=None, es_client=None):
        """Initializes an entity resolver

        Args:
            app_path (str): The application path
            resource_loader (ResourceLoader): An object which can load resources for the resolver
            entity_type: The entity type associated with this entity resolver
            es_host (str): The Elasticsearch host server
        """
        self._app_namespace = get_app_namespace(app_path)
        self._resource_loader = resource_loader
        self._normalizer = resource_loader.query_factory.normalize
        self.type = entity_type
        self._is_system_entity = Entity.is_system_entity(self.type)

        self._exact_match_mapping = None

        er_config = get_classifier_config('entity_resolution', app_path=app_path)
        self._use_text_rel = er_config['model_type'] == 'text_relevance'
        self._use_double_metaphone = 'double_metaphone' in er_config.get('phonetic_match_types', [])
        self._es_host = es_host
        self.__es_client = es_client
        self._pid = os.getpid()
        self._es_index_name = EntityResolver.ES_SYNONYM_INDEX_PREFIX + "_" + entity_type

    @property
    def _es_client(self):
        # Lazily connect to Elasticsearch.  Make sure each subprocess gets it's own connection
        if self.__es_client is None or self._pid != os.getpid():
            self._pid = os.getpid()
            self.__es_client = create_es_client()
        return self.__es_client

    @classmethod
    def ingest_synonym(cls, app_namespace, index_name, index_type=INDEX_TYPE_SYNONYM,
                       field_name=None, data=[], es_host=None, es_client=None,
                       use_double_metaphone=False):
        """Loads synonym documents from the mapping.json data into the
        specified index. If an index with the specified name doesn't exist, a
        new index with that name will be created.

        Args:
            app_namespace (str): The namespace of the app. Used to prevent
                collisions between the indices of this app and those of other
                apps.
            index_name (str): The name of the new index to be created
            index_type (str): specify whether to import to synonym index or
                knowledge base object index. INDEX_TYPE_SYNONYM is the default
                which indicates the synonyms to be imported to synonym index,
                while INDEX_TYPE_KB indicates that the synonyms should be
                imported into existing knowledge base index.
            field_name (str): specify name of the knowledge base field that the
                synonym list corresponds to when index_type is
                INDEX_TYPE_SYNONYM.
            data (list): A list of documents to be loaded into the index
            es_host (str): The Elasticsearch host server
            es_client (Elasticsearch): The Elasticsearch client
            use_double_metaphone (bool): Whether to use the phonetic mapping or not
        """
        def _action_generator(docs):

            for doc in docs:
                action = {}

                # id
                if doc.get('id'):
                    action['_id'] = doc['id']
                else:
                    # generate hash from canonical name as ID
                    action['_id'] = hashlib.sha256(doc.get('cname').encode('utf-8')).hexdigest()

                # synonym whitelist
                whitelist = doc['whitelist']
                syn_list = []
                syn_list.append({"name": doc['cname']})
                for syn in whitelist:
                    syn_list.append({"name": syn})

                # If index type is INDEX_TYPE_KB  we import the synonym into knowledge base object
                # index by updating the knowledge base object with additional synonym whitelist
                # field. Otherwise, by default we import to synonym index in ES.
                if index_type == INDEX_TYPE_KB and field_name:
                    syn_field = field_name + "$whitelist"
                    action['_op_type'] = 'update'
                    action['doc'] = {syn_field: syn_list}
                else:
                    action.update(doc)
                    action['whitelist'] = syn_list

                yield action

        mapping = PHONETIC_ES_SYNONYM_MAPPING if use_double_metaphone else \
            DEFAULT_ES_SYNONYM_MAPPING
        load_index(app_namespace, index_name, _action_generator(data), len(data),
                   mapping, DOC_TYPE, es_host, es_client)

    def fit(self, clean=False):
        """Loads an entity mapping file to Elasticsearch for text relevance based entity resolution.

        In addition, the synonyms in entity mapping are imported to knowledge base indexes if the
        corresponding knowledge base object index and field name are specified for the entity type.
        The synonym info is then used by Question Answerer for text relevance matches.

        Args:
            clean (bool): If True, deletes and recreates the index from scratch instead of
                          updating the existing index with synonyms in the mapping.json
        """
        if self._is_system_entity:
            return

        if not self._use_text_rel:
            self._fit_exact_match()
            return

        if clean:
            delete_index(self._app_namespace, self._es_index_name, self._es_host,
                         self._es_client)
        entity_map = self._resource_loader.get_entity_map(self.type)

        # list of canonical entities and their synonyms
        entities = entity_map.get('entities', [])

        # create synonym index and import synonyms
        logger.info("Importing synonym data to synonym index '{}'".format(self._es_index_name))
        EntityResolver.ingest_synonym(app_namespace=self._app_namespace,
                                      index_name=self._es_index_name, data=entities,
                                      es_host=self._es_host, es_client=self._es_client,
                                      use_double_metaphone=self._use_double_metaphone)

        # It's supported to specify the KB object type and field name that the NLP entity type
        # corresponds to in the mapping.json file. In this case the synonym whitelist is also
        # imported to KB object index and the synonym info will be used when using Question Answerer
        # for text relevance matches.
        kb_index = entity_map.get('kb_index_name')
        kb_field = entity_map.get('kb_field_name')

        # if KB index and field name is specified then also import synonyms into KB object index.
        if kb_index and kb_field:
            # validate the KB index and field are valid.
            # TODO: this validation can probably be in some other places like resource loader.
            if not does_index_exist(self._app_namespace, kb_index, self._es_host, self._es_client):
                raise ValueError("Cannot import synonym data to knowledge base. The knowledge base "
                                 "index name \'{}\' is not valid.".format(kb_index))
            if kb_field not in get_field_names(self._app_namespace, kb_index, self._es_host,
                                               self._es_client):
                raise ValueError("Cannot import synonym data to knowledge base. The knowledge base "
                                 "field name \'{}\' is not valid.".format(kb_field))
            if entities and not entities[0].get('id'):
                raise ValueError("Knowledge base index and field cannot be specified for entities "
                                 "without ID.")
            logger.info("Importing synonym data to knowledge base index '{}'".format(kb_index))
            EntityResolver.ingest_synonym(app_namespace=self._app_namespace, index_name=kb_index,
                                          index_type='kb', field_name=kb_field, data=entities,
                                          es_host=self._es_host, es_client=self._es_client,
                                          use_double_metaphone=self._use_double_metaphone)

    @staticmethod
    def _process_entity_map(entity_type, entity_map, normalizer):
        """Loads in the mapping.json file and stores the synonym mappings in a item_map and a
        synonym_map for exact match entity resolution when Elasticsearch is unavailable

        Args:
            entity_type: The entity type associated with this entity resolver
            entity_map: The loaded mapping.json file for the given entity type
            normalizer: The normalizer to use
        """
        item_map = {}
        syn_map = {}
        seen_ids = []
        for item in entity_map.get('entities'):
            cname = item['cname']
            item_id = item.get('id')
            if cname in item_map:
                msg = 'Canonical name {!r} specified in {!r} entity map multiple times'
                logger.debug(msg.format(cname, entity_type))
            if item_id:
                if item_id in seen_ids:
                    msg = 'Item id {!r} specified in {!r} entity map multiple times'
                    raise ValueError(msg.format(item_id, entity_type))
                seen_ids.append(item_id)

            aliases = [cname] + item.pop('whitelist', [])
            items_for_cname = item_map.get(cname, [])
            items_for_cname.append(item)
            item_map[cname] = items_for_cname
            for alias in aliases:
                norm_alias = normalizer(alias)
                if norm_alias in syn_map:
                    msg = 'Synonym {!r} specified in {!r} entity map multiple times'
                    logger.debug(msg.format(cname, entity_type))
                cnames_for_syn = syn_map.get(norm_alias, [])
                cnames_for_syn.append(cname)
                syn_map[norm_alias] = list(set(cnames_for_syn))

        return {'items': item_map, 'synonyms': syn_map}

    def _fit_exact_match(self):
        """Fits a simple exact match entity resolution model when Elasticsearch is not available.
        """
        entity_map = self._resource_loader.get_entity_map(self.type)
        self._exact_match_mapping = self._process_entity_map(self.type, entity_map,
                                                             self._normalizer)

    def predict(self, entity):
        """Predicts the resolved value(s) for the given entity using the loaded entity map or the
        trained entity resolution model

        Args:
            entity (Entity, or tuple): An entity found in an input query, or a list of n-best entity
                                       objects

        Returns:
            The top 20 resolved values for the provided entity
        """
        if isinstance(entity, (list, tuple)):
            top_entity = entity[0]
            entity = tuple(entity)
        else:
            top_entity = entity
            entity = tuple([entity])

        if self._is_system_entity:
            # system entities are already resolved
            return [top_entity.value]

        if not self._use_text_rel:
            return self._predict_exact_match(top_entity)

        weight_factors = [1 - float(i) / len(entity) for i in range(len(entity))]

        def _construct_match_query(entity, weight=1):
            return [
                       {
                            "match": {
                                "cname.normalized_keyword": {
                                    "query": entity.text,
                                    "boost": 10 * weight
                                }
                            }
                       },
                       {
                            "match": {
                                "cname.raw": {
                                    "query": entity.text,
                                    "boost": 10 * weight
                                }
                            }
                       }
                   ]

        def _construct_phonetic_match_query(entity, weight=1):
            return [
                       {
                            "match": {
                                "cname.double_metaphone": {
                                    "query": entity.text,
                                    "boost": 2 * weight
                                }
                            }
                       }
                    ]

        def _construct_whitelist_query(entity, weight=1, use_phons=False):
            query = {
                        "nested": {
                            "path": "whitelist",
                            "score_mode": "max",
                            "query": {
                                "bool": {
                                    "should": [
                                        {
                                            "match": {
                                                "whitelist.name.normalized_keyword": {
                                                    "query": entity.text,
                                                    "boost": 10 * weight
                                                }
                                            }
                                        },
                                        {
                                            "match": {
                                                "whitelist.name": {
                                                    "query": entity.text,
                                                    "boost": weight
                                                }
                                            }
                                        },
                                        {
                                            "match": {
                                                "whitelist.name.char_ngram": {
                                                    "query": entity.text,
                                                    "boost": weight
                                                }
                                            }
                                        }
                                    ]
                                }
                            },
                            "inner_hits": {}
                        }
                   }

            if use_phons:
                query["nested"]["query"]["bool"]["should"].append(
                   {
                        "match": {
                            "whitelist.double_metaphone": {
                                "query": entity.text,
                                "boost": weight
                            }
                        }
                   }
                )

            return query

        text_relevance_query = {
            "query": {
                "function_score": {
                    "query": {
                        "bool": {
                            "should": []
                        }
                    },
                    "field_value_factor": {
                        "field": "sort_factor",
                        "modifier": "log1p",
                        "factor": 10,
                        "missing": 0
                    },
                    "boost_mode": "sum",
                    "score_mode": "sum"
                }
            }
        }

        match_query = []
        for e, weight in zip(entity, weight_factors):
            match_query.extend(_construct_match_query(e, weight))
            if self._use_double_metaphone:
                match_query.extend(_construct_phonetic_match_query(e, weight))
        text_relevance_query["query"]["function_score"]["query"]["bool"]["should"].append(
            {"bool": {"should": match_query}})

        whitelist_query = _construct_whitelist_query(top_entity,
                                                     use_phons=self._use_double_metaphone)
        text_relevance_query["query"]["function_score"]["query"]["bool"]["should"].append(
            whitelist_query)

        try:
            index = get_scoped_index_name(self._app_namespace, self._es_index_name)
            response = self._es_client.search(index=index, body=text_relevance_query)
        except ConnectionError as e:
            logger.error(
                'Unable to connect to Elasticsearch: {} details: {}'.format(e.error, e.info))
            raise EntityResolverConnectionError(es_host=self._es_client.transport.hosts)
        except TransportError as e:
            logger.error('Unexpected error occurred when sending requests to Elasticsearch: {} '
                         'Status code: {} details: {}'.format(e.error, e.status_code, e.info))
            raise EntityResolverError('Unexpected error occurred when sending requests to '
                                      'Elasticsearch: {} Status code: {} details: '
                                      '{}'.format(e.error, e.status_code, e.info))
        except ElasticsearchException:
            raise EntityResolverError
        else:
            hits = response['hits']['hits']

            results = []
            for hit in hits:
                top_synonym = None
                synonym_hits = hit['inner_hits']['whitelist']['hits']['hits']
                if len(synonym_hits) > 0:
                    top_synonym = synonym_hits[0]['_source']['name']
                result = {
                    'cname': hit['_source']['cname'],
                    'score': hit['_score'],
                    'top_synonym': top_synonym}

                if hit['_source'].get('id'):
                    result['id'] = hit['_source'].get('id')

                if hit['_source'].get('sort_factor'):
                    result['sort_factor'] = hit['_source'].get('sort_factor')

                results.append(result)

            return results[0:20]

    def _predict_exact_match(self, entity):
        """Predicts the resolved value(s) for the given entity using the loaded entity map.

        Args:
            entity (Entity): An entity found in an input query
        """
        normed = self._normalizer(entity.text)
        try:
            cnames = self._exact_match_mapping['synonyms'][normed]
        except KeyError:
            logger.warning('Failed to resolve entity %r for type %r', entity.text, entity.type)
            return None

        if len(cnames) > 1:
            logger.info('Multiple possible canonical names for %r entity for type %r',
                        entity.text, entity.type)

        values = []
        for cname in cnames:
            for item in self._exact_match_mapping['items'][cname]:
                item_value = copy.copy(item)
                item_value.pop('whitelist', None)
                values.append(item_value)

        return values

    def predict_proba(self, entity):
        """Runs prediction on a given entity and generates multiple hypotheses with their
        associated probabilities using the trained entity resolution model

        Args:
            entity (Entity): An entity found in an input query

        Returns:
            list: a list of tuples of the form (str, float) grouping resolved values and their
                probabilities
        """
        pass

    def evaluate(self, use_blind=False):
        """Evaluates the trained entity resolution model on the given test data

        Returns:
            TYPE: Description
        """
        pass

    def dump(self, model_path):
        """Persists the trained entity resolution model to disk.

        Args:
            model_path (str): The location on disk where the model should be stored
        """
        pass

    def load(self):
        """Loads the trained entity resolution model from disk

        Args:
            model_path (str): The location on disk where the model is stored
        """
        try:
            if self._use_text_rel:
                scoped_index_name = get_scoped_index_name(self._app_namespace, self._es_index_name)
                if not self._es_client.indices.exists(index=scoped_index_name):
                    self.fit()
            else:
                self.fit()

        except ConnectionError as e:
            logger.error(
                'Unable to connect to Elasticsearch: {} details: {}'.format(e.error, e.info))
            raise EntityResolverConnectionError(es_host=self._es_client.transport.hosts)
        except TransportError as e:
            logger.error('Unexpected error occurred when sending requests to Elasticsearch: {} '
                         'Status code: {} details: {}'.format(e.error, e.status_code, e.info))
            raise EntityResolverError
        except ElasticsearchException:
            raise EntityResolverError
