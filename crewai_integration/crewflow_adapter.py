# Adapter to interface CrewAI agents with InfraFlow
def format_crew_task(input_data):
    return {
        "agent_id": input_data.get("id"),
        "instructions": input_data.get("prompt"),
        "priority": input_data.get("priority", "normal")
    }

def dispatch_to_mesh(formatted_task):
    print("[CrewAI Adapter] Dispatching to InfraFlow Mesh:", formatted_task)

# Example test
if __name__ == "__main__":
    test = format_crew_task({"id": "c1", "prompt": "Check mesh health."})
    dispatch_to_mesh(test)
