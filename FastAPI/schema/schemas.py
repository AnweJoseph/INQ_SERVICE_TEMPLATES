def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "cct_id": str(todo["cct_id"]),
        "client_vrf": str(todo["client_vrf"]),
        "rd": str(todo["rd"]),
        "rt_export": str(todo["rt_export"]),
        "rt_import": str(todo["rt_import"])
    }


def list_serial(todos) -> list:
    return [individual_serial(todo) for todo in todos]
