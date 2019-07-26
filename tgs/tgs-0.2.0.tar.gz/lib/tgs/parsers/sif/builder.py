import math
from xml.dom import minidom

from ... import objects
from ...utils import restructure


blend_modes = {
    objects.BlendMode.Normal: 0, # composite
    objects.BlendMode.Multiply: 6,
    objects.BlendMode.Screen: 16,
    objects.BlendMode.Overlay: 20,
    objects.BlendMode.Darken: 3,
    objects.BlendMode.Lighten: 2,
    objects.BlendMode.HardLight: 17,
    objects.BlendMode.Difference: 18,
    objects.BlendMode.Hue: 9,
    objects.BlendMode.Saturation: 10,
    objects.BlendMode.Color: 8,
    objects.BlendMode.Luminosity: 11,
    #1  : "straight",
    #13 : "onto",
    #21 : "straight onto",
    #12 : "behind",
    #7  : "divide",
    #4  : "add",
    #5  : "subtract",
    objects.BlendMode.Exclusion: 18,
    objects.BlendMode.SoftLight: 6,
    objects.BlendMode.ColorDodge: 0,
    objects.BlendMode.ColorBurn: 0,
}


class SifBuilder(restructure.AbstractBuilder):
    def __init__(self):
        super().__init__()
        self.dom = minidom.Document()
        self.canvas = self.dom.appendChild(self.dom.createElement("canvas"))
        self.canvas.setAttribute("version", "1.0")

    def _format_time_f(self, time):
        return "%sf" % time

    def _format_time(self, time):
        return "%ss" % (time / self.framerate)

    def _subelement(self, parent, tagname):
        return parent.appendChild(self.dom.createElement(tagname))

    def _settext(self, element, text):
        element.appendChild(self.dom.createTextNode(text))

    def _on_animation(self, animation: objects.Animation):
        if animation.name:
            self._settext(self._subelement(self.canvas, "name"), animation.name)
        self.canvas.setAttribute("width", str(animation.width))
        self.canvas.setAttribute("height", str(animation.height))
        self.canvas.setAttribute("xres", str(animation.width))
        self.canvas.setAttribute("yres", str(animation.height))
        self.canvas.setAttribute("view-box", "0 0 %s %s" % (animation.width, animation.height))
        self.canvas.setAttribute("fps", str(animation.frame_rate))
        self.canvas.setAttribute("begin-time", self._format_time_f(animation.in_point))
        self.canvas.setAttribute("end-time", self._format_time_f(animation.out_point))
        self.canvas.setAttribute("antialias", "1")
        self.framerate = animation.frame_rate
        self.end_frame = animation.out_point
        self.width = animation.width
        self.height = animation.height
        return self.canvas

    def _on_layer(self, layer_builder, dom_parent):
        layer = self.layer_from_lottie("group", layer_builder.lottie, dom_parent)
        if not layer_builder.lottie.name:
            layer.setAttribute("desc", layer_builder.lottie.__class__.__name__)

        bm = getattr(layer_builder.lottie, "blend_mode", objects.BlendMode.Normal)
        self.simple_param("blend_method", bm, layer, "integer").setAttribute("static", "true")

        stretch = getattr(layer_builder.lottie, "stretch", 1) or 1
        self.simple_param("time_dilation", stretch, layer)

        in_point = getattr(layer_builder.lottie, "in_point", 0)
        self.simple_param("time_offset", self._format_time(in_point), layer, "time")

        pcanv = self._subelement(layer, "param")
        pcanv.setAttribute("name", "canvas")
        canvas = self._subelement(pcanv, "canvas")
        out_point = getattr(layer_builder.lottie, "out_point", self.end_frame)
        canvas.setAttribute("end-time", self._format_time(out_point))
        return canvas

    def layer_from_lottie(self, type, lottie, dom_parent):
        g = self._subelement(dom_parent, "layer")
        g.setAttribute("type", type)
        g.setAttribute("active", "true")
        g.setAttribute("exclude_from_rendering", "false")
        #g.setAttribute("version", "0.2")
        if lottie.name:
            g.setAttribute("desc", lottie.name)

        transf = getattr(lottie, "transform", None)
        if transf:
            self.set_transform(g, lottie.transform)
        return g

    def set_transform(self, group, transform):
        param = self._subelement(group, "param")
        param.setAttribute("name", "transformation")
        composite = self._subelement(param, "composite")
        composite.setAttribute("type", "transformation")
        self.process_vector("offset", transform.position, composite)

        keyframes = self._merge_keyframes([transform.scale, transform.skew])

        def get_scale(keyframe, elem):
            t = keyframe.time if keyframe else 0
            scale_x, scale_y = transform.scale.get_value(t)[:2]
            scale_x /= 100
            scale_y /= 100
            skew = transform.skew.get_value(t) if transform.skew else 0
            c = math.cos(skew * math.pi / 180)
            if c != 0:
                scale_y *= 1 / c
            self._settext(self._subelement(elem, "x"), str(scale_x))
            self._settext(self._subelement(elem, "y"), str(scale_y))

        self.process_vector_ext("scale", keyframes, composite, "vector", get_scale)
        #self.process_vector_ext("scale", transform.scale.keyframes, composite, "vector", get_scale)
        self.process_scalar("angle", "skew_angle", transform.skew or objects.Value(0), composite)
        self.process_scalar("angle", "angle", transform.rotation, composite)
        self.process_scalar("real", "param", transform.opacity, group, 1/100).setAttribute("name", "amount")
        self.process_vector("param", transform.anchor_point, group).setAttribute("name", "origin")
        # TODO get z_depth from position
        self.process_scalar("real", "param", objects.Value(0), group).setAttribute("name", "z_depth")

    def process_vector(self, name, multidim, parent):
        def getter(keyframe, elem):
            if keyframe is None:
                v = multidim.value
            else:
                v = keyframe.start
            self._settext(self._subelement(elem, "x"), str(v[0]))
            self._settext(self._subelement(elem, "y"), str(v[1]))

        return self.process_vector_ext(name, multidim.keyframes, parent, "vector", getter)

    def process_vector(self, name, multidim, parent):
        def getter(keyframe, elem):
            if keyframe is None:
                v = multidim.value
            else:
                v = keyframe.start
            self._settext(self._subelement(elem, "x"), str(v[0]))
            self._settext(self._subelement(elem, "y"), str(v[1]))

        return self.process_vector_ext(name, multidim.keyframes, parent, "vector", getter)

    def process_vector_ext(self, name, kframes, parent, type, getter):
        wrap = self._subelement(parent, name)
        if kframes is not None:
            animated = self._subelement(wrap, "animated")
            animated.setAttribute("type", type)
            for keyframe in kframes:
                waypoint = self._subelement(animated, "waypoint")
                waypoint.setAttribute("time", self._format_time(keyframe.time))
                waypoint.setAttribute("before", "clamped")
                waypoint.setAttribute("after", "clamped")
                vector = self._subelement(waypoint, type)
                getter(keyframe, vector)
        else:
            vector = self._subelement(wrap, type)
            getter(None, vector)
        return wrap

    def process_scalar(self, type, name, value, parent, mult=None):
        def getter(keyframe, elem):
            if keyframe is None:
                v = value.value
            else:
                v = keyframe.start[0]
            if mult is not None:
                v *= mult
            elem.setAttribute("value", str(v))
        return self.process_vector_ext(name, value.keyframes, parent, type, getter)

    def simple_param(self, name, vaue, parent, type="real"):
        param = self._subelement(parent, "param")
        param.setAttribute("name", name)
        e_val = self._subelement(param, type)
        e_val.setAttribute("value", str(vaue))
        return e_val

    def simple_composite_param(self, name, vaue, parent, type="real"):
        param = self._subelement(parent, name)
        e_val = self._subelement(param, type)
        e_val.setAttribute("value", str(vaue))
        return e_val

    def _on_shape(self, shape, group, dom_parent):
        layers = []
        if group.fill:
            sif_shape = self.build_path("region", shape.to_bezier(), dom_parent)
            layers.append(sif_shape)
            self.apply_group_fill(sif_shape, group.fill)

        if group.stroke:
            sif_shape = self.build_path("outline", shape.to_bezier(), dom_parent)
            self.apply_group_stroke(sif_shape, group.stroke)
            layers.append(sif_shape)

        return layers

    def _merge_keyframes(self, props):
        keyframes = {}
        for prop in props:
            if prop is not None and prop.animated:
                keyframes.update({kf.time: kf for kf in prop.keyframes})
        return list(sorted(keyframes.values(), key=lambda kf: kf.time)) or None

    def apply_group_fill(self, sif_shape, fill):
        # TODO gradients?
        if hasattr(fill, "colors"):
            return

        def getter(keyframe, elem):
            if keyframe is None:
                v = fill.color.value
            else:
                v = keyframe.start
            self._settext(self._subelement(elem, "r"), str(v[0]))
            self._settext(self._subelement(elem, "g"), str(v[1]))
            self._settext(self._subelement(elem, "b"), str(v[2]))
            self._settext(self._subelement(elem, "a"), "1")

        self.process_vector_ext("param", fill.color.keyframes, sif_shape, "color", getter).setAttribute("name", "color")

        def get_op(keyframe, elem):
            if keyframe is None:
                v = fill.opacity.value
            else:
                v = keyframe.start
            v /= 100
            elem.setAttribute("value", str(v))

        self.process_vector_ext("param", fill.opacity.keyframes, sif_shape, "real", get_op).setAttribute("name", "amount")

    def apply_group_stroke(self, sif_shape, stroke):
        self.apply_group_fill(sif_shape, stroke)
        cusp = self._format_bool(stroke.line_join == objects.LineJoin.Miter)
        self.simple_param("sharp_cusps", cusp, sif_shape, "bool")
        round_cap = self._format_bool(stroke.line_cap == objects.LineCap.Round)
        self.simple_param("round_tip[0]", round_cap, sif_shape, "bool")
        self.simple_param("round_tip[1]", round_cap, sif_shape, "bool")
        self.process_scalar("real", "param", stroke.width, sif_shape).setAttribute("name", "width")

    def _format_bool(self, value):
        return str(bool(value)).lower()

    def build_path(self, type, path, dom_parent):
        layer = self.layer_from_lottie(type, path, dom_parent)
        bline_par = self._subelement(layer, "param")
        bline_par.setAttribute("name", "bline")
        bline = self._subelement(bline_par, "bline")
        bline.setAttribute("type", "bline_point")
        startbez = path.shape.get_value()
        bline.setAttribute("loop", self._format_bool(startbez.closed))
        nverts = len(startbez.vertices)
        for point in range(nverts):
            self.bezier_point(path, point, bline)
        return layer

    def bezier_point(self, lottie_path, point_index, sif_parent):
        entry = self._subelement(sif_parent, "entry")
        composite = self._subelement(entry, "composite")
        composite.setAttribute("type", "bline_point")

        def get_point(keyframe, elem):
            if keyframe is None:
                bezier = lottie_path.shape.value
            else:
                bezier = keyframe.start
            if not bezier:
                elem.parentNode.parentNode.removeChild(elem.parentNode)
                return
            vert = bezier.vertices[point_index]
            self._settext(self._subelement(elem, "x"), str(vert[0]))
            self._settext(self._subelement(elem, "y"), str(vert[1]))

        self.process_vector_ext("point", lottie_path.shape.keyframes, composite, "vector", get_point)
        self.simple_composite_param("split", "true", composite, "bool")
        self.simple_composite_param("split_radius", "true", composite, "bool")
        self.simple_composite_param("split_angle", "true", composite, "bool")
        self.simple_composite_param("width", "1.0", composite, "real")
        self.simple_composite_param("origin", "0.5", composite, "real")

        def get_tangent_r(keyframe, elem):
            if keyframe is None:
                bezier = lottie_path.shape.value
            else:
                bezier = keyframe.start
            if not bezier:
                elem.parentNode.parentNode.removeChild(elem.parentNode)
                return

            inp = getattr(bezier, which_point)[point_index]
            radius = math.hypot(inp.x, inp.y) * 3 * mult
            elem.setAttribute("value", str(radius))

        def get_tangent_th(keyframe, elem):
            if keyframe is None:
                bezier = lottie_path.shape.value
            else:
                bezier = keyframe.start
            if not bezier:
                elem.parentNode.parentNode.removeChild(elem.parentNode)
                return

            inp = getattr(bezier, which_point)[point_index]
            theta = math.atan2(inp[1], inp[0]) * 180 / math.pi
            elem.setAttribute("value", str(theta))

        mult = -1
        which_point = "in_point"
        radial_composite = self._subelement(self._subelement(composite, "t1"), "radial_composite")
        radial_composite.setAttribute("type", "vector")
        self.process_vector_ext("radius", lottie_path.shape.keyframes, radial_composite, "real", get_tangent_r)
        self.process_vector_ext("theta", lottie_path.shape.keyframes, radial_composite, "angle", get_tangent_th)

        mult = 1
        which_point = "out_point"
        radial_composite = self._subelement(self._subelement(composite, "t2"), "radial_composite")
        radial_composite.setAttribute("type", "vector")
        self.process_vector_ext("radius", lottie_path.shape.keyframes, radial_composite, "real", get_tangent_r)
        self.process_vector_ext("theta", lottie_path.shape.keyframes, radial_composite, "angle", get_tangent_th)

    def _on_shapegroup(self, shape_group, dom_parent):
        if shape_group.empty():
            return

        layer = self.layer_from_lottie("group", shape_group.lottie, dom_parent)

        pcanv = self._subelement(layer, "param")
        pcanv.setAttribute("name", "canvas")
        canvas = self._subelement(pcanv, "canvas")
        self.shapegroup_process_children(shape_group, canvas)


def to_sif(animation):
    builder = SifBuilder()
    builder.process(animation)
    return builder.dom
