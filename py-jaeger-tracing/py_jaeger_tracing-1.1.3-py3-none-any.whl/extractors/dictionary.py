from opentracing import Format
from opentracing import Reference
from opentracing import ReferenceType

from py_jaeger_tracing.main import TracingEnvironment


class TracingDictExtractor:
    def __init__(self, operation='child'):
        self._operation = operation

    def _extract(self, carrier):
        span_ctx = TracingEnvironment.tracer.extract(
            format=Format.TEXT_MAP,
            carrier=carrier
        )

        references = [Reference(ReferenceType.FOLLOWS_FROM, span_ctx)]
        if len(TracingEnvironment.spans) > 0:
            references += [Reference(ReferenceType.FOLLOWS_FROM, TracingEnvironment.spans[-1])]

        span = TracingEnvironment.tracer.start_span(
            operation_name=self._operation,
            references=references
        )

        TracingEnvironment.spans.append(span)
        span.finish()

    def extract(self, carrier):
        if TracingEnvironment.tracer:
            self._extract(carrier)
