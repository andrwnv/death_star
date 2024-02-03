import asyncio

from service.config import Config
from service import run


SUB_SERVICE_INFO = "Death-Star: Energy unit service (v1.0.0)"

SERVICE_INFO = f"""
    ______                                  __  __      _ __
   / ____/___  ___  _________ ___  __      / / / /___  (_) /_
  / __/ / __ \/ _ \/ ___/ __ `/ / / /_____/ / / / __ \/ / __/
 / /___/ / / /  __/ /  / /_/ / /_/ /_____/ /_/ / / / / / /_
/_____/_/ /_/\___/_/   \__, /\__, /      \____/_/ /_/_/\__/
                      /____//____/

{SUB_SERVICE_INFO}
"""


if __name__ == "__main__":

    def __parse_args():
        import argparse

        parser = argparse.ArgumentParser(SUB_SERVICE_INFO)

        parser.add_argument(
            "-c", "--config", nargs="?", type=str, help="Filepath to config file."
        )

        parser.add_argument(
            "-gaddr",
            "--grpc_addr",
            nargs="?",
            type=str,
            help="Address of self grpc server.",
        )
        parser.add_argument(
            "-gport",
            "--grpc_port",
            nargs="?",
            type=int,
            help="Port of self grpc server.",
        )

        parser.add_argument(
            "-qaddr",
            "--rmq_addr",
            nargs="?",
            type=str,
            help="Address of self event queue.",
        )
        parser.add_argument(
            "-qport",
            "--rmq_port",
            nargs="?",
            type=int,
            help="Port of self event queue.",
        )

        parser.add_argument(
            "-sqaddr",
            "--scenariste_rmq_addr",
            type=str,
            nargs="?",
            help="Address of 'scenariste' event queue.",
        )
        parser.add_argument(
            "-sqport",
            "--scenariste_rmq_port",
            type=int,
            nargs="?",
            help="Port of 'scenariste' event queue.",
        )

        return parser.parse_args()

    args = __parse_args()

    print(SERVICE_INFO)

    cfg = Config()
    if args.config is not None:
        cfg.init_with_file(args.config)
    else:
        if (
            args.grpc_addr is None
            or args.grpc_port is None
            or args.rmq_addr is None
            or args.rmq_port is None
            or args.scenariste_rmq_addr is None
            or args.scenariste_rmq_port is None
        ):

            print(
                "Failed to start service! Config file doesn't set and manual configuration miss matched!"
            )

            exit(-1)

        cfg.self_props.grpc_addr = args.grpc_addr
        cfg.self_props.grpc_port = args.grpc_port

        cfg.self_props.event_queue_addr = args.rmq_addr
        cfg.self_props.event_queue_port = args.rmq_port

        cfg.scenariste_props.event_queue_addr = args.scenariste_rmq_addr
        cfg.scenariste_props.event_queue_port = args.scenariste_rmq_port

    asyncio.run(run(cfg))
