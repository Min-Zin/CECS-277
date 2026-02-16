import logger

def func1():
    log1 = logger.Logger()
    log1.write_msg("In func 1")

def func2():
    log2 = logger.Logger()
    log2.write_msg("In func 2")

def main():
    log = logger.Logger()
    log.write_msg("Begin main")
    func1()
    func2()
    log.write_msg("End main")
    log.close_file()

main()