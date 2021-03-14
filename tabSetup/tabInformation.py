import tabSetup.memberTab as memberTab
import tabSetup.announcementTab as announcementTab
import tabSetup.aboutTab as aboutTab

tabs = []

tabs.append({
    "TabName": "Modify Member",
    "Description": "Modify Members within the Database",
    "Function": memberTab.setup,
})
tabs.append({
    "TabName": "Post Announcement",
    "Description": "Post an announcement to the Database",
    "Function": announcementTab.setup,
})
tabs.append({
    "TabName": "About",
    "Description": "About IEEEngage",
    "Function": aboutTab.setup,
})
