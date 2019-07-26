from base import NotifierBase
from compressor import Compressor
from errors import Error, ErrorCodes
from stream_connect.connector import StreamPublisher

REPUBLISH_METHOD = 'KAFKA'

class Notifier(NotifierBase):

    @staticmethod
    def _compress(payload):
        compressor = Compressor(payload)
        return compressor.compress()

    @staticmethod
    def _get_publishing_payload(message_id, topic, payload, status, timestamp,
        offset, partition, **kwargs):
        """Returns the publishing payload"""
        data = dict(
            message_id=message_id,
            topic=topic,
            offset=offset,
            partition=partition,
            timestamp=timestamp,
            status=status,
            payload=payload
        )
        data.update(**kwargs)
        return data

    def _publish(self, data, compression):
        """Publishes the data to the republisher"""
        try:
            publisher = StreamPublisher(REPUBLISH_METHOD, self.host, self.topic)
            publisher_response = publisher.publish({
                'payload': data,
                'compression': compression
            })
            if not publisher_response.success:
                self.response.errors.extend(publisher_response.errors)
                raise Error(ErrorCodes.StreamConnectError)
        except Exception as e:
            raise Error(ErrorCodes.StreamConnectError)

    def process(self, message_id, topic, payload, status, timestamp, offset=None,
            partition=None, compression=True, **kwargs):
        """
        Generates the re-publishing payload and publishes it to the republisher
        """
        try:
            data = Notifier._get_publishing_payload(
                message_id, topic, payload, status, timestamp, offset, partition, **kwargs)
            compressed_data = Notifier._compress(data) if compression else data
            self._publish(compressed_data, compression)
            self.response.success = True
        except Error as e:
            self.response.errors.append(e.get_error())


# a = Notifier('localhost:9092', 'Dev.Godam.agn.info')
# a.process('message_id', 'Dev.Godam.agn.info', {"key": "value"}, 'PUBLISHED', '2018-09-7', 1, 0, False, extra='abc')