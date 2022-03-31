def create_response_skeleton(long_url, short_url):
    response = {"url": long_url, "link": short_url}
    return response


def generate_response(bitly_response_ettr, tiny_response_attr, response_obj):
    if bitly_response_ettr in response_obj:
        long_url = response_obj["long_url"]
        short_url = response_obj["link"]
        return create_response_skeleton(long_url, short_url)
    elif tiny_response_attr in response_obj:
        long_url = response_obj["data"]["url"]
        short_url = response_obj["data"]["tiny_url"]
        return create_response_skeleton(long_url, short_url)
    else:
        return {"Empty Response"}
