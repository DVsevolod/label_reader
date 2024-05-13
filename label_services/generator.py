from random import choice

from enums import Meta, Length, MetaKeys

class LabelGenerator:
    __meta = Meta
    length = Length
    keys = MetaKeys

    def generate_randomly(self, length):
        if length not in [self.length.stand_by.value, self.length.departed.value]:
            raise ValueError(f"Wrong Length value! length={length}")

        label = ''

        storage = [
            key for key, value in self.__meta.storage.value.items()
        ]
        status = [
            key for key, value in self.__meta.status.value.items()
        ]
        state = [
            key for key, value in self.__meta.state.value.items()
        ]
        loaded = [
            key for key, value in self.__meta.loaded.value.items()
        ]
        departed = [
            key for key, value in self.__meta.departed.value.items()
        ]

        params = [
            storage, status, state, loaded, departed
        ]

        for param in params[:length]:
            label += choice(param)

        return label

    def generate(self):

        storage = [
            key for key, value in self.__meta.storage.value.items()
        ]
        storage = choice(storage)

        status = [
            key for key, value in self.__meta.status.value.items()
        ]
        status = choice(status)

        if status == self.keys.NOT_READY.value:
            state = [
                key for key, value in self.__meta.state.value.items() if key != self.keys.OK.value
            ]
            state = choice(state)
        else:
            state = self.keys.OK.value

        if status != self.keys.READY.value:
            return "".join([storage, status, state])

        elif status == self.keys.READY.value and state == self.keys.OK.value:
            loaded = self.keys.YES.value
        else:
            loaded = self.keys.NO.value

        if loaded == self.keys.YES.value:
            departed = [
                key for key, value in self.__meta.departed.value.items()
            ]
            departed = choice(departed)
        else:
            departed = self.keys.NO.value

        params = [
            storage, status, state, loaded, departed
        ]

        return "".join(params)
