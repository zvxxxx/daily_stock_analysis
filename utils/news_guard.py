from datetime import datetime, timedelta

MIN_NEWS_COUNT = 2
MAX_DAYS_OLD = 7

def validate_news(news_items: list):
    """
    校验新闻是否可信、是否够新
    """
    if not news_items or len(news_items) < MIN_NEWS_COUNT:
        return False, "暂无可靠新闻源，已禁用AI基本面编造"

    valid_news = []
    now = datetime.now()

    for item in news_items:
        try:
            publish_time = datetime.fromisoformat(item.get("date", ""))
            if now - publish_time <= timedelta(days=MAX_DAYS_OLD):
                valid_news.append(item)
        except:
            continue

    if len(valid_news) < MIN_NEWS_COUNT:
        return False, "新闻过旧，已禁用AI基本面编造"

    return True, valid_news
