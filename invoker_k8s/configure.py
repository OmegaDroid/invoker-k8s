from invoke import run, task

from importlib import import_module


def default(ctx):
    kubectl_exe = ctx.get('kubectl_exe', 'kubectl')

    kubectl_context = ctx.get('kubectl_context')
    if kubectl_context:
        run('{} config use-context {}'.format(kubectl_exe, kubectl_context))

    kubectl_namespace = ctx.get('kubectl_namespace')
    if kubectl_namespace:
        run('{} config set-context --current --namespace={}'.format(kubectl_exe, kubectl_namespace))

    kubectl_cluster = ctx.get('kubectl_cluster')
    if kubectl_cluster:
        run('{} config set-context --current --cluster={}'.format(kubectl_exe, kubectl_cluster))

    kubectl_user = ctx.get('kubectl_user')
    if kubectl_user:
        run('{} config set-context --current --user={}'.format(kubectl_exe, kubectl_user))


@task
def config(ctx):
    """
    Configures kubectl to the relevant provider
    """
    config_path = ctx.get('kubectl_config_path', 'invoker_k8s.configure.default')
    module_path, func_name = config_path.rsplit('.', 1)

    module = import_module(module_path)
    func = getattr(module, func_name)

    func(ctx)
