from main import generate_summary_for_stream_count


def test_summary_statistics_for_stream_count():
    median, max, min = generate_summary_for_stream_count()
    assert median == 290530915.0
    assert max == 3703895074.0
    assert min == 2762.0


if __name__ == "__main__":
    test_summary_statistics_for_stream_count()
