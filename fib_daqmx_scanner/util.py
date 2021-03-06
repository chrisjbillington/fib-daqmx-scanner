import numpy as np

def scientific_notation(x, sigfigs=4, mode='eng'):
    """Returns a unicode string of the float f in scientific notation"""

    times = u'\u00d7'
    thinspace = u'\u2009'
    hairspace = u'\u200a'
    sups = {u'-': u'\u207b',
            u'0': u'\u2070',
            u'1': u'\xb9',
            u'2': u'\xb2',
            u'3': u'\xb3',
            u'4': u'\u2074',
            u'5': u'\u2075',
            u'6': u'\u2076',
            u'7': u'\u2077',
            u'8': u'\u2078',
            u'9': u'\u2079'}

    prefixes = {
        -24: u"y",
        -21: u"z",
        -18: u"a",
        -15: u"f",
        -12: u"p",
        -9: u"n",
        -6: u"\u03bc",
        -3: u"m",
        0: u"",
        3: u"k",
        6: u"M",
        9: u"G",
        12: u"T",
        15: u"P",
        18: u"E",
        21: u"Z",
        24: u"Y"
    }

    if not isinstance(x, float):
        raise TypeError('x must be floating point number')
    if np.isnan(x) or np.isinf(x):
        return str(x)
    if x != 0:
        exponent = int(np.floor(np.log10(np.abs(x))))
        # Only multiples of 10^3
        exponent = int(np.floor(exponent / 3) * 3)
    else:
        exponent = 0

    significand = x / 10 ** exponent
    pre_decimal, post_decimal = divmod(significand, 1)
    digits = sigfigs - len(str(int(pre_decimal)))
    significand = round(significand, digits)
    result = str(significand)
    if exponent:
        if mode == 'exponential':
            superscript = ''.join(sups.get(char, char) for char in str(exponent))
            result += thinspace + times + thinspace + '10' + superscript
        elif mode == 'eng':
            try:
                # If our number has an SI prefix then use it
                prefix = prefixes[exponent]
                result += hairspace + prefix
            except KeyError:
                # Otherwise display in scientific notation
                superscript = ''.join(sups.get(char, char) for char in str(exponent))
                result += thinspace + times + thinspace + '10' + superscript
    return result
