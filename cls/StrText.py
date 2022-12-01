#!/usr/bin/env python3

class StrText():

    # Base64加密文本转换为标准格式
    def get_str_base64(origStr):
        missing_padding = 4 - len(origStr) % 4 
        if missing_padding: 
            origStr += '=' * missing_padding
        return origStr

    # 从字符中取两不同字符串中间的字符，print(sub_link)，参数：文本，第一字符串，第二字符串，是否保留字符串
    def get_str_btw(s, f, b, y):
        par = s.partition(f)
        if(y == 0):
            return (par[2].partition(b))[0][:]
        else:
            return f + '' + (par[2].partition(b))[0][:] + '' + b

    #检验是否全是中文字符
    def is_all_chinese(strs):
        for _char in strs:
            if not '\u4e00' <= _char <= '\u9fa5':
                return False
        return True

    #检验是否含有中文字符
    def is_contains_chinese(strs):
        for _char in strs:
            if '\u4e00' <= _char <= '\u9fa5':
                return True
        return False
