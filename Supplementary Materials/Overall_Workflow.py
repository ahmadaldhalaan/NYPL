# @begin MenuDatasetCleaning
# @in Menu.csv
# @in Dish.csv
# @in MenuItem.csv
# @in MenuPage.csv

# @out Menu_Clean.csv
# @out Dish_Clean.csv
# @out MenuItem_Clean.csv
# @out MenuPage_Clean.csv



  # @begin OpenRefineMenu
  # @in Menu.csv
  # @out Menu1.csv
  # @end OpenRefineMenu

  # @begin OpenRefineDish
  # @in Dish.csv
  # @out Dish1.csv
  # @end OpenRefineDish
  
  # @begin OpenRefineMenuItem
  # @in MenuItem.csv
  # @out MenuItem1.csv
  # @end OpenRefineMenuItem
  
  # @begin OpenRefineMenuPage
  # @in MenuPage.csv
  # @out MenuPage1.csv
  # @end OpenRefineMenuPage


    # @begin MySQLLoaderMenu
    # @in Menu1.csv
    # @out menus.Menu
    # @end MySQLLoaderMenu

    # @begin MySQLLoaderDish
    # @in Dish1.csv
    # @out menus.Dish
    # @end MySQLLoaderDish
    
    # @begin MySQLLoaderMenuItem
    # @in MenuItem1.csv
    # @out menus.MenuItem
    # @end MySQLLoaderMenuItem
    
    # @begin MySQLLoaderMenuPage
    # @in MenuPage1.csv
    # @out menus.MenuPage
    # @end MySQLLoaderMenuPage



      # @begin MySQLIntegrityCleaning
      # @in menus.Menu
      # @in menus.Dish
      # @in menus.MenuItem
      # @in menus.MenuPage

      # @out menus.Menu_clean
      # @out menus.Dish_clean
      # @out menus.MenuItem_clean
      # @out menus.MenuPage_clean
      # @end MySQLIntegrityCleaning

        # @begin MySQLExportMenu
        # @in menus.Menu_clean
        # @out Menu_Clean.csv
        # @end MySQLExportMenu.csv

        # @begin MySQLExportDish
        # @in menus.Dish_clean
        # @out Dish_Clean.csv
        # @end MySQLExportDish.csv

        # @begin MySQLExportMenuItem
        # @in menus.MenuItem_clean
        # @out MenuItem_Clean.csv
        # @end MySQLExportMenuItem.csv

        # @begin MySQLExportMenuPage
        # @in menus.MenuPage_clean
        # @out MenuPage_Clean.csv
        # @end MySQLExportMenuPage.csv

# @end MenuDatasetCleaning