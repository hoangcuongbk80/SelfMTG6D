_base_ = ["ss_FreezeBN_20e_Blender08_bboxCrop_woDepth_refinePM100_blenderCrop_DZI10_ape.py"]

# refiner_cfg_path = "configs/_base_/SelfMTG6D_refiner_base.py"

OUTPUT_DIR = "output/SelfMTG6D/ssLMCrop/FreezeBN_20e_Blender08_bboxCrop_woDepth_refinePM100_blenderCrop_DZI10/driller"

DATASETS = dict(
    TRAIN=("lm_crop_driller_train",),  # real data
    TRAIN2=("lm_blender_driller_train",),  # synthetic data
    TEST=("lm_crop_driller_test",),
)


MODEL = dict(
    # synthetically trained model
    WEIGHTS="output/MTGOPE/lm_crop_blender/resnest50d_a6_AugCosyAAEGray_BG05_mlBCE_bboxCrop_DZI10_lm_blender_100e/driller/model_final_wo_optim-c1cc7169.pth"
)
