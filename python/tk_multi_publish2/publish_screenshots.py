import sgtk
import os
import os.path

import glob

logger = sgtk.platform.get_logger(__name__)


class PublishScreenshots():
    """
    Publish snapshots class
    Folder Example:
    self.current_unreal_project = "C:/ARK2_Dev-Milestone1/Projects/PrimalArk"
    self.screenshots_path = "{}/Saved/Screenshots/WindowsEditor".format(self.current_unreal_project)
    """
    def __init__(self):
        self.current_unreal_project = None
        self.screenshots_path = None

    def list_files(self):
        """
        If we are using "tk-unreal" engine, lists all screetshots in the screetshots folder
        Otherwise return None
        """
        engine_name = sgtk.platform.current_engine().name
        msg = "Engine is: {}".format(engine_name)
        logger.debug(msg)
        print(msg)

        if engine_name == "tk-unreal":
            try:
                import unreal
                paths = unreal.Paths()

                root_dir = paths.root_dir()
                project_dir = paths.project_dir()
                project_dir = project_dir.strip("../")
                self.current_unreal_project = "{}{}".format(root_dir, project_dir)
                self.screenshots_path = "{}/Saved/Screenshots/WindowsEditor".format(self.current_unreal_project)

                if os.path.exists(self.screenshots_path):
                    file_list = sorted(glob.glob('%s/*.png' % self.screenshots_path), reverse=True)
                    return file_list
                else:
                    msg = "Unable to find the UE5 screenshots folder: {}".format(self.screenshots_path)
                    print("msg")
                    logger.debug(msg)

            except:
                msg = "Error locating the UE5 screenshots folder: {}".format(self.screenshots_path)
                print("msg")
                logger.debug(msg)
                pass
        return None
