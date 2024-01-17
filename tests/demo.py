################################################################################
#
#                                  DEMO
#
################################################################################
# Libraries
import src.packages.request     as SR
import src.packages.Collection  as SC

# main
def main():
    request     = SR.request()
    collection  = SC.collection()

    collection.getCollection()
    collection.getEnvironment()
    
    request.set_collection(
        collection.collection
    )
    request.set_environment(
        collection.environment
    )
    
    request.set_options(
        [
            ["e", ""]   ,
            ["n", "1"]  ,
            ["x", ""]   ,
            ["html", ""],
            # To test error pop up
            #["TTT", ""]
        ]
    )
    
    request.build_request()
    request.send_request()
     
# main execution
if __name__ == "__main__":
    main()