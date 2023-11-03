def individual_serial(todo) -> dict:
    return {
            "id": str(todo["_id"]),
            "client_vrf": todo["client_vrf"],
	    	"rd": todo["rd"],
	    	"rt_export": todo["rt_export"],
	    	"rt_import": todo["rt_import"]
            }

def list_serial(todos) -> list:
    return [individual_serial(todo) for todo in todos]
