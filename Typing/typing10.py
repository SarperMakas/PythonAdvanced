from logging import Logger

class LoggedVar[T]:
  def __init__(self, value: T, name: str, logger: Logger) -> None:
    self.name = name
    self.logger = logger
    self.value = value

  def set(self, new: T) -> None:
    self.log("Set" + repr(self.value))
    self.value = new

