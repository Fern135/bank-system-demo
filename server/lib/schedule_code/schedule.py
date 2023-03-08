import schedule

class schedule:
    #TODO: add this when adding compound interest functionality
    def __init__(self, interval:int, task) -> None:
        """sumary_line
        
        Keyword arguments:
        argument -- interval : int how many times this should run
        argument -- task : any function in which said task will be handled
        Return: None
        """
        
        if interval is not None and task is not None:
            self.sch = schedule.every(interval).minutes.do(task)

        else:
            return False
        

    def run(self) -> None:
        try:
            self.sch.run_pending()

        except Exception as e:
            print(str(e))