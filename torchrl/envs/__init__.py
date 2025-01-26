# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from .batched_envs import ParallelEnv, SerialEnv
from .common import EnvBase, EnvMetaData, make_tensordict
from .custom import ChessEnv, LLMHashingEnv, PendulumEnv, TicTacToeEnv
from .env_creator import env_creator, EnvCreator, get_env_metadata
from .gym_like import default_info_dict_reader, GymLikeEnv
from .libs import (
    BraxEnv,
    BraxWrapper,
    DMControlEnv,
    DMControlWrapper,
    gym_backend,
    GymEnv,
    GymWrapper,
    HabitatEnv,
    IsaacGymEnv,
    IsaacGymWrapper,
    JumanjiEnv,
    JumanjiWrapper,
    MeltingpotEnv,
    MeltingpotWrapper,
    MOGymEnv,
    MOGymWrapper,
    MultiThreadedEnv,
    MultiThreadedEnvWrapper,
    OpenMLEnv,
    OpenSpielEnv,
    OpenSpielWrapper,
    PettingZooEnv,
    PettingZooWrapper,
    RoboHiveEnv,
    set_gym_backend,
    SMACv2Env,
    SMACv2Wrapper,
    UnityMLAgentsEnv,
    UnityMLAgentsWrapper,
    VmasEnv,
    VmasWrapper,
)
from .model_based import DreamerDecoder, DreamerEnv, ModelBasedEnvBase
from .transforms import (
    ActionDiscretizer,
    ActionMask,
    AutoResetEnv,
    AutoResetTransform,
    BatchSizeTransform,
    BinarizeReward,
    BurnInTransform,
    CatFrames,
    CatTensors,
    CenterCrop,
    ClipTransform,
    Compose,
    Crop,
    DeviceCastTransform,
    DiscreteActionProjection,
    DoubleToFloat,
    DTypeCastTransform,
    EndOfLifeTransform,
    ExcludeTransform,
    FiniteTensorDictCheck,
    FlattenObservation,
    FrameSkipTransform,
    GrayScale,
    gSDENoise,
    Hash,
    InitTracker,
    KLRewardTransform,
    LineariseRewards,
    MultiStepTransform,
    NoopResetEnv,
    ObservationNorm,
    ObservationTransform,
    PermuteTransform,
    PinMemoryTransform,
    R3MTransform,
    RandomCropTensorDict,
    RemoveEmptySpecs,
    RenameTransform,
    Resize,
    Reward2GoTransform,
    RewardClipping,
    RewardScaling,
    RewardSum,
    SelectTransform,
    SignTransform,
    SqueezeTransform,
    Stack,
    StepCounter,
    TargetReturn,
    TensorDictPrimer,
    TimeMaxPool,
    Tokenizer,
    ToTensorImage,
    TrajCounter,
    Transform,
    TransformedEnv,
    UnaryTransform,
    UnsqueezeTransform,
    VC1Transform,
    VecGymEnvTransform,
    VecNorm,
    VIPRewardTransform,
    VIPTransform,
)
from .utils import (
    check_env_specs,
    check_marl_grouping,
    exploration_type,
    ExplorationType,
    make_composite_from_td,
    MarlGroupMapType,
    set_exploration_type,
    step_mdp,
)
