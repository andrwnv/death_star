from attr import dataclass


class Config:
    @dataclass
    class SelfProps:
        grpc_addr: str
        grpc_port: str

        event_queue_addr: str
        event_queue_port: str

    @dataclass
    class ScenaristeProps:
        event_queue_addr: str
        event_queue_port: str

    def __init__(self) -> None:
        self.self_props = Config.SelfProps(
            grpc_addr="0.0.0.0",
            grpc_port=4040,
            event_queue_addr="0.0.0.0",
            event_queue_port=5560,
        )
        self.scenariste_props = Config.ScenaristeProps(
            event_queue_addr="0.0.0.0",
            event_queue_port=5560,
        )

    def init_with_file(self, file: str):
        import yaml

        with open(file, "r") as file:
            cfg = yaml.safe_load(file)

            self.self_props.grpc_addr = cfg["grpc_addr"]
            self.self_props.grpc_port = cfg["grpc_port"]
            self.self_props.event_queue_addr = cfg["event_queue_addr"]
            self.self_props.event_queue_port = cfg["event_queue_port"]

            self.scenariste_props.event_queue_addr = cfg["scenariste"][
                "event_queue_addr"
            ]
            self.scenariste_props.event_queue_port = cfg["scenariste"][
                "event_queue_port"
            ]
