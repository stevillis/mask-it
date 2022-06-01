from typing import Union


class MaskIt:
    """Apply a mask to a given input based on given pattern."""

    def __init__(self, value: str, pattern: str):
        self.PATTERN_SIGN = '#'
        self.value = value
        self.pattern = pattern

    def _count_octothorpe(self) -> int:
        """Count occurrencies of # in given pattern."""
        count = 0
        for v in self.pattern:
            if v == self.PATTERN_SIGN:
                count += 1
        return count

    def mask(self) -> Union[str, ValueError]:
        """
        Apply a mask to value based on given pattern.

        Arguments:
        value: the input value

        pattern: the pattern of mask. Ex.: ###.###.###-##.
        Every '#' in the pattern will replace by input value items.

        Returns: The masked value based on given pattern. 
        """
        len_octothorpe = self._count_octothorpe()
        len_value = len(self.value)
        value_list = list(self.value)

        if len_value != len_octothorpe:
            raise ValueError(
                f'{self.value} size not compatible with # occurrencies in pattern. '
                f'{len_value} != {len_octothorpe}'
            )

        result = ''
        for p in self.pattern:
            if p == self.PATTERN_SIGN:
                result += value_list.pop(0)
            else:
                result += p

        return result
