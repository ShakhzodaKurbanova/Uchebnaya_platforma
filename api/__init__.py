def result_message(result):
    print(result)
    if result:
        return {"status": 1, "message": result}
    return {"status": 0, "message": False}