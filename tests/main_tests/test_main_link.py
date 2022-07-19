from main import link


def test_link_output():
    url = "https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists"
    label = "Removing duplicates in lists"
    format_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'
    assert link(url, label) == format_mask.format('', url, label)
    assert link(url) == format_mask.format('', url, url)
