"""App's configuration parameters.

Classes
-------
Parameter()
"""

from __future__ import annotations

from typing import Any


class Parameter():
    """Class that represents PyPSA-Earth configuration parameters."""

    _unique_id_delimiter: str = '__'
    _default_unique_id_prefix: str = 'defaultuniqueidprefix'

    def __init__(
            self,
            name: str,
            value: Any,
            unique_id_prefix: str | None = None,
            ancestors: list[str] = [],
        ) -> None:
        """Initialize a PyPSA-Earth parameter object.
        
        Parameters
        ----------
        name: str
            A string representing the parameter's name.
        value: Any
            The value of the parameter.
        unique_id_prefix: str
            A prefix to append in the parameter unique id.
        ancestors: list[str]
            The list of names of parameter's ancestors in the configuration
            structure.
        """
        self.name: str = name
        self.hierarchy: list = ancestors + [name]
        self.value = value
        self._widget_metadata: dict = {}
        if (unique_id_prefix is None) or (unique_id_prefix == ''):
            self.unique_id_prefix = self._default_unique_id_prefix
        else:
            self.unique_id_prefix = unique_id_prefix

    @property
    def value(self) -> Any:
        """Get/set the parameter's value.
        
        Parameters
        ----------
        value: Any
            The value associated with the parameter.

        Returns
        -------
        Any
            The value of the parameter.     
        """
        return self._value
    
    @value.setter
    def value(self, value: Any) -> None:
        """"""
        self._value = value

    @property
    def widget_metadata(self) -> dict:
        """Get/set the parameter's widget metadata.
        
        Parameters
        ----------
        value: dict
            The dictionary containig the parameter's ui widget metadata.
        
        Returns
        -------
        dict
            A dictionary containing the parameter's ui widget metadata.
        
        Raises
        ------
        TypeError:
            If value is not a dict.
        """
        return self._widget_metadata
    
    @widget_metadata.setter
    def widget_metadata(self, value: dict) -> None:
        """"""
        if not isinstance(value, dict):
            raise TypeError(
                "Parameter.widget_metadata: expected value to be a dict, got "
                f"a(n) {type(value).__name__}."
            )
        self._widget_metadata = value

    @property
    def unique_id(self) -> str:
        """Get the parameter's unique id.
        
        Format:
           'unique_id_prefix__ancestor1name__...__ancestorNname__parametername'
        
        Returns
        -------
        str
            The string representation of the parameter's unique identifier.
        """
        # some parameters have integer names (e.g. co2_budget/year/2020), need
        # to convert to string to generate the unique id as a str otherwise
        # TypeError
        base_id: str = self._unique_id_delimiter.join(
            [str(entry) for entry in self.hierarchy]
        )
        return self.unique_id_prefix + self._unique_id_delimiter + base_id


    @property
    def label(self) -> str:
        """Get the parameter's label.
        
        The label is the parameter's name capitalized.

        Returns
        -------
        str
            The parameter's label.
        """
        return str(self.name).capitalize()

    def __str__(self) -> str:
        """The string representation of the parameter.
        
        Format: 'name: value'.

        Returns
        -------
        str
            A string representation of the parameter.
        """
        return f"{self.name}: {self.value}"
    
    def remove_from_hierarchy(self, idx: int) -> None:
        """Remove the entry at position idx in the hierarchy.
        
        Parameters
        ----------
        idx: int
            The index of the item to be removed from the hierarchy.
        
        Returns
        -------
        None
        """
        self.hierarchy.pop(idx)
    
    @classmethod
    def get_parameter_from_unique_id(
            cls,
            unique_id: str,
            value: Any,
        ) -> Parameter:
        """Get a PyPSA-Earth parameter object buit from unique_id and value.
        
        Parameters
        ----------
        unique_id: str
            A string representing the parameter's unique identifier. See the
            documentation of Parameter.unique_id for the expected format.
        value: Any
            The value associated with the returned parameter.
        
        Returns
        -------
        Parameter
            A parameter object with unique_id and value.
        """
        hierarchy_list = unique_id.split(cls._unique_id_delimiter)
        return Parameter(
            hierarchy_list.pop(-1), # remove parameter's name
            value,
            hierarchy_list.pop(0),  # remove parameter's unique_id_prefix
            hierarchy_list,         # what remains is the list of ancestors
        )
