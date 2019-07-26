"""
Hermite Genz-Keister 16 rule.
"""

import numpy

def quad_genz_keister_16(order):
    """
    Hermite Genz-Keister 16 rule.

    Args:
        order (int):
            The quadrature order. Must be in the interval (0, 8).

    Returns:
        (:py:data:typing.Tuple[numpy.ndarray, numpy.ndarray]):
            Abscissas and weights

    Examples:
        >>> abscissas, weights = quad_genz_keister_16(1)
        >>> print(numpy.around(abscissas, 4))
        [-1.7321  0.      1.7321]
        >>> print(numpy.around(weights, 4))
        [0.1667 0.6667 0.1667]
    """
    order = sorted(GENZ_KEISTER_16.keys())[order]

    abscissas, weights = GENZ_KEISTER_16[order]
    abscissas = numpy.array(abscissas)
    weights = numpy.array(weights)

    weights /= numpy.sum(weights)
    abscissas *= numpy.sqrt(2)

    return abscissas, weights


GENZ_KEISTER_16 = {
    1 : ((
        0.0000000000000000E+00,
    ), (
        1.7724538509055159E+00,
    )),
    3 : ((
        -1.2247448713915889E+00,
        0.0000000000000000E+00,
        1.2247448713915889E+00,
    ), (
        2.9540897515091930E-01,
        1.1816359006036772E+00,
        2.9540897515091930E-01,
    )),
    7 : ((
        -2.9592107790638380E+00,
        -1.2247448713915889E+00,
        -5.2403354748695763E-01,
        0.0000000000000000E+00,
        5.2403354748695763E-01,
        1.2247448713915889E+00,
        2.9592107790638380E+00,
    ), (
        1.2330680655153448E-03,
        2.4557928535031393E-01,
        2.3286251787386100E-01,
        8.1310410832613500E-01,
        2.3286251787386100E-01,
        2.4557928535031393E-01,
        1.2330680655153448E-03,
    )),
    9 : ((
        -2.9592107790638380E+00,
        -2.0232301911005157E+00,
        -1.2247448713915889E+00,
        -5.2403354748695763E-01,
        0.0000000000000000E+00,
        5.2403354748695763E-01,
        1.2247448713915889E+00,
        2.0232301911005157E+00,
        2.9592107790638380E+00,
    ), (
        1.6708826306882348E-04,
        1.4173117873979098E-02,
        1.6811892894767771E-01,
        4.7869428549114124E-01,
        4.5014700975378197E-01,
        4.7869428549114124E-01,
        1.6811892894767771E-01,
        1.4173117873979098E-02,
        1.6708826306882348E-04,
    )),
    17 : ((
        -4.4995993983103881E+00,
        -3.6677742159463378E+00,
        -2.9592107790638380E+00,
        -2.0232301911005157E+00,
        -1.8357079751751868E+00,
        -1.2247448713915889E+00,
        -8.7004089535290285E-01,
        -5.2403354748695763E-01,
        0.0000000000000000E+00,
        5.2403354748695763E-01,
        8.7004089535290285E-01,
        1.2247448713915889E+00,
        1.8357079751751868E+00,
        2.0232301911005157E+00,
        2.9592107790638380E+00,
        3.6677742159463378E+00,
        4.4995993983103881E+00,
    ), (
        3.7463469943051758E-08,
        -1.4542843387069391E-06,
        1.8723818949278350E-04,
        1.2466519132805918E-02,
        3.4840719346803800E-03,
        1.5718298376652240E-01,
        2.5155825701712934E-02,
        4.5119803602358544E-01,
        4.7310733504965385E-01,
        4.5119803602358544E-01,
        2.5155825701712934E-02,
        1.5718298376652240E-01,
        3.4840719346803800E-03,
        1.2466519132805918E-02,
        1.8723818949278350E-04,
        -1.4542843387069391E-06,
        3.7463469943051758E-08,
    )),
    19 : ((
        -4.4995993983103881E+00,
        -3.6677742159463378E+00,
        -2.9592107790638380E+00,
        -2.2665132620567876E+00,
        -2.0232301911005157E+00,
        -1.8357079751751868E+00,
        -1.2247448713915889E+00,
        -8.7004089535290285E-01,
        -5.2403354748695763E-01,
        0.0000000000000000E+00,
        5.2403354748695763E-01,
        8.7004089535290285E-01,
        1.2247448713915889E+00,
        1.8357079751751868E+00,
        2.0232301911005157E+00,
        2.2665132620567876E+00,
        2.9592107790638380E+00,
        3.6677742159463378E+00,
        4.4995993983103881E+00,
    ), (
        1.5295717705322357E-09,
        1.0802767206624762E-06,
        1.0656589772852267E-04,
        5.1133174390883855E-03,
        -1.1232438489069229E-02,
        3.2055243099445879E-02,
        1.1360729895748269E-01,
        1.0838861955003017E-01,
        3.6924643368920851E-01,
        5.3788160700510168E-01,
        3.6924643368920851E-01,
        1.0838861955003017E-01,
        1.1360729895748269E-01,
        3.2055243099445879E-02,
        -1.1232438489069229E-02,
        5.1133174390883855E-03,
        1.0656589772852267E-04,
        1.0802767206624762E-06,
        1.5295717705322357E-09,
    )),
    31 : ((
        -6.3759392709822356E+00,
        -5.6432578578857449E+00,
        -5.0360899444730940E+00,
        -4.4995993983103881E+00,
        -3.6677742159463378E+00,
        -2.9592107790638380E+00,
        -2.5705583765842968E+00,
        -2.2665132620567876E+00,
        -2.0232301911005157E+00,
        -1.8357079751751868E+00,
        -1.5794121348467671E+00,
        -1.2247448713915889E+00,
        -8.7004089535290285E-01,
        -5.2403354748695763E-01,
        -1.7606414208200893E-01,
        0.0000000000000000E+00,
        1.7606414208200893E-01,
        5.2403354748695763E-01,
        8.7004089535290285E-01,
        1.2247448713915889E+00,
        1.5794121348467671E+00,
        1.8357079751751868E+00,
        2.0232301911005157E+00,
        2.2665132620567876E+00,
        2.5705583765842968E+00,
        2.9592107790638380E+00,
        3.6677742159463378E+00,
        4.4995993983103881E+00,
        5.0360899444730940E+00,
        5.6432578578857449E+00,
        6.3759392709822356E+00,
    ), (
        2.2365645607044459E-15,
        -2.6304696458548942E-13,
        9.0675288231679823E-12,
        1.4055252024722478E-09,
        1.0889219692128120E-06,
        1.0541662394746661E-04,
        2.6665159778939428E-05,
        4.8385208205502612E-03,
        -9.8566270434610019E-03,
        2.9409427580350787E-02,
        3.1210210352682834E-03,
        1.0939325071860877E-01,
        1.1594930984853116E-01,
        3.5393889029580544E-01,
        4.9855761893293160E-02,
        4.5888839636756751E-01,
        4.9855761893293160E-02,
        3.5393889029580544E-01,
        1.1594930984853116E-01,
        1.0939325071860877E-01,
        3.1210210352682834E-03,
        2.9409427580350787E-02,
        -9.8566270434610019E-03,
        4.8385208205502612E-03,
        2.6665159778939428E-05,
        1.0541662394746661E-04,
        1.0889219692128120E-06,
        1.4055252024722478E-09,
        9.0675288231679823E-12,
        -2.6304696458548942E-13,
        2.2365645607044459E-15,
    )),
    33 : ((
        -6.3759392709822356E+00,
        -5.6432578578857449E+00,
        -5.0360899444730940E+00,
        -4.4995993983103881E+00,
        -4.0292201405043713E+00,
        -3.6677742159463378E+00,
        -2.9592107790638380E+00,
        -2.5705583765842968E+00,
        -2.2665132620567876E+00,
        -2.0232301911005157E+00,
        -1.8357079751751868E+00,
        -1.5794121348467671E+00,
        -1.2247448713915889E+00,
        -8.7004089535290285E-01,
        -5.2403354748695763E-01,
        -1.7606414208200893E-01,
        0.0000000000000000E+00,
        1.7606414208200893E-01,
        5.2403354748695763E-01,
        8.7004089535290285E-01,
        1.2247448713915889E+00,
        1.5794121348467671E+00,
        1.8357079751751868E+00,
        2.0232301911005157E+00,
        2.2665132620567876E+00,
        2.5705583765842968E+00,
        2.9592107790638380E+00,
        3.6677742159463378E+00,
        4.0292201405043713E+00,
        4.4995993983103881E+00,
        5.0360899444730940E+00,
        5.6432578578857449E+00,
        6.3759392709822356E+00,
    ), (
        -1.7602932805372496E-15,
        4.7219278666417693E-13,
        -3.4281570530349562E-11,
        2.7547825138935901E-09,
        -2.3903343382803510E-08,
        1.2245220967158438E-06,
        9.8710009197409173E-05,
        1.4753204901862772E-04,
        3.7580026604304793E-03,
        -4.9118576123877555E-03,
        2.0435058359107205E-02,
        1.3032872699027960E-02,
        9.6913444944583621E-02,
        1.3726521191567551E-01,
        3.1208656194697448E-01,
        1.8411696047725790E-01,
        2.4656644932829619E-01,
        1.8411696047725790E-01,
        3.1208656194697448E-01,
        1.3726521191567551E-01,
        9.6913444944583621E-02,
        1.3032872699027960E-02,
        2.0435058359107205E-02,
        -4.9118576123877555E-03,
        3.7580026604304793E-03,
        1.4753204901862772E-04,
        9.8710009197409173E-05,
        1.2245220967158438E-06,
        -2.3903343382803510E-08,
        2.7547825138935901E-09,
        -3.4281570530349562E-11,
        4.7219278666417693E-13,
        -1.7602932805372496E-15,
    )),
    35 : ((
        -6.3759392709822356E+00,
        -5.6432578578857449E+00,
        -5.0360899444730940E+00,
        -4.4995993983103881E+00,
        -4.0292201405043713E+00,
        -3.6677742159463378E+00,
        -3.3491639537131945E+00,
        -2.9592107790638380E+00,
        -2.5705583765842968E+00,
        -2.2665132620567876E+00,
        -2.0232301911005157E+00,
        -1.8357079751751868E+00,
        -1.5794121348467671E+00,
        -1.2247448713915889E+00,
        -8.7004089535290285E-01,
        -5.2403354748695763E-01,
        -1.7606414208200893E-01,
        0.0000000000000000E+00,
        1.7606414208200893E-01,
        5.2403354748695763E-01,
        8.7004089535290285E-01,
        1.2247448713915889E+00,
        1.5794121348467671E+00,
        1.8357079751751868E+00,
        2.0232301911005157E+00,
        2.2665132620567876E+00,
        2.5705583765842968E+00,
        2.9592107790638380E+00,
        3.3491639537131945E+00,
        3.6677742159463378E+00,
        4.0292201405043713E+00,
        4.4995993983103881E+00,
        5.0360899444730940E+00,
        5.6432578578857449E+00,
        6.3759392709822356E+00,
    ), (
        1.8684014894510604E-18,
        9.6599466278563243E-15,
        5.4896836948499462E-12,
        8.1553721816916897E-10,
        3.7920222392319532E-08,
        4.3737818040926989E-07,
        4.8462799737020461E-06,
        6.3328620805617891E-05,
        4.8785399304443770E-04,
        1.4515580425155904E-03,
        4.0967527720344047E-03,
        5.5928828911469180E-03,
        2.7780508908535097E-02,
        8.0245518147390893E-02,
        1.6371221555735804E-01,
        2.6244871488784277E-01,
        3.3988595585585218E-01,
        9.1262675363737921E-04,
        3.3988595585585218E-01,
        2.6244871488784277E-01,
        1.6371221555735804E-01,
        8.0245518147390893E-02,
        2.7780508908535097E-02,
        5.5928828911469180E-03,
        4.0967527720344047E-03,
        1.4515580425155904E-03,
        4.8785399304443770E-04,
        6.3328620805617891E-05,
        4.8462799737020461E-06,
        4.3737818040926989E-07,
        3.7920222392319532E-08,
        8.1553721816916897E-10,
        5.4896836948499462E-12,
        9.6599466278563243E-15,
        1.8684014894510604E-18,
    )),
}

if __name__ == "__main__":
    import doctest
    doctest.testmod()
