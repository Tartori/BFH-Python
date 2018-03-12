/* state machine of garage door control as a switch/case in C */
 
/* state enumeration of the states involved */
typedef enum { CLOSED, OPENING, OPEN, CLOSING, ERROR } state_t;

/* control mode for motor */ 
typedef enum { OFF, UP, DOWN } motor_mode_t;

/* input/output functions */
extern int close_button(void);        /* returns Boolean value */
extern int open_button(void);         /* returns Boolean value */
extern int limit_switch_open(void);   /* returns Boolean value */
extern int limit_switch_closed(void); /* returns Boolean value */
extern void motor(motor_mode_t);

/* implementation of the transition and action table of the Mealy machine */
state_t state_transition_action(state_t current_state)
{
    state_t next_state; 
    switch(current_state) 
    {
        case CLOSED:
            if (open_button()) {
                next_state = OPENING;
                motor(UP);
            } else {
                next_state = CLOSED;
            }
            break;
        case OPENING:
            if (limit_switch_open()) {
                next_state = OPEN;
                motor(OFF);
            } else if (close_button()) {
                next_state = CLOSING;
                motor(DOWN); 
            } else {
                next_state = OPENING;
            }
            break;
        case OPEN:
            if (close_button()) {
                next_state = CLOSING;
                motor(DOWN);
            } else {
                next_state = OPEN;
            }
            break;
        case CLOSING:
            if (limit_switch_closed()) {
                next_state = CLOSED;
                motor(OFF);
            } else if (open_button()) {
                next_state = OPENING;
                motor(UP);
            } else {
                next_state = CLOSING;
            }
            break;
        case ERROR:
        default:
            next_state = ERROR;
    }
    return next_state;
}

void state_machine()
{
    state_t state = CLOSING;
    for (;;)
    {
        state_t next_state = state_transition_action(state);
        state = next_state;
    }
}

int error_state()
{
    return ERROR;
}