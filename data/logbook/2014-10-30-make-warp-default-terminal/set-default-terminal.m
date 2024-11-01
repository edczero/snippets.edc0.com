/*
Compile it with (use gcc if clang is causing problems)

clang -framework Foundation -framework CoreServices -o SetDefaultTerminal <path to your .m file>

./SetDefaultTerminal
*/

#import <Foundation/Foundation.h>
#import <CoreServices/CoreServices.h>

void setDefaultTerminal(NSString *bundleId) {
    CFStringRef unixExecutableContentType = (CFStringRef)@"public.unix-executable";
    LSSetDefaultRoleHandlerForContentType(unixExecutableContentType, kLSRolesShell, (CFStringRef) bundleId);
}

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        setDefaultTerminal(@"dev.warp.Warp-Stable");
    }
    return 0;
}
