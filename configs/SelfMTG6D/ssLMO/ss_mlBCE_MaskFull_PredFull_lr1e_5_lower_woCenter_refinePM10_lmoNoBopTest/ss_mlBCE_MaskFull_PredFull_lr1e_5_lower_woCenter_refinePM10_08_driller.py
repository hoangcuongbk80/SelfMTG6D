_base_ = ["ss_mlBCE_MaskFull_PredFull_lr1e_5_lower_woCenter_refinePM10_01_ape.py"]

OUTPUT_DIR = "output/SelfMTG6D/ssLMO/ss_mlBCE_MaskFull_PredFull_lr1e_5_lower_woCenter_refinePM10_lmoNoBopTest/driller"

DATASETS = dict(
    TRAIN=("lmo_NoBopTest_driller_train",),
    TRAIN2=("lmo_pbr_driller_train",),  # real data  # synthetic data
)

MODEL = dict(
    # synthetically trained model
    WEIGHTS="output/MTGOPE/lmoPbrSO/resnest50d_online_AugCosyAAEGray_mlBCE_DoubleMask_lmo_pbr_100e/driller/model_final_wo_optim-bded40f0.pth"
)
