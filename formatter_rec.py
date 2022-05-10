def formatter(rec):
    result = rec.split()
    result.pop(0)
    rec = ' '.join(result)
    return rec