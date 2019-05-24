from os.path import join
from invoke import task, run


@task(help={
    'path': 'The path to the kustomize input (uses kustomize_path from the invoke context if not specified)',
    'output_file': 'The output path for the built config, stdout if nothing is set'
})
def kustomize(ctx, path=None, output_file=None):
    """
    Generates a kubernetes config from a kustomize template

    All parameters are configurable in the invoke config
    """
    cmd = ctx.get('kustomize_cmd', 'kustomize')
    kustomize_root = ctx.get('kustomize_root', 'k8s')
    build_path = path or ctx.get('kustomize_path', join(kustomize_root, 'overlays', ctx['env']))
    output_string = '-o {}'.format(output_file) if output_file else ''

    run('{cmd} build {path} {output}'.format(
        cmd=cmd,
        path=build_path,
        output=output_string,
    ))
