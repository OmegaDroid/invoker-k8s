from invoke import Collection

from .configure import config
from .kustomize import kustomize
from .k8s import apply, deploy


ns = Collection(
    'k8s',
    config,
    kustomize,
    apply,
    deploy,
)
