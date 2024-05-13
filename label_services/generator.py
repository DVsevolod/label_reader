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

        storage = list(self.__meta.storage.value.keys())
        status = list(self.__meta.status.value.keys())
        state = list(self.__meta.state.value.keys())
        loaded = list(self.__meta.loaded.value.keys())
        departed = list(self.__meta.departed.value.keys())

        params = [
            storage, status, state, loaded, departed
        ]

        for param in params[:length]:
            label += choice(param)

        return label

    def generate(self):
        storage = choice(list(self.__meta.storage.value.keys()))
        status = choice(list(self.__meta.status.value.keys()))

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
            departed = choice(list(self.__meta.departed.value.keys()))
        else:
            departed = self.keys.NO.value

        params = [
            storage, status, state, loaded, departed
        ]

        return "".join(params)
