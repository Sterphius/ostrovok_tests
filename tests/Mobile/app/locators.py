from selene import browser

more_navigation_button = browser.element('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                         '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                         '/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget'
                                         '.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[4]')

user_email = browser.element('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                             '.widget.FrameLayout/android.widget.LinearLayout/'
                             'android.widget.FrameLayout/android.widget.RelativeLayout/android.widget'
                             '.LinearLayout/android.widget.FrameLayout[1]/'
                             'androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/'
                             'android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/'
                             'android.widget.LinearLayout[1]/android.widget.TextView')

support_navigation_button = browser.element('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                            '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                            '/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget'
                                            '.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[3]')

support_phone_call_button = browser.element('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                            '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                            '/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget'
                                            '.FrameLayout[1]/androidx.viewpager.widget.ViewPager/'
                                            'android.widget.FrameLayout/android.widget.LinearLayout/'
                                            'androidx.recyclerview.widget.RecyclerView/'
                                            'android.widget.RelativeLayout[4]')

recycler = browser.element('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                           'android.widget.FrameLayout/android.widget.LinearLayout/'
                           'android.widget.FrameLayout/android.widget.RelativeLayout/'
                           'android.widget.LinearLayout/android.widget.FrameLayout[1]/'
                           'androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/'
                           'android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/'
                           'androidx.recyclerview.widget.RecyclerView[2]')

