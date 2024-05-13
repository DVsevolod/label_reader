from enums import Meta


class LabelReader:
    __meta = Meta

    def read(self, label):
        storage = self.__meta.storage.value.get(label[0])
        status = self.__meta.status.value.get(label[1])
        state = self.__meta.state.value.get(label[2])

        result = f"""Storage: {storage}
Status: {status}
State: {state}
"""

        if len(label) == 5:
            loaded = self.__meta.loaded.value.get(label[3])
            departed = self.__meta.departed.value.get(label[4])

            result += f"""Loaded: {loaded}
Departed: {departed}"""

        return result
