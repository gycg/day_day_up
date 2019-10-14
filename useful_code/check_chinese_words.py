# 判断是否含有非中文，有则返回True
def check(cstr):
    for ch in cstr:
        if ch < '\u4e00' or ch > '\u9fa5':
            return True
    return False

# 判断是否含有中文，有则返回True
def check(cstr):
    for ch in cstr:
        if ch > '\u4e00' and ch < '\u9fa5':
            return True
    return False

def check(ch):
    punct = """abcdefghijklmnopqrstuvwxyz0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､\u3000、〃〈〉《》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏﹑﹔·！？｡。"""
    if ch > '\u4e00' and ch < '\u9fa5' or ch in punct:
        return True
    return False

a = '#今日贴纸打卡##健康饮食打卡# 今天晚上步行后，吃的有点多，有点辣，明天注意⚠️，把喜欢的壁纸收藏一下！都是萌萌哒！听说明天还是继续阴雨天☔，打算一天做面包🍞蛋糕🍰'
emoji_pattern = re.compile('[\U00010000-\U0010ffff]|[\u2600-\u2B55]|\ufe0f')
emoji_pattern.findall(a)
