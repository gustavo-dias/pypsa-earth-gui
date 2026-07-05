"""App's home view entry.

Functions
---------
main() -> None
"""

import streamlit as st


def main() -> None:
    """Entry point for the home view.
    
    Returns
    -------
    None
    """
    st.write(
        "Welcome to PyPSA-Earth's app. To use it: \n" \
        "1) Create a configuration;\n" \
        "2) Solve it;\n" \
        "3) Visualize the results. \n\n" \
        "Use the sidebar menu to the left to navigate.\n\n\n" \
        "Start-off by selecting the directory where PyPSA-Earth is installed "
        "in the (local) machine."
    )


if __name__ == '__main__':
    main()