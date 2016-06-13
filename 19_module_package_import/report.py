

def get_description():
    """ランダムに天気を返す"""
    from random import choice
    weathers = ["rain", "snow", "sleet", "fog", "sun", "who knows"]
    return choice(weathers)

def get_poor_description():
    """常に役立たない情報を返す"""
    return "Sorry, I don't know ..."
