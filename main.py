from common.arguments import get_args
from common.utils import make_env
from runner import Runner
import torch


if __name__ == '__main__':
    # get the params
    args = get_args()
    env, args = make_env(args)

    # Initialize the runner
    runner = Runner(args, env)

    # Execute
    if args.evaluate:
        runner.evaluate()
    elif args.compare:
        runner.compare_models_curves()
    else:
        runner.run()
        if torch.cuda.is_available():
            print(f"Training finished using GPU: {torch.cuda.get_device_name(0)}")
        else:
            print("Training finished using CPU")