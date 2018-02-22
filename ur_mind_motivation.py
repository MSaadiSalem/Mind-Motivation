#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import fresh_tomatoes
import media

feed_ur_mind = media.Movie("Feed Your Mind With Success",
                           "The person you will be in the future is based on EVERYTHING you do today.",
                           "",
                           "https://youtu.be/cEEhBmEJMEc")

best_vr_of_urself = media.Movie("Best Version Of Yourself",
                                "Push yourself every day, to become the very best version of yourself. You don't need to compete with others, just work on becoming better EVERY SINGLE DAY.",
                                "",
                                "https://youtu.be/lkDBImBAmN0")


anything_possible = media.Movie("Anything Is Possible.",
                                "You are capable of great things in your life time, but great things can only be created if you first BELIEVE they can, and then you TAKE ACTION. Anything IS possible.",
                                "",
                                "https://youtu.be/aqiqA45xSIw")

struggle = media.Movie("STRUGGLE makes you STRONGER",
                       "Struggles, challenges and hard times offer you much more value than any other time in your life. You can not grow without struggle. You can not get STRONGER without resistance. Think about a time in your life that may have been hard, but forced you to become better. Get grateful for the struggles and WORK on yourself to ensure your future has much more PLEASURE than PAIN.",
                       "",
                       "https://youtu.be/Wcf5b3mENJU")

never_giveup = media.Movie("Never Give Up",
                           "If I could go back and give my younger self just one piece of advice, what would it be? Never give up.",
                           "",
                           "https://youtu.be/uuCAYqyFMg8")

controlled_by_things = media.Movie("Don't Allow Your Life To Be Controlled By These 5 Things",
                                   "Many people spend their life, at the mercy of circumstances. Living at the mercy of what happens to them. Living at the mercy of other people. NOT living in the present, because they are stuck in the prison of their past.",
                                   "",
                                   "https://youtu.be/nQ7XCalQfx0")

movies = [feed_ur_mind, best_vr_of_urself, anything_possible,
          struggle, never_giveup, controlled_by_things]
fresh_tomatoes.open_movies_page(movies)
