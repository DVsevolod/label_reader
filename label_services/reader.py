from enums import Meta, LabelIndex


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
            loaded = self.__meta.loaded.value.get(LabelIndex.loaded.value)
            departed = self.__meta.departed.value.get(LabelIndex.departed.value)

            result += f"""Loaded: {loaded}
Departed: {departed}"""

        return result
