"""
Integrates the computes together
"""
from typing import Any, Dict, Optional, Union

from qcelemental.models import FailedOperation, ResultInput

from .config import get_config
from .exceptions import InputError, RandomError
from .procedures import get_procedure
from .programs import get_program
from .util import compute_wrapper, handle_output_metadata, model_wrapper

__all__ = ["compute", "compute_procedure"]


def _process_failure_and_return(model, return_dict, raise_error):
    if isinstance(model, FailedOperation):
        if raise_error:
            raise InputError(model.error.error_message)
        elif return_dict:
            return model.dict()
        else:
            return model
    else:
        return False


def compute(input_data: Union[Dict[str, Any], 'ResultInput'],
            program: str,
            raise_error: bool = False,
            local_options: Optional[Dict[str, Any]] = None,
            return_dict: bool = False) -> 'Result':
    """Executes a single quantum chemistry program given a QC Schema input.

    The full specification can be found at:
        http://molssi-qc-schema.readthedocs.io/en/latest/index.html#

    Parameters
    ----------
    input_data : Union[Dict[str, Any], 'ResultInput']
        A QCSchema input specification in dictionary or model from QCElemental.models
    program : str
        The program to execute the input with.
    raise_error : bool, optional
        Determines if compute should raise an error or not.
    retries : int, optional
        The number of random tries to retry for.
    local_options : Optional[Dict[str, Any]], optional
        A dictionary of local configuration options
    return_dict : bool, optional
        Returns a dict instead of qcelemental.models.ResultInput

    Returns
    -------
    Result
        A computed Result object.
    """

    output_data = input_data.copy()  # lgtm [py/multiple-definition]
    with compute_wrapper(capture_output=False, raise_error=raise_error) as metadata:

        # Grab the executor and build the input model
        executor = get_program(program)

        # Build the model and validate
        input_data = model_wrapper(input_data, ResultInput)

        # Build out local options
        if local_options is None:
            local_options = {}

        input_engine_options = input_data.extras.pop("_qcengine_local_config", {})

        local_options = {**local_options, **input_engine_options}
        config = get_config(local_options=local_options)

        for x in range(config.retries + 1):
            try:
                output_data = executor.compute(input_data, config)
                break
            except RandomError as e:

                if x == config.retries:
                    raise e
                else:
                    metadata["retries"] += 1
            except:
                raise


    return handle_output_metadata(output_data, metadata, raise_error=raise_error, return_dict=return_dict)


def compute_procedure(input_data: Union[Dict[str, Any], 'BaseModel'],
                      procedure: str,
                      raise_error: bool = False,
                      local_options: Optional[Dict[str, str]] = None,
                      return_dict: bool = False) -> 'BaseModel':
    """Runs a procedure (a collection of the quantum chemistry executions)

    Parameters
    ----------
    input_data : dict or qcelemental.models.OptimizationInput
        A JSON input specific to the procedure executed in dictionary or model from QCElemental.models
    procedure : {"geometric"}
        The name of the procedure to run
    raise_error : bool, option
        Determines if compute should raise an error or not.
    local_options : dict, optional
        A dictionary of local configuration options
    return_dict : bool, optional, default True
        Returns a dict instead of qcelemental.models.ResultInput

    Returns
    ------
    dict, Optimization, FailedOperation
        A QC Schema representation of the requested output, type depends on return_dict key.
    """

    output_data = input_data.copy()  # lgtm [py/multiple-definition]
    with compute_wrapper(capture_output=False, raise_error=raise_error) as metadata:

        # Grab the executor and build the input model
        executor = get_procedure(procedure)

        config = get_config(local_options=local_options)
        input_data = executor.build_input_model(input_data)

        # Create a base output data in case of errors
        output_data = input_data.copy()  # lgtm [py/multiple-definition]
        output_data = executor.compute(input_data, config)

    return handle_output_metadata(output_data, metadata, raise_error=raise_error, return_dict=return_dict)
