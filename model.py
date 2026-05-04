from beam.integrations import VLLM, VLLMArgs 
MODEL_NAME = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"

deepseek_r1= VLLM(
    name = MODEL_NAME.split("/")[-1],
    cpu=8,
    memory="32Gi",
    gpu="A10G",
    gpu_count=1,
    vllm_args=VLLMArgs(
        model= MODEL_NAME,
        served_model_name=[MODEL_NAME],
        task = "generate", 
        trust_remote_code= True , 
        max_model_len= 8096 
    )
)