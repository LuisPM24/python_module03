import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    names = ["Bob", "Dylan", "Alice", "Charlie"]
    actions = [
        "run",
        "eat",
        "sleep",
        "move",
        "grab",
        "climb",
        "swim",
        "release"
    ]
    while 1:
        yield (random.choice(names), random.choice(actions))


def consume_event(events_list: list[tuple[str, str]]
                  ) -> typing.Generator[tuple[str, str], None, None]:
    while events_list:
        index = random.randrange(len(events_list))
        yield events_list.pop(index)


def main() -> None:
    event_generator = gen_event()
    for count in range(1000):
        event = next(event_generator)
        print(f"Event {count}: Player {event[0]} did action {event[1]}")
    new_events = []
    for count in range(10):
        new_events.append(next(event_generator))
    print(f"Built list of {len(new_events)} events: {new_events}")
    for selected_event in consume_event(new_events):
        print(f"Got event from list: {selected_event}")
        print(f"Remains in list: {new_events}")


if __name__ == "__main__":
    main()
