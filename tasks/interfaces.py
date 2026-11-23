from typing import List


def parse_interfaces(output: str) -> List[dict]:
    result = []
    if not output:
        return result
    for line in output.strip().splitlines()[1:]:
        try:
            name, ip, status, protocol = line.split()
            result.append({
                "name": name,
                "ip": ip if ip != "unassigned" else None,
                "status": status,
                "protocol": protocol
            })
        except Exception as e:
            print(f"Unpacking failed: line is '{line}'")

    return result
