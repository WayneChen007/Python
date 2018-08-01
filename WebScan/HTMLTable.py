class DictMath(object):
    def __init__(self, json):
        self.json = json

    @property
    def keys_list(self):
        return [k for k in self.json]

    @property
    def _value_list(self):
        _l = []
        for k in self.keys_list:
            w = self.json.get(k)
            _l.append(w)
        return _l

    @staticmethod
    def _list_length(seq):
        return len(seq)

    def max_list(self):
        __l = self._value_list.copy()
        __l.sort(key=self._list_length, reverse=True)
        return __l[0]


class HTMLColor(object):
    LightPink = '#FFB6C1'
    Pink = '#FFC0CB'
    Crimson = '#DC143C'
    LavenderBlush = '#FFF0F5'
    PaleVioletRed = '#DB7093'
    HotPink = '#FF69B4'
    DeepPink = '#FF1493'
    MediumVioletRed = '#C71585'
    Orchid = '#DA70D6'
    Thistle = '#D8BFD8'
    plum = '#DDA0DD'
    Violet = '#EE82EE'
    Magenta = '#FF00FF'
    Fuchsia = '#FF00FF'
    DarkMagenta = '#8B008B'
    Purple = '#800080'
    MediumOrchid = '#BA55D3'
    DarkVoilet = '#9400D3'
    DarkOrchid = '#9932CC'
    Indigo = '#4B0082'
    BlueViolet = '#8A2BE2'
    MediumPurple = '#9370DB'
    MediumSlateBlue = '#7B68EE'
    SlateBlue = '#6A5ACD'
    DarkSlateBlue = '#483D8B'
    Lavender = '#E6E6FA'
    GhostWhite = '#F8F8FF'
    Blue = '#0000FF'
    MediumBlue = '#0000CD'
    MidnightBlue = '#191970'
    DarkBlue = '#00008B'
    Navy = '#000080'
    RoyalBlue = '#4169E1'
    CornflowerBlue = '#6495ED'
    LightSteelBlue = '#B0C4DE'
    LightSlateGray = '#778899'
    SlateGray = '#708090'
    DoderBlue = '#1E90FF'
    AliceBlue = '#F0F8FF'
    SteelBlue = '#4682B4'
    LightSkyBlue = '#87CEFA'
    SkyBlue = '#87CEEB'
    DeepSkyBlue = '#00BFFF'
    LightBLue = '#ADD8E6'
    PowDerBlue = '#B0E0E6'
    CadetBlue = '#5F9EA0'
    Azure = '#F0FFFF'
    LightCyan = '#E1FFFF'
    PaleTurquoise = '#AFEEEE'
    Cyan = '#00FFFF'
    Aqua = '#00FFFF'
    DarkTurquoise = '#00CED1'
    DarkSlateGray = '#2F4F4F'
    DarkCyan = '#008B8B'
    Teal = '#008080'
    MediumTurquoise = '#48D1CC'
    LightSeaGreen = '#20B2AA'
    Turquoise = '#40E0D0'
    Auqamarin = '#7FFFAA'
    MediumAquamarine = '#00FA9A'
    MediumSpringGreen = '#00FF7F'
    MintCream = '#F5FFFA'
    SpringGreen = '#3CB371'
    SeaGreen = '#2E8B57'
    Honeydew = '#F0FFF0'
    LightGreen = '#90EE90'
    PaleGreen = '#98FB98'
    DarkSeaGreen = '#8FBC8F'
    LimeGreen = '#32CD32'
    Lime = '#00FF00'
    ForestGreen = '#228B22'
    Green = '#008000'
    DarkGreen = '#006400'
    Chartreuse = '#7FFF00'
    LawnGreen = '#7CFC00'
    GreenYellow = '#ADFF2F'
    OliveDrab = '#556B2F'
    Beige = '#F5F5DC'
    LightGoldenrodYellow = '#FAFAD2'
    Ivory = '#FFFFF0'
    LightYellow = '#FFFFE0'
    Yellow = '#FFFF00'
    Olive = '#808000'
    DarkKhaki = '#BDB76B'
    LemonChiffon = '#FFFACD'
    PaleGodenrod = '#EEE8AA'
    Khaki = '#F0E68C'
    Gold = '#FFD700'
    Cornislk = '#FFF8DC'
    GoldEnrod = '#DAA520'
    FloralWhite = '#FFFAF0'
    OldLace = '#FDF5E6'
    Wheat = '#F5DEB3'
    Moccasin = '#FFE4B5'
    Orange = '#FFA500'
    PapayaWhip = '#FFEFD5'
    BlanchedAlmond = '#FFEBCD'
    NavajoWhite = '#FFDEAD'
    AntiqueWhite = '#FAEBD7'
    Tan = '#D2B48C'
    BrulyWood = '#DEB887'
    Bisque = '#FFE4C4'
    DarkOrange = '#FF8C00'
    Linen = '#FAF0E6'
    Peru = '#CD853F'
    PeachPuff = '#FFDAB9'
    SandyBrown = '#F4A460'
    Chocolate = '#D2691E'
    SaddleBrown = '#8B4513'
    SeaShell = '#FFF5EE'
    Sienna = '#A0522D'
    LightSalmon = '#FFA07A'
    Coral = '#FF7F50'
    OrangeRed = '#FF4500'
    DarkSalmon = '#E9967A'
    Tomato = '#FF6347'
    MistyRose = '#FFE4E1'
    Salmon = '#FA8072'
    Snow = '#FFFAFA'
    LightCoral = '#F08080'
    RosyBrown = '#BC8F8F'
    IndianRed = '#CD5C5C'
    Red = '#FF0000'
    Brown = '#A52A2A'
    FireBrick = '#B22222'
    DarkRed = '#8B0000'
    Maroon = '#800000'
    White = '#FFFFFF'
    WhiteSmoke = '#F5F5F5'
    Gainsboro = '#DCDCDC'
    LightGrey = '#D3D3D3'
    Silver = '#C0C0C0'
    DarkGray = '#A9A9A9'
    Gray = '#808080'
    DimGray = '#696969'
    Black = '#000000'


class HtmlTable(object):
    title_color = HTMLColor.OrangeRed
    title_size = 15
    title_margin = 7.5
    header_height = 30
    header_bgcolor = HTMLColor.LightSkyBlue
    header_font_size = "medium"
    table_width = 720
    table_height = 20
    table_align = "left"
    table_bgcolor = HTMLColor.Azure
    left_header_width = 50

    def __init__(self, title):
        self.title = title
        self.__by_col = TableByColumn
        self.__by_row = TableByRow

    @property
    def global_style(self):
        return """padding: 1px; border: 1px solid #666;"""

    @property
    def title_tag(self):
        return """<p class="MsoNormal" align="center" style="text-align:center;line-height:15.0pt;vertical-align:middle;margin-top:%s">
        <b><span style="font-family: 'fae 8f6f 96c5 9ed1', 'sans-serif'; font-size: %s; color: %s">%s<span lang="EN-US"><u></u><u></u></span></span></b>
        </p>""" % (str(self.title_margin), str(self.title_size), self.title_color, self.title)

    @property
    def header_tag(self):
        return """<th style="%s; %s" height="%.2fpx" bgColor=%s>%s</th>
        """ % ('%s', self.global_style, self.header_height, self.header_bgcolor, '%s')

    @property
    def table_tag(self):
        return """<table style="width:%.2fpx; table-layout:fixed; border-collapse: collapse; %s word-break: break-all;" cellspacing="0" cellpadding="0">""" % (self.table_width, self.global_style)

    @property
    def row_tag(self):
        return """<tr style="height:%.2fpt; %s" bgColor=%s align="%s">
                    %s
                    </tr>""" % (self.table_height, self.global_style, self.table_bgcolor, self.table_align, '%s')

    def set_title_style(self, font_size=title_size, font_color=title_color):
        self.title_size = font_size
        self.title_color = font_color
        self.title_margin = self.title_size / 2

    def set_header_style(self, height=header_height, bg_color=header_bgcolor):
        self.header_height = height
        self.header_bgcolor = bg_color

    def set_table_style(self, width=table_width, height=table_height, bg_color=table_bgcolor, align=table_align):
        self.table_width = width
        self.table_height = height
        self.table_bgcolor = bg_color
        self.table_align = align

    def _table(self, header_tag, body_tag):
        _table = """
    <div align="center">
        %s
    %s
        <tbody>
            <tr>
                %s
                </tr>
                %s
            </tbody>
        </table>
    </div>"""
        return _table % (self.title_tag, self.table_tag, header_tag, body_tag)

    def add_left_headers(self, left_headers, width):
        self.__by_col._left_headers_switch = {'left_headers': left_headers, 'width': width}

    def table_by_column(self, data, diff_width=None):
        __by_col = self.__by_col(data)
        headers_tag = __by_col.headers_tags(self.header_tag, diff_width)
        return self._table(headers_tag, __by_col.table_body(self.row_tag))

    def table_by_row(self, data):
        __by_row = self.__by_row(data)
        return self._table('', __by_row.test(self.row_tag))


class TableByColumn(DictMath):
    _left_headers_switch = None

    def __init__(self, data):
        super(TableByColumn, self).__init__(data)
        self.data = data
        self.headers = self.keys_list
        if self._left_headers_switch is not None:
            self.lh = self._left_headers_switch.get('left_headers')
            self.lhw = self._left_headers_switch.get('width')

    def headers_tags(self, html_header, diff_width):
        header_tag_list = ''
        if self._left_headers_switch is not None:
            self.headers.insert(0, '')
        for _h in self.headers:
            if diff_width and _h in diff_width:
                width = 'width:%spx' % str(diff_width.get(_h))
            elif _h == '':
                width = 'width:%spx' % str(self.lhw)
            else:
                width = ''
            header_tag_list += (html_header % (width, _h))
        return header_tag_list

    @staticmethod
    def _row_tags(data_list, html_body):
        cells = ''
        for d in data_list:
            cells += """\t<td style="padding: 1px; border: 1px solid #666;"> %s</td>
                    """ % d
        tags = html_body % cells
        return tags

    def _row_by_index(self, index, html_body):
        data_list = []
        for header in self.keys_list:
            col_list = self.data.get(header)
            try:
                data_by_header = col_list[index]
            except IndexError:
                data_by_header = ''
            data_list.append(data_by_header)
        if self._left_headers_switch:
            lh = self.lh[index] if len(self.lh) > index else ''
            data_list.insert(0, lh)
        return self._row_tags(data_list, html_body)

    def table_body(self, html_body):
        tags = ''
        for i in range(0, len(self.max_list())):
            row = self._row_by_index(i, html_body)
            tags += row
        return tags


class TableByRow(DictMath):
    def __init__(self, data):
        super(TableByRow, self).__init__(data)
        self.data = data
        self.headers = self.keys_list

    @staticmethod
    def _row_tags(data_list, html_body):
        cells = ''
        for d in data_list:
            cells += "\t<td>%s</td>" % d
        tags = html_body % cells
        return tags

    def test(self, html_body):
        data_list = self._value_list
        print(data_list)
        return self._row_tags(self._value_list[0], html_body)
