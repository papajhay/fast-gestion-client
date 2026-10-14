"""Backward-compatible import for settings; use app.core.config going forward."""

from app.core.config import settings

__all__ = ["settings"]
