/*
Liveblog App for Pebble Time.
Code by Thomas Suarez (tomthecarrot)
*/

#include <pebble.h>

static char *subscription = ""; // name of the added subscription
static Window *win_sub; // subscribe confirmation window
static TextLayer *text_subscribed; // subscribe confirmation text

static void win_sub_load(Window *window) {
  // Create TextLayer & set parameters
  text_subscribed = text_layer_create(GRect(0, 10, 144, 100));
  text_layer_set_background_color(text_subscribed, GColorClear);
  text_layer_set_text_color(text_subscribed, GColorBlack);
  text_layer_set_overflow_mode(text_subscribed, GTextOverflowModeWordWrap);
  text_layer_set_font(text_subscribed, fonts_get_system_font(FONT_KEY_GOTHIC_24_BOLD));
  text_layer_set_text_alignment(text_subscribed, GTextAlignmentCenter);
  
  // Concatenate strings to create message & set text
  static char message[400]; // buffer to hold concatenated strings
  strcpy(message, "Subscribed to:\n"); // copy first part
  strcat(message, subscription); // concatenate second part
  text_layer_set_text(text_subscribed, message); // set text to view
  
  // Add TextLayer as a child layer to the subscription Window's root layer
  layer_add_child(window_get_root_layer(window), text_layer_get_layer(text_subscribed));
}

static void win_sub_unload(Window *window) {
  // Destroy TextLayer
  text_layer_destroy(text_subscribed);
}

static void add_subscription(char *new) {
  // Concatenate current and new subscription vars
  char updated[400]; // buffer to hold concatenated strings
  strcpy(updated, subscription);
  strcat(updated, "\n- "); // concatenate newline and list item
  strcat(updated, new); // concatenate new part
  subscription = updated; // set globally
  
  // Register timeline listener for new subscription
  //add here...
}

static void tmp() {
  // tmp test
  add_subscription("Verge Live");
  add_subscription("Maker Faire BA 2015");
  add_subscription("Twitter: @tomthecarrot");
}

static void init() {
  tmp(); // tmp test
  
  // Create main Window element and assign to pointer
  win_sub = window_create();
  
  // Set handlers to manage the elements inside the widnow
  window_set_window_handlers(win_sub, (WindowHandlers) {
    .load = win_sub_load,
    .unload = win_sub_unload
  });
  
  // Show the Window on the watch, animated=true
  window_stack_push(win_sub, true);
}

static void deinit() {
  // Destroy window
  window_destroy(win_sub);
}

int main(void) {
  init();
  app_event_loop();
  deinit();
}