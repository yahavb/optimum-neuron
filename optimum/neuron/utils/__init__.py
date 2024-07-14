# coding=utf-8
# Copyright 2023 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import TYPE_CHECKING

from transformers.utils import _LazyModule


_import_structure = {
    "argument_utils": ["convert_neuronx_compiler_args_to_neuron", "store_compilation_config"],
    "constant": [
        "DECODER_NAME",
        "DIFFUSION_MODEL_TEXT_ENCODER_2_NAME",
        "DIFFUSION_MODEL_TEXT_ENCODER_NAME",
        "DIFFUSION_MODEL_UNET_NAME",
        "DIFFUSION_MODEL_VAE_DECODER_NAME",
        "DIFFUSION_MODEL_VAE_ENCODER_NAME",
        "DIFFUSION_MODEL_CONTROLNET_NAME",
        "ENCODER_NAME",
        "NEURON_FILE_NAME",
    ],
    "hub_cache_utils": ["ModelCacheEntry", "get_hub_cached_entries", "hub_neuronx_cache", "synchronize_hub_cache"],
    "import_utils": [
        "is_accelerate_available",
        "is_neuron_available",
        "is_neuronx_available",
        "is_neuronx_distributed_available",
        "is_torch_neuronx_available",
        "is_torch_xla_available",
        "is_transformers_neuronx_available",
    ],
    "input_generators": [
        "DummyBeamValuesGenerator",
        "DummyMaskedPosGenerator",
        "DummyControNetInputGenerator",
        "ASTDummyAudioInputGenerator",
    ],
    "misc": [
        "DiffusersPretrainedConfig",
        "check_if_weights_replacable",
        "get_stable_diffusion_configs",
        "is_main_worker",
        "is_precompilation",
        "replace_weights",
    ],
    "model_utils": ["get_tied_parameters_dict", "tie_parameters"],
    "optimization_utils": [
        "get_attention_scores_sd",
        "get_attention_scores_sdxl",
    ],
    "patching": [
        "DynamicPatch",
        "ModelPatcher",
        "Patcher",
        "patch_everywhere",
        "patch_within_function",
        "replace_class_in_inheritance_hierarchy",
    ],
    "peft_utils": ["NeuronPeftModel", "get_peft_model"],
    "training_utils": [
        "is_model_officially_supported",
        "patch_transformers_for_neuron_sdk",
    ],
}

if TYPE_CHECKING:
    from .argument_utils import convert_neuronx_compiler_args_to_neuron, store_compilation_config
    from .constant import (
        DECODER_NAME,
        DIFFUSION_MODEL_CONTROLNET_NAME,
        DIFFUSION_MODEL_TEXT_ENCODER_2_NAME,
        DIFFUSION_MODEL_TEXT_ENCODER_NAME,
        DIFFUSION_MODEL_UNET_NAME,
        DIFFUSION_MODEL_VAE_DECODER_NAME,
        DIFFUSION_MODEL_VAE_ENCODER_NAME,
        ENCODER_NAME,
        NEURON_FILE_NAME,
    )
    from .hub_cache_utils import ModelCacheEntry, get_hub_cached_entries, hub_neuronx_cache, synchronize_hub_cache
    from .import_utils import (
        is_accelerate_available,
        is_neuron_available,
        is_neuronx_available,
        is_neuronx_distributed_available,
        is_torch_neuronx_available,
        is_torch_xla_available,
        is_transformers_neuronx_available,
    )
    from .input_generators import (
        ASTDummyAudioInputGenerator,
        DummyBeamValuesGenerator,
        DummyControNetInputGenerator,
        DummyMaskedPosGenerator,
    )
    from .misc import (
        DiffusersPretrainedConfig,
        check_if_weights_replacable,
        get_stable_diffusion_configs,
        is_main_worker,
        is_precompilation,
        replace_weights,
    )
    from .model_utils import get_tied_parameters_dict, tie_parameters
    from .optimization_utils import (
        get_attention_scores_sd,
        get_attention_scores_sdxl,
    )
    from .patching import (
        DynamicPatch,
        ModelPatcher,
        Patcher,
        patch_everywhere,
        patch_within_function,
        replace_class_in_inheritance_hierarchy,
    )
    from .peft_utils import NeuronPeftModel, get_peft_model
    from .training_utils import (
        is_model_officially_supported,
        patch_transformers_for_neuron_sdk,
    )
else:
    import sys

    sys.modules[__name__] = _LazyModule(
        __name__,
        globals()["__file__"],
        _import_structure,
        module_spec=__spec__,
    )
