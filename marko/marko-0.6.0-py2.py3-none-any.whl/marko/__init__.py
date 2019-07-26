#! -*- coding: utf-8 -*-
"""
  _    _     _     ___   _  _    ___
 | \  / |   /_\   | _ \ | |/ /  / _ \
 | |\/| |  / _ \  |   / | ' <  | (_) |
 |_|  |_| /_/ \_\ |_|_\ |_|\_\  \___/

 A markdown parser with high extensibility.

 Licensed under MIT.
 Created by Frost Ming<mianghong@gmail.com>
"""
from .html_renderer import HTMLRenderer
from .renderer import Renderer
from .parser import Parser
from .helpers import is_type_check

if is_type_check():
    from typing import Type, List, Any, Optional
    from .block import Document
    from .parser import ElementType

__version__ = "0.6.0"


class SetupDone(Exception):
    def __str__(self):
        return "Unable to register more extensions after setup done."


class Markdown(object):
    """The main class to convert markdown documents.

    Attributes:
        * parser: an instance of :class:`marko.parser.Parser`
        * renderer: an instance of :class:`marko.renderer.Renderer`

    :param parser: a subclass :class:`marko.parser.Parser`.
    :param renderer: a subclass :class:`marko.renderer.Renderer`.
    :param extensions: a list of extensions to register on the object.
    """

    def __init__(self, parser=Parser, renderer=HTMLRenderer, extensions=None):
        # type: (Type[Parser], Type[Renderer], Optional[Any]) -> None
        assert issubclass(parser, Parser)
        self._base_parser = parser
        self._parser_mixins = []  # type: List[Any]

        assert issubclass(renderer, Renderer)
        self._base_renderer = renderer
        self._renderer_mixins = []  # type: List[Any]

        self._extra_elements = []  # type: List[ElementType]

        self._setup_done = False

        if extensions:
            self.use(*extensions)

    def use(self, *extensions):  # type: (Any) -> None
        """Register extensions to Markdown object.
        An extension should be an object providing ``parser_mixins`` or
        ``renderer_mixins`` attributes or both. The extension can also provide elements
        attribute to contain all elements to be added.
        Note that Marko uses a mixin based extension system, the order of extensions
        matters: An extension preceding in order will have higher priorty.

        :param \*extensions: one or many extension objects.
        """
        if self._setup_done:
            raise SetupDone()
        for extension in extensions:
            self._parser_mixins = (
                getattr(extension, "parser_mixins", []) + self._parser_mixins
            )
            self._renderer_mixins = (
                getattr(extension, "renderer_mixins", []) + self._renderer_mixins
            )
            self._extra_elements.extend(getattr(extension, "elements", []))

    def _setup_extensions(self):  # type: () -> None
        """Install all extensions and set things up."""
        if self._setup_done:
            return
        self.parser = type(
            "MarkdownParser", tuple(self._parser_mixins) + (self._base_parser,), {}
        )()
        for e in self._extra_elements:
            self.parser.add_element(e)
        self.renderer = type(
            "MarkdownRenderer",
            tuple(self._renderer_mixins) + (self._base_renderer,),
            {},
        )()
        self._setup_done = True

    def convert(self, text):  # type: (str) -> str
        """Parse and render the given text."""
        return self.render(self.parse(text))

    def __call__(self, text):  # type: (str) -> str
        return self.convert(text)

    def parse(self, text):  # type: (str) -> Document
        """Call ``self.parser.parse(text)``.

        Override this to preprocess text or handle parsed result.
        """
        self._setup_extensions()
        return self.parser.parse(text)

    def render(self, parsed):  # type: (Document) -> str
        """Call ``self.renderer.render(text)``.

        Override this to handle parsed result.
        """
        self.renderer.root_node = parsed
        with self.renderer as r:
            return r.render(parsed)


# Inner instance, use the bare convert/parse/render function instead
_markdown = Markdown()


def convert(text):  # type: (str) -> str
    """Parse and render the given text.

    :param text: text to convert.
    :returns: The rendered result.
    """
    return _markdown.convert(text)


def parse(text):  # type: (str) -> Document
    """Parse the text to a structured data object.

    :param text: text to parse.
    :returns: the parsed object
    """
    return _markdown.parse(text)


def render(parsed):  # type: (Document) -> str
    """Render the parsed object to text.

    :param parsed: the parsed object
    :returns: the rendered result.
    """
    return _markdown.render(parsed)
