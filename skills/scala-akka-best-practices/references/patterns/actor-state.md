# Commands, entity state, validation, and compare-and-set

435 source-specific cases. Statements retain their historical scope and source stance. Read related PR cases for corrections or alternatives.

## Cases

- A1-0021 — CustomerAdvisoryProfileEntity intentionally does not update lastUpdatedTS
- A1-0113 — Place SgPlanAcknowledgementManagerEntity error log in command handler
- A1-0433 — Deleting all plan-fee instructions conflicts with DeletePlanFeeInstructionCmd semantics
- A1-0434 — Use ResetAll command/event with reset date and clear instructions
- A1-0474 — Operation belongs in entity
- A1-0769 — Manual cancellation gets encapsulation command; system cancellation uses existing no-encapsulation
- A1-0790 — Use InvestmentRrtCommandContext with rrtContext None instead of SystemTriggeredCommand
- A1-0823 — Financial SIP patch needs event identity or remark distinguishing system patch from reanswer
- A1-0824 — Events must preserve what happened beyond temporary logs Jira and sheets
- A1-0992 — Update only acknowledgement keys matching scheduleId rather than replace all
- A1-1025 — Capture all acknowledgements together to avoid overriding
- A1-1028 — Separate threshold-breach acknowledgements from recurring investment schedule acknowledgements
- A1-1136 — Use parallelism one for commands to same entity
- A1-1194 — PlanAcknowledgementState keys recurring transfer acknowledgements by sourcePlanId
- A1-1195 — CapturePlanAcknowledgments replaces the complete matching schedule acknowledgement set
- A1-1196 — RemovePlanAcknowledgmentCmd derives removals and preserves unrelated acknowledgement state
- A1-1197 — AddPlanAcknowledgmentsCmd tops up posthoc acknowledgement without replacing existing set
- A1-1203 — Initialize plan acknowledgement entity
- A1-1204 — Register plan acknowledgement entity
- A1-1211 — Replace acks by acknowledgement identity rather than Set entry
- A1-1212 — Posthoc action should update schedule-state acks rather than persist as own state context
- A1-1214 — Removal result must return being-removed acks rather than remaining
- A1-1215 — Persist removal event only after checking removed results nonempty
- A1-1270 — Trade deletion before external export already nonterminal; force transition may unnecessary
- A1-1464 — DeleteFeeChargeRequestCmdHandler acknowledgements refusal can leave undeleted charge
- A1-1653 — Typed top-level ActorSystem failed with Lagom ScaladslKafkaSubscriber
- A1-1707 — If delete cmd carries instrumentCcy validate matches state
- A1-1710 — Add same state-versus-command instrument currency validation here
- A1-1720 — Do not send expired comms merely after successful remove command
- A1-1739 — Notify failure and update next date in same command handler
- A1-1740 — Recurring-transfer nextUpcomingDate rollout needs complete population and every-trigger advance
- A1-1741 — RequestInvestmentTransferWithRedemptionCmdHandler also advances nextUpcomingDate
- A1-1809 — CustomerEmployeeEmailV2 producer already wired and eagerly creates topic
- A1-1871 — Deprecate old events but retain no-op state handlers
- A1-1909 — Bulk price command overrides whole state: merge combinedPrices with manual prices
- A1-2008 — Retain still-needed entity in this PR; eventual removal separate
- A1-2040 — Fee command duplicate initiatingFullRedemptionRequestId check makes topic handling idempotent
- A1-2157 — Approval operation state change needs revisit
- A1-2300 — Why entity was never initialized with ClusterSharding
- A1-2336 — Akka ExtensionId singleton per actor system
- A1-2337 — Eager application init exposed manual cluster join hidden in Lagom client
- A1-2338 — Eager init reduces AskTimeout during restarts but coordinator deletion still causes some
- A2-0021 — PortfolioUnderlyingManager: This will go to entity? Do we need that or readside is ok?
- A2-0025 — package: We may decide to make it required field in DTO after successful backfill \(or adding on-the-fly lookup\), but here it must stay optional as [person] said, due to histor...
- A2-0026 — BackfillPlanProfileTenantIdCmdHandler: Let’s also return without events if same tenantId already exists. Then we won’t have duplicated events, as the subscriber might process a ...
- A2-0027 — BackfillPlanProfileTenantIdTaskTopicSubscriber: We shouldn’t need planId as part of the cmd since it’s already entityId
- A2-0028 — PlanProfileJdbcProjectionV3: Since we have the full PlanProfile in the `PlanProfileTenantIdBackFilledEvt`, let’s use it directly instead of fetching from entity again.
- A2-0031 — BackfillPlanProfileTenantIdTaskTopicSubscriber: I realize we could have made the task keyed by customerId instead, then in this subscriber, we query planProfiles by customerId a...
- A2-0039 — BaseRedemptionCommunicationV2Projection: Naming can be a little confusing now
- A2-0052 — SgWorkflowEngineE4s: Can we double check this endpoint with workflow-engine again? I think the ActorRole here is supposed to be for assignee type?
- A2-0077 — FixV3FeeRedemptionTransactions: Temp code so maybe ok, but I remember we have a refactored version of this code in transaction svc…
- A2-0081 — CreateFixedMaturityProductGoal: If small number of goals then it’s ok, but ideally we could use an async loading cache here \+ go to readside instead of entity
- A2-0095 — InstrumentTransferService: Do we need to specify brokerAccountId in this cmd? Since it’s possible to have multiple broker accounts?
- A2-0106 — GoalSupportingDataProjection: This block probably can refactor to avoid repeating the code vs `handleGoalCreationApprovedHandler`
- A2-0120 — InvestmentPlanEntity: The request would be upserted by `InvestmentRequestCreatedEvt`. We don’t need to do anything here for the state
- A2-0140 — InvestOnceCmdHandler: Nit: `maybeInvestmentRequestCreationApprovedEvt.toList` is sufficient
- A2-0143 — StopRecurringInvestmentScheduleCmdHandler: Same here and the cmd handler below. Can use Option#toList
- A2-0171 — CreateGoalWithPlansCmdHandler: map
- A2-0200 — InitiateCancellationFlowCmdHandler: This `INVALID_CANCEL_ATTEMPT` is mapped to NotFound right now. It seems not used, so maybe change it to BadRequest instead?
- A2-0201 — InitiateCancellationFlowCmdHandler: If you stick with throwing, need to add handling in compliance svc’s state change logic as well
- A2-0202 — InitiateCancellationFlowCmdHandler: We will need to add another `InvestmentSvcException` in investment-impl otherwise it won’t work in cluster mode
- A2-0210 — BffServiceE4s: Yea unfortunately we will have to type out the `Schema` for all data models that are \(recursively\) used in endpoints' input/output. It’s not exactly a refactor ...
- A2-0211 — package: [person] [person] Looks the issue to due to `BrokerAccountCashBalanceDto` containing a nested field of itself
- A2-0219 — SgGoalCreateApprovalSummaryBehaviour: State change applies here. Let’s check w PM \+ designer
- A2-0230 — RebalancePlanTableV4: Remove all the index on customerId/goalId/tradingAccountType/planCcy - we don’t use them at all.
- A2-0231 — ClientEntity: You will need to add `TenantSvcException` in tenant-impl that extends `PlayJsonSerializable` otherwise serdes will fail in cluster mode
- A2-0244 — SgGoalApprovedForCreationBehaviour: Ideally `validate` should return the resolved objects that all these create steps can use without further validation.
- A2-0263 — InstrumentTransfer: Yea the trigger endpoint is one plan only cuz that’s the max safety we can guarantee \(via PlanTraderEntity\). I allow simulation to accept multiple source p...
- A2-0264 — AcceptRebalanceSellTradeRequestCmdHandler: We agreed to leave this intact. It will be short circuited later due to no sell orders.
- A2-0274 — ChargeHelpers: `state.feeInstructions.to(TreeMap)` is sufficient I think
- A2-0276 — PlanFeeInstructionEntity: Do we need to error here? Just return ack without any events?
- A2-0278 — PlanFeeInstructionEntity: Similarly, for upsert command, overriding whole Map with single entry from an empty map is the same if we add that entry directly. So there’s no value ...
- A2-0281 — FeeInstruction: Alright, I’m ok if you prefer this approach too. Just one small ask to return the Map from GetCmd, and you can define the period case class \+ conversion logic i...
- A2-0282 — PlanFeeInstructionEntity: The entity state is default with empty fee instructions, it means the plan always exists, just without any data. Modelling it this way means you can’t ...
- A2-0283 — PlanFeeInstructionEntity: Just thinking out loud, I’m not sure about capturing this effectiveEndDate in the event
- A2-0286 — FeeRangeManager: It seems the later PRs assume that firm’s fee range config is already in good state. So maybe we should add validation here to ensure the config is properly con...
- A2-0289 — common: Removed since wrong existing config. `report` doesn’t have any entity anymore
- A2-0291 — common: Removed since wrong existing config. `projection` doesn’t have any entity anymore
- A2-0293 — common: Correct config but still removed, cuz `composition` doesn’t have any entity anymore
- A2-0294 — common: Removed since wrong existing config. And `performance` doesn’t have any entity anymore.
- A2-0297 — common: Removed. Existing config is wrong \+ `admin` ~~doesn’t have any entity~~ was using default value
- A2-0300 — BackfillPlanInvestmentCmdHandler: I think this could be confusing to read, e.g. what if existing but doesn’t match the resolve? Well it cannot be, due to how we resolve. So mayb...
- A2-0301 — BaseServiceLogicImpl: The cmd is idempotent anyway, so maybe we just trigger from goal level instead? No need to double lookup
- A2-0302 — UpdateInvestmentPlanInitialInvestmentRequestCmdHandler: So how do we get of this invalid data state?
- A2-0303 — UpdateInvestmentPlanInitialInvestmentRequestCmdHandler: And how will we sync? If there is endpoint already, let’s document it in this error msg as well
- A2-0308 — BackfillPlanInvestmentCmdHandler: Move the resolve logic to this `case None`, and no need to check `plan.initialInvestmentRequest` anymore
- A2-0309 — BackfillPlanInvestmentCmdHandler: Wrong id
- A2-0310 — UpdateInvestmentPlanInitialInvestmentRequestCmdHandler: Not sure about refreshing the updatedAt here. Is it used for anything related to customer, if not then safe
- A2-0311 — UpdateRecurringInvestmentScheduleCmdHandler: Yea ok this shouldn’t happen in the first place. Agree let’s put error alert and skip. We will decide what to do when it happens :th...
- A2-0315 — UpdateInvestmentPlanRecurringInvestmentScheduleCmdHandler: Let’s name these cmd as “Backfill” cmd as well? Not good to name them “Update” but actually if any change is include w...
- A2-0317 — InstrumentMarketDataEventProcessorForMultiCcy: We don’t need this check here, then entity has the logic already
- A2-0324 — MarketDataUploader: Here we want to check. It’s same rationale as `safeUploadMonthlyChanges` because we are setting `triggerFxConversion` = true, which will override the logic i...
- A2-0363 — CreateGoalWithPlansCmdHandler: ```
- A2-0378 — TenantAwareInstrumentManager: Need to check whitelisting as well. Better to refactor to sharing common code, same approach as FundList/FundDetails
- A2-0476 — BffServiceImpl: Ok so my above example would be when FA performs operation on-behalf of customer, so employee would be there.
- A2-0502 — package: Same here, let’s not stamp it here. Rather we add the resolved fee to `CreateInvestmentPlanCmd` as separate field like other cmd I think
- A2-0505 — package: Should we drop this field in the cmd?
- A2-0520 — HkFeeManagerProjection: There is no tax in HK at all, so maybe simpler solution would be to have `HkFeeManagerProjection` only handle `FeeChargeDiscountAppliedEvt` which would t...
- A2-0534 — HkFeeManagerEntityTest: We don’t need this test cuz there is no split logic at entity level?
- A2-0536 — HkCustomerDailyAltsFeesCalculator: Actually this const makes me more paranoid and having to check in 2 places to ensure `FiveHundredThousand` having the correct value. However w...
- A2-0537 — HkFeeManagerEntityTest: There is no logical change in the entity/cmd handler. It’s better to have the waiver bit injected, and keep the existing test in tact. Then you can unit ...
- A2-0544 — HkChargeCommunicationProjection: This logic actually exists in `InitiateFeeRedemptionCmdHandler`, it’s best we rely on sequence of events, rather than duplicating it again.
- A2-0558 — DistributionCalculatorHelperHk: Can we retry \+ fallback to entity for this, just to be on safe side?
- A2-0579 — UpdateProductCharacteristicsCmdHandler: If this cmd handler does not support B2B types, let match and reject it outside, then pass in only the resolved B2C type
- A2-0582 — UpdateProductCharacteristicsCmdHandler: Let’s also validate that we can’t change B2C ↔︎ B2B productlines?
- A2-0590 — UpdateProductCharacteristicsCmdHandler: private
- A2-0592 — UpdateProductCharacteristicsCmdHandler: immutable List instead? Same for b2b
- A2-0596 — ModelPortfolioEntity: Can we update this to check TAA changed OR EffectiveDate changed
- A2-0597 — ModelPortfolioEntity: So there are 2 events:
- A2-0598 — ModelPortfolioEntity: It’s not a problem/caveat in advisory, cuz it handles both `PortfolioMovedToNewTargetAllocationMsg` and `PortfolioAllocationTargetUpdatedMsg`
- A2-0604 — HkFundSmartCollectionManager: This step is common between the two. Should be able to refactor a bit so that we only branch on customerId when checking corp profile. Same for SG
- A2-0646 — GoalModifyBehaviourHelpers: Same here. Switch to calling the new `findProductPortfolio(advisoryTag, newRiskTarget)`
- A2-0693 — DividendEntity: Let’s check for all states - you can’t delete if data mismatch, regardless of state
- A2-0694 — DividendEntity: Let’s use the new check method?
- A2-0695 — DividendEntity: Let’s give more context for all these error message. We want to warn support person that data mismatch, and that we are ignoring the command, please investigate ...
- A2-0696 — Review: Since we do not support topping up unit dividend on top of existing \(cash or unit\) dividend at all, let’s also check the trigger endpoint of unit dividend, and add que...
- A2-0718 — PortfolioMonthlyChangesHelper: I think there are 2 types of race conditions we might see here:
- A2-0747 — DividendEntity: Let’s log error for both `BrokerAccountReinvestDividendCmd` and `BrokerAccountDistributeDividendCmd` if dividend data mismatch between entity and cmd. So that if...
- A2-0748 — DividendEntity: You need to handle this `BrokerAccountDeleteDividendCmd`, not `DeleteCmd`
- A2-0750 — DividendEntity: This entity doesn’t even distinguish between unit vs cash dividend. So I don’t know we can safely handle this….
- A2-0753 — SplitCashReservationsForFullRedemptionFeeChargeCmdHandler: It starts from None, and then capture the fee charge amount so far for the full redemption. It might have 2 fee charge...
- A2-0760 — CustomerStatusHelper: Let’s use same approach as goal svc
- A2-0776 — SgRecommendedInvestmentManager: Can we refactor so that we can avoid calling Option.get
- A2-0783 — SgRecommendedInvestmentManager: Best if we can refactor to avoid make unnecessary calls
- A2-0784 — SgRecommendedInvestmentManager: Can we change to this style instead
- A2-0807 — TimeSeriesServiceClient: Can use `ServiceExceptionFactory.NoopFactory` if a service doesn’t have any need for custom exception
- A2-0813 — BrokerOrderTopicSubscriber: Lagom is using below by default
- A2-0820 — ServiceClientExceptionSerializerTest: Shouldn’t it be `implicit val system: ActorSystem`
- A2-0821 — ProductPortfolioRepository: Maybe we can keep this method generic, but only handle for CoreEnhanced for now…
- A2-0858 — InstrumentMarketDataEntity: If it’s None, `exists` will return false and we won’t fail
- A2-0859 — InstrumentMarketDataEntity: As in is this marketdata update original \(and not result of fx conversion\)
- A2-0860 — NonAltsFeeManager: Can you help to refactor this bit a little, to make it clearer
- A2-0863 — OverrideRedemptionCashReservationsCmdHandler: Should be safe to just use `RedemptionRequestStatus.terminalStatuses`… FAILED should block as well
- A2-0882 — EmailProviderData: All of these, in theory, would need to be optional. Cuz there might be existing message in the kafka topic without the fields, and communication svc starts ex...
- A2-0883 — StatementDataGenerator: Let’s filter for dpmGoals outside, regardless of `ignoreTimeForDebug`
- A2-0884 — StatementEmailProducer: Let’s name these `DpmSemiAnnualReport*` or `DiscretionarySemiAnnualReport`
- A2-0887 — StatementEmailProducer: Can help to rename this typo `MonthlyStatemnetGenerated`
- A2-0889 — HkServiceLogicImpl: Looking at `StatementDataGenerator.createStatementDataAndGeneratePdf`, looks like it’s better to use `statementPeriod = END_OF_MONTH` and `monthPeriod = Some...
- A2-0892 — BaseServiceLogicImpl: I extracted `IncludeExcludeUtils`. Can see example for rebate / charge svc. If make sense, maybe we can refactor to use that as well
- A2-0894 — StatementGenerationScheduler: Maybe getYear - 1 is cheaper?
- A2-0895 — StatementGenerationScheduler: Should be July?
- A2-0896 — HkServiceLogicImpl: Looks like this is not needed, as `endDateOfStatement` will be resolved from `yearMonth`
- A2-0898 — StatementGenerationScheduler: Should we take in `today: LocalDate`?
- A2-0901 — StatementGenerationScheduler: Nit: `shouldGenerateDpmSemiAnnualReport`
- A2-0903 — StatementGenerationScheduler: Nit: `generateMonthlyStatement`
- A2-0906 — allInvestmentGoalsPage: You can have both
- A2-0907 — StatementDataGenerator: Maybe rename this val to `isApplicableForStatementType`
- A2-0910 — StatementPageData: Can you remind me again why this condition is not just `startOfNonDiscretionaryGoalIndex > 0` ? Shouldn’t the condition be same as one in `showGoalOnLeftOfCov...
- A2-0912 — StatementPageData: Both this and the one below should check against `MaxGoalRowsCanFitOnLeftSectionOfCoverPagePureGoal` \(even though left and right here ref the same const\)?
- A2-0913 — StatementPageData: Maybe we can put some common method so it’s easier to follow
- A2-0914 — StatementPageData: Also this has an implicit assumption that we only calls this method in DPM semi-annual report, which doesn’t have non-DPM heading and hence no need to if such...
- A2-0915 — StatementPageData: Let’s add comment here too
- A2-0916 — StatementPageData: Let’s put some comment explaining this a bit, e.g. `reserve 3 rows for [...] as compared to CoverPagePureGoal`
- A2-0917 — ReportService: The term for this \(understood by product and clients\) is actually `semi-annual report` \(as opposed to `monthly statement`\) hence this name everywhere
- A2-0918 — StatementDataGenerator: Actually no need a default `case _` as well cuz it should already give MatchError by default.
- A2-0919 — ReportService: [person] I don’t really follow this comment…
- A2-0922 — StatementPageData: Yea the condition is negation, applicable for all of these pages as well I think. But it was like this in the templates and we simply moved them out \+ added ...
- A2-0924 — FeeManager: As discussed, let’s try to refactor and move this decision to outer level \(similar to fee estimation query\), cuz we already have all the planProfiles and customerI...
- A2-0929 — package: We won’t be sending this as separate payload anywhere between the actors, so shouldn’t need extend `PlayJsonSerializable`
- A2-0930 — package: Should we use the above isDiy instead? We do not support RF semi-liquid alts yet \(I don’t know if we will one day\), until then, and anyway we are only targeting the n...
- A2-0932 — InitiateFeeChargeCmdHandler: Maybe we can rearrange this logic a little
- A2-0934 — commands: nit: let’s name this field here and above cmd with same name
- A2-0939 — InitiateFeeChargeCmdHandler: Not cleanest code branches, but if we reach here, we already validated `!noFeeChargeRequired`. This is why existing code also calls `maybeAccumulate...
- A2-0952 — BaseRedemptionCommunicationV2Projection: Can import `TraversableOnceUtils` and use it like this
- A2-0970 — NonAltsFeeManager: There’s a small performance boost here cuz [person] queries tradable-goals by customerId first, and we only care about checking TAA if a plan does not exist i...
- A2-0993 — NotifyRebalanceTradeSettlementAmendedCmdHandler: Probably check w trading team but if amendment comes after buy started, the buy amount is already determined
- A2-0994 — NotifyRebalanceTradeSettlementAmendedCmdHandler: We need to flip this amount
- A2-0995 — NotifyRebalanceTradeSettlementAmendedCmdHandler: Don’t we need more brackets to group these conditions?
- A2-0996 — package: Rename to `NotifyRebalanceTradeSettlementDetailsAmendedCmd`… do the same for event and kafka msg
- A2-0997 — NotifyRebalanceTradeSettlementAmendedCmdHandler: This is very dangerous and potentially lead to wonky data state if not done properly by POps. In fact, if you check the entrypoi...
- A2-1001 — NotifyRebalanceTradeSettlementAmendedCmdHandler: As discussed on Slack thread w trading \+ POps, we won’t touch cash reservations, this means buy trade is not affected by amendm...
- A2-1002 — NotifyRebalanceTradeSettlementAmendedCmdHandler: If buy trade has not started, and we amend totalSoldAmount but keeping cashReservation intact, we might run into additional cash...
- A2-1003 — NotifyRebalanceTradeSettlementAmendedCmdHandler: This `cashReservations` is from sell trade, to be used by subsequent buy trade.
- A2-1004 — NotifyRebalanceTradeSettlementAmendedCmdHandler: check if diff, log here as well
- A2-1005 — NotifyRebalanceTradeSettlementAmendedCmdHandler: No need to check here
- A2-1006 — RedemptionRequestTopicSubscriberV3: Not sure if we need all these validation in transaction svc. Maybe just dump directly with status = `SETTLEMENT_CONFIRMED`.
- A2-1009 — package: Name should be `AmendSettlementCmd`. Update for cmd handler too
- A2-1010 — SettlementAmendedCmdHandler: So this flag `chargeFeeForFullRedemption` is not used? How does this flow work if we amend for full redemption? Probably a question for trading team...
- A2-1011 — SettlementAmendedCmdHandler: Ok this one is not safe. On redemption trade side, cash reservations \(if any\) correspond to each individual orders, however if full redemption fee...
- A2-1013 — SettlementAmendedCmdHandler: Only log this error if current `request.settlementConfirmation.cashReservations` is different from `cmd.cashReservations`… currently trading side wo...
- A2-1014 — SettlementAmendedCmdHandler: The settled amount surely is going to be diverged \(exactly the point of the amendment\). We want to log if the cash reservations also changes \(exp...
- A2-1015 — SettlementAmendedCmdHandler: ```
- A2-1035 — CustomerAdvisoryProfileEntity: Yea, luckily we haven’t launched DPM, so no customers currently have valid DPM status and in VC grace period. So we can afford to leave with this ...
- A2-1050 — GoalBasedStatementInfoDbDto: I’m not sure if we need all these new fields in `*DbDto`. As I understand, these DTO are persisted and used to check if a statement is reprint or not.
- A2-1051 — StatementPageDataDto: Still feel that `numberOfDiscretionaryGoals` and `startOfNonDPMGoalIndex` are duplicating each other. I feel we should be able to make it work with just on...
- A2-1052 — GoalBasedStatementDataGenerator: Use the `empty`?
- A2-1053 — GoalBasedStatementDataGenerator: Let’s reverse the goalDetails here before returning, so it’s easier to follow… a bit out of context when we reverse when assigning to `AllInvest...
- A2-1054 — PageDataGenerator: Similar here… “SG AllInvestmentGoals templates do not distinguish DPM and non-DPM goals, hence treating all goals as non-DPM”
- A2-1055 — StatementPageData: Let’s use named var, e.g. `startingBalance = startingBalance + other.startingBalance`. A bit easier to read, and safer to refactor later
- A2-1056 — package: Should be compatible cuz this is not persisted \(only the `*DbDto` are persisted\).
- A2-1057 — GoalBasedStatementDataGenerator: Maybe give a bit more context.. “SG CoverPage templates do not distinguish DPM and non-DPM goals, hence treating all goals as non-DPM”
- A2-1058 — GoalBasedStatementDataGenerator: Maybe put a comment here to explain this is just dummy value as base input. We have this thing just because we reuse the same case class for inp...
- A2-1059 — PageDataGenerator: Actually we have too many region pattern matching in this method. Maybe consolidate it a bit
- A2-1060 — StatementPageDataDto: Let’s rename it to `totalNumberOfDiscretionaryGoals` then
- A2-1061 — GoalBasedStatementInfoDbDto: Yea so I think adding these new fields to `*DbDto` can cause confusion for existing data if we don’t retrospectively update them.
- A2-1062 — StatementPdfGeneratorTest: I suppose this assertion at best can only verify the html templates don’t throw error, and that some pdf file is generated.
- A2-1063 — PageDataGenerator: Can we change this method to additionally return `maxNoOfRowCanFitOnCurrentPage`? I find it a bit funky to check the template name again below. Maybe sth like...
- A2-1064 — package: [person] after checking the usage of this class again, I’m convinced that
- A2-1065 — PageDataGenerator: Maybe just use named var here
- A2-1066 — GoalBasedStatementInfoDbDto: Let’s add these fields into the list of data-loss fields in the comment in `GoalBasedStatementPageDataDbDto`, together with explanation, e.g. isDpm ...
- A2-1067 — StatementPageDataDto: After your change to remove the usage of `totalNumberOfDiscretionaryGoals` inside template, we now can remove this field from the CoverPageData completely ...
- A2-1071 — InvestmentCommunicationV2EventProcessor: So invalid bank account state \(e.g. 2 bank accounts\) will throw can cause this processor to get stuck here. How do we go about resolvi...
- A2-1080 — DpmStatusLogic: [person] [person] this kind of validation in logic \+ blind update in entity is actually not safe against race condition / concurrent modification. Specialized c...
- A2-1081 — ReportApplication: Just some notes here, yall are right about the trade-offs but manual start is not that bad, depending on use cases.
- A2-1108 — DetectUpcomingRecurringInvestmentCmdHandler: Remind me how does notification for upcoming-recurring-txn work? It seems we only have amount, without fundingCcy in this event. How...
- A2-1109 — MakeRecurringInvestmentCmdHandler: We should throw if fxRate is missing for autofx?
- A2-1114 — MakeRecurringInvestmentCmdHandler: Need to reply with exception, cannot just throw like this
- A2-1115 — MakeRecurringInvestmentCmdHandler: It doesn’t matter so let’s relax this and simple ignore indicativeFxRate even if it’s provided? at most let’s just log warn?
- A2-1119 — MakeRecurringInvestmentCmdHandler: Should this use `resolvedFundingInstructions` too?
- A2-1122 — RecurringInvestmentProcessor: This one is just used for tradability \+ compliance check. We don’t pass this amount to cmd, only the fxRate
- A2-1125 — DetectUpcomingRecurringInvestmentCmdHandler: Then we don’t need `indicativeFxRate` in this detect cmd either
- A2-1126 — DetectUpcomingRecurringInvestmentCmdHandler: Does this amount needs to be “correct” amount here? Maybe just make it as deprecated, and only use if old events
- A2-1162 — SuggestAllocationTargetUpdateCmdHandler: Are we sure this is what we want for Factors in SG? Cuz it’s still Advisory there currently? Let’s check w PM?
- A2-1173 — ChargeApplication: Shouldn’t have any issue to spawn a simple actor, but yeah if that throws, it will block init of everything else, and cause the HttpServerStartUp onMemberUp t...
- A2-1175 — ClusterStartup: So I guess the only reason for `ClusterStartup` to own the termination bit is because `onMemberUp` itself might not have access to the actorSystem
- A2-1191 — EmailDataFactory: Let’s just return for planCcy? A bit weird to see None here \(I know it’s existing code\)
- A2-1192 — EmailDataFactory: Is this flag a bit confusing for CPF/SRS?
- A2-1193 — EmailDataFactory: It seems this piece of code didnt exist for Alts flow before, because we assumed autofx is not applicable for Alts.
- A2-1196 — EmailDataFactory: Should we change these fields to use data from `fiDetails`?
- A2-1204 — HttpServerStartup: Should we make `route` and `rejectionHandler` available in the base Endpoints? Then we provide overloading constructors, so service doesn’t need to think too ...
- A2-1205 — Startup: How about we decouple cluster startup from onMemberUp callback \(potentially can provide 0 or more than 1 callbacks\)
- A2-1234 — InvestmentRequestTopicSubscriberV3: Should we also use `UpdateFundingInstructionsCmd` here?
- A2-1236 — InvestmentRequestTopicSubscriberV3: Looks like we need separate cmd to update fxConversionRequestId / deposit transactionId without changing status?
- A2-1244 — BrokerCashTransactionTopicSubscriberV3: What will happen to normal deposit? They will flow straight from broker → transaction, without any records in TradingAccountEntity right?...
- A2-1248 — TransactionTypes: Same here. Individual transaction should be serdes via the sealed trait `Transaction` by default. You can ref this inside the object so that we ensure it’s onl...
- A2-1249 — TransactionV3Entity: I think it’s safer to assume we only want to copy over tradeDetails from existing to new value, than to assume we only need to take new statusDetails only f...
- A2-1257 — HkGoalCreatePortfolioSummaryBehaviour: Shouldn’t this be calculated from `request.riskTolerance` instead? Also should we refactor and use the `ProductLineAndIntentHelper` ? Then...
- A2-1306 — CustomerStateUpdatedLogic: Maybe make them follow same style right?
- A2-1307 — Wrongly deleted fee-redemption recovery: first order stays deleted, second assumption restores, confirmations complete
- A2-1310 — D56 abort rejected withdrawal dividend: 187.44 switches to cash balance; 12.56 reinvestment remains unchanged
- A2-1311 — DividendTopicSubscriberV3: Added comment for the AbortCmd… from transaction pov, it doesnt need to know about the possible cases of pref here. In future, we might support for ca...
- A2-1332 — EdgeWarningAndRestrictionQueryLogic: Should we make this a method of `PlanStateValidationResult` instead? Merge the goalIds from the 3 impacted plan sets, no need to check again...
- A2-1345 — package: Many fields of same type next to each other makes this very easy to mess sth up during refactoring if we are not careful. Let’s just use this syntax instead
- A2-1402 — EmailDataFactory: Can remove “SG”
- A2-1439 — BaseServiceLogicImpl: Yes all the usage of this API mostly just check if plan exists.. and in general, if you query by not entity-id, you should expect EC regardless
- A2-1446 — package: Actually no need to split also right? This PR we will only release goal svc, all consumer of goal svc will still use old endpoints.
- A2-1461 — BaseTradingServiceLogicImpl: Should we also add internal endpoints to trigger this `UpdateCashReservationFxConversionRequestIdCmd` and `NotifyFxFundedTradeFxConversionRequestedC...
- A2-1485 — CraManager: Remove this and move its code to `submitCra`. For other simulation purpose, we can just create the `Input` from state and call `matchAdvisoryProfile` directly, no ne...
- A2-1487 — Review: Existing naming in `transaction` svc is a bit confusing \(introduced by the multiple versions of entity migration\)
- A2-1498 — InitiateCancellationFlowCmdHandler: It seems the approach taken in this cmd handler is to ignore if request has reached un-cancellable state
- A2-1499 — InitiateCancellationFlowCmdHandler: Alright let’s leave those as is for now. This exception will also hit the serdes issue, but ok we clean in separate PR.
- A2-1500 — InitiateCancellationFlowCmdHandler: Maybe update the msg here to reflect latest decision, it’s not executed but only cash reserved right?
- A2-1501 — TradingAccountEventProcessor: We should not come here cuz the cmd handler should cancel this already reserved cash in the first place?
- A2-1502 — UpdateTradeFxConversionRequestIdCmdHandler: Are you planning to use same cmd handler for future cases of `fundingInstructions`?
- A2-1510 — AcceptFxCreditSettlementCmdHandler: nits: `events ++= additionalEvts`
- A2-1523 — FundSmartHelper: As discussed, let’s try to refactor this a bit more to reduce code dups
- A2-1536 — HkEstimateAccessFeeGoalCreateBehaviour: Ah nvm me. That one is for existing plans. I guess we can refactor a bit, but yea next time
- A2-1561 — PersistentEntityRefProvider: Let’s put a scaladoc for this class, noting down all the entity names that were used in the history
- A2-1566 — TransactionJdbcProjectionV2: Let’s not mix the naming, it can be confusing for future readers:
- A2-1583 — InstrumentState: Didn’t realize we are using same model in state and db… it should be cheap enough to convert back to DTO and use all the existing methods there?
- A2-1585 — TransactionTypes: We can let the old `FxConversionDetails` having optional accounts, as we are migrating away from this v1 model.
- A2-1591 — InvestOnceCmdHandler: Just put this check as another if in the block above?
- A2-1595 — InvestOnceCmdHandler: Use the matched `fundingInstructions` instead of casting `cmd.fundingInstructions` again
- A2-1600 — RebateDistributionJdbcEventProcessor: Nit naming. We normally name these with snake case `<entity>-jdbc-evt-handler-vX` so maybe `rebate-distribution-jdbc-evt-handler-v1`?
- A2-1624 — InstrumentTable: [person] [person] let’s create tix, if not already, to completely get rid of V1 instrument repository \+ its entity later
- A2-1636 — RegionalCustomerTopicCustomer: Not possible as of now I think. I mean if any chance of mistake, at least on our side, we only touch the schedules, which are easy to reinstate. A...
- A2-1638 — RegionalCustomerTopicCustomer: Entity is keyed by goalId so would it be better to increase parallelism for goals to 4, keeping parallelism for plans at 1?
- A2-1648 — EmailDataFactory: [person] this one just need a method in `Translator` for ZonedDateTime?
- A2-1716 — package: Let me think a bit more on this. Probably we want to include both the current and previous quarter amount here. Otherwise the amount on full redemption request would be...
- A2-1717 — InitiateFeeChargeCmdHandler: No issue for charge flow. But I rmb some charge dashboard were checking if we have missing charge, hence last time we added this logic to waive prev...
- A2-1736 — Review: Not touching redemption yet as we would still allow customer to liquidate their AI-only funds \(when they are retail\) or when they are suspended \(POps does on behalf o...
- A2-1776 — AltsLcoCalculationMatrix: Feels like this and the scoreCalculator can be refactor a bit more to remove duplicate code, but ok we can iterate on this later
- A2-1780 — ServiceLogicImpl: We can already trust data from this repo, no need to go entity if repo says no annual yield
- A2-1802 — MarketDataUploader: Call annual yield here too. So you just need to upsert always. No need to link with entity/processor
- A3-0068 — InstrumentCommandsHandler.scala: We only have 2 states, None or with instrument… anyhow we already have to list of the cmd for each state, so I think can just split this get handler i
- A3-0069 — InstrumentState.scala: Updating this should be part of logic/manager and here we can just use data from DTO directly?
- A3-0070 — InstrumentCommandsHandler.scala: And I suppose the only reason we have to list all these cmd is because we need the replyTo which is not available at trait level… I guess we can live 
- A3-0074 — InstrumentDataUpdateManagerV2.scala: So how do we update from No/Partial to Full status?
- A3-0080 — InstrumentCmdDelegator.scala: So what’s the diff? Yours mean we don’t need to worry about other BaseInstrument impl until we need them? And if cmd is invoked on invalid state, e.g.
- A3-0082 — InstrumentState.scala: Generally I’d prefer to keep these methods as pure getter/setter between dto and model. But yeah we can leave this for now, it’s easy to change later,
- A3-0088 — UpdateCurrentAssetAllocationCmdHandler.scala: Need to break this method… otherwise we will have wrong reason
- A3-0090 — AcceptSuggestedRebalanceRequestCmdHandler.scala: Yeah, with new logic, it could be accepted RPC but haven’t triggered yet also. I added some comments to explain.
- A3-0091 — UpdateCurrentAssetAllocationCmdHandler.scala: this shouldn’t happen. I log error here to alert just in case.
- A3-0092 — UpdateCurrentAssetAllocationCmdHandler.scala: Same here, this should not happen based on our checks in other cmd handlers. Just logging to alert and do not proceed just in case we miss anything
- A3-0094 — Rebalance-in-progress RPC acceptance: modification cancellation versus threshold-breach race
- A3-0095 — UpdateCurrentAssetAllocationCmdHandler.scala: For RPC, goal svc will send a TAA updated msg which will trigger this cmd. However, we will skip it, cuz we change the flow to trigger both RPC/Breach
- A3-0096 — d56 RPC verification: goal modification, threshold breach, acceptance and race outcomes
- A3-0111 — package.scala: Just put this in `state/package` or even companion object of the get cmd… It’s a simple wrapper, everywhere else should continue to interact with List
- A3-0116 — RPC endpoints intentionally differ: customer readside versus goal entity consistency
- A3-0135 — ServiceLogicImpl.scala: Should we add some validations here? e.g. request is indeed for RPC and still either pendingAcceptance/rejected
- A3-0139 — RPC read-only summary may see accepted/cancelled TAA; FE-list precondition currently tolerated
- A3-0148 — MV-before-plan-topic race creates planProfile with wrong planCcy; remove early creation
- A3-0150 — Voucher wallet calculation needs full GetVoucherWalletStateCmd; entity load is bottleneck
- A3-0155 — RebalanceMsgLogicImpl.scala: Yea should be correct I think. If deletedAt is present, it is deleted
- A3-0176 — InstrumentCommands.scala: This cmd actually feels off.. we shouldn’t need to check this in ServiceLogic later, just let the other cmd handler does the check?
- A3-0177 — TypedInstrumentEventsHandler.scala: If simple enough, I think we can just put in the entity. Only those cmd handlers that have a lot of logic then we can split out to aid readability.
- A3-0191 — InvestmentTransactionV2Transformer.scala: `SUBMITTED_INTERNALLY_AND_PENDING_EXTERNAL_BROKER_SUBMISSION` should have orders already?
- A3-0192 — InvestmentTransactionV2Transformer.scala: patch will blindly copy and toV2Order will set status according to assumedAt/confirmedAt… so we will have assumed order here even if it’s still pendin
- A3-0195 — RedemptionTransactionV2Transformer.scala: Submitted internally should have orders?
- A3-0206 — CustomerTransactionMigrationEventProcessor.scala: Yea this one is purely just to capture the requestedBy/reason - which helps to explain these manual override if we have to dig in future. If we don’t 
- A3-0228 — DetectExpiringRecurringInvestmentCmdHandler.scala: Why don’t we just send the communication directly from the scheduler? I’m thinking this is really not an event for GoalEntity - no logic in cmd handle
- A3-0235 — Expiring-schedule Kafka lag/replay must not notify a replacement schedule
- A3-0244 — Idempotent command permits bounded AskTimeout retry
- A3-0257 — RecurringInvestmentScheduleJdbcEventProcessor.scala: `upsertPlanRecurringInvestmentSchedule` will skip if schedule is None? don’t we need another method to delete in dbHandler?
- A3-0263 — Schedule deactivation domain events belong in command/PlanProjection; JDBC writes only
- A3-0271 — RecurringInvestmentScheduleHelper.scala: This is a helper method. IMO we shouldn’t use State here unless we need data from it.
- A3-0277 — Schedule-update command validates persisted interval and plan/schedule existence under race
- A3-0323 — Three-MCCY-broker creation: partial success, retry and stale active-account readside
- A3-0325 — TAA has four entities/two BQ copies; remove rebalance TAA entity and janitor remaining three
- A3-0363 — RebateDistributionTopicSubscriberV2.scala: Hmm actually `RequestedAmountStatusDetails` should only be used for the initial status, e.g. `CREATED_AND_PENDING_INTERNAL_BROKER_SUBMISSION` / `PROCE
- A3-0365 — Requested-state submission statuses: remove unused external, preserve existing internal if prod data
- A3-0366 — RebateDistributionTopicSubscriberV2.scala: If we are keeping submitted-internally in Requested state, then I suppose we can let this one be in Requested state :pray:
- A3-0389 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Should we also handle `InvestmentPlanDeactivatedEvt`?
- A3-0391 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Here we use latest data of investmentPlan, so you may see a schedule created here with an already deactivated plan. Not sure but now I’m thinking if w
- A3-0398 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Actually, here you should use the `recurringInvestmentSchedule` inside the investmentPlan of the event, instead of fetching latest from entity Also, i
- A3-0402 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: `MakeRecurringInvestmentCmdHandler` set correct reason. Only `InvestOnceCmdHandler` overrides to initial investment if first one
- A3-0403 — UpdateCustomerPreferencesCmdHandler.scala: Requirement as of now yeah… but I’m asking if it even makes sense to block this if we already block at rebalance triggering side
- A3-0406 — SgServiceLogicImpl.scala: As of now, we do not support deactivating individual plans under a goal. All plans of same goal must be deactivated together. But this might change in
- A3-0407 — SgServiceLogicImpl.scala: This will return empty if goal is inactive. So maybe check that first. Or handle empty validPlans here
- A3-0428 — package.scala: I think it’s cleaner to create new cmd, mark old one deprecated. Once we switch the usage completely, it’s simple to remove the old cmd whenever we to
- A3-0445 — package.scala: AFAICS, all manual orders we support so far are all amount-based orders. I wanted to keep this request for all trades, and let the cmd handler decide 
- A3-0446 — UpdateTradeWithManualOrdersCmdHandler.scala: these basic validations I just follow existing code. It’s not clear why in some places we reply ack, reply message or reply error. Note that reply err
- A3-0447 — Empty generated orders before/after Lagom removal: log+Done with no event preserves outcome
- A3-0448 — UpdateMarketDataCmdHandler.scala: I extract the event logic for fee to separate method so if we enter here, don’t need to worry about fee anymore
- A3-0450 — PlanTraderEntityTestForSellFeeCharge.scala: No events mean state will not change right?
- A3-0451 — replyMessage uses StatusReply.error(String) to avoid Throwable serdes custom type
- A3-0452 — UpdateTradeWithManualOrdersCmdHandler.scala: I updated to replyMessage here to give immediate error to caller instead of having to check Kibana/Sentry
- A3-0453 — UpdateTradeWithManualOrdersCmdHandler.scala: I’m not changing the `UpdateMarketDataCmdHandler` side as it seems to “expect” it to happen in its info logging ``` (perhaps the events got replayed b
- A3-0458 — WithdrawalTopicSubscriber.scala: Should we go to entity if not found in readside?
- A3-0480 — package.scala: we can just move this method there, instead of state
- A3-0500 — : Don’t you need an endpoint to trigger the cmd too?
- A3-0502 — RebalancePlanEntityTest.scala: check exactly new new TAA matches what provided in cmd? Also let’s verify the emitted events contain only the TAA updated evt, and nothing else. Do yo
- A3-0505 — d56 fee-withdrawal deletion test: error-before,200-after, reservation/events/DELETED checks
- A3-0506 — : The cash balance is a bit messed up due to testing in d56, but it did try to recalculate the balance. The warning in transaction svc about missing fee
- A3-0513 — TriggerThresholdBreachedRebalanceCmdHandler.scala: No you need to extends PlayJsonSerializable for `RebalanceSvcException` `RebalanceSvcException` is a case class, so it has default apply method ``` ca
- A3-0515 — Post-Lagom API contract exception versus actor serializer; goal internal exception pattern unresolved
- A3-0524 — chargeTopic.scala: There are a few validation in the cmd handler. Essentially we should only allow backfilling if it does not affect final chargeable amount. However, th
- A3-0532 — commands.scala: Just to make sure we don’t wrongly override existing data in case the cmd is called twice, unless the force flag is set \(cuz it will be called via pr
- A3-0533 — InitiateFeeRedemptionCmdHandler.scala: this is how SG flow works today. `CHARGEABLE_FEE_FINALIZED` is not used at all
- A3-0534 — InvestmentTransferEventProcessor.scala: We need to return Future to chain it here. Otherwise, event processor won’t wait for investOnce and `NotifyInvestmentProcessInitiatedCmd` to complete 
- A3-0550 — SgPlanUpsertValidationBehaviour.scala: we don’t expect to receive portfolioId in summary step at all. The warn log in summary behaviour is just there, in case FE sends us. We validate and b
- A3-0552 — TriggerThresholdBreachedRebalanceCmdHandler.scala: We don’t really change anything to RebalancePlan here right?
- A3-0561 — AltsRedeemOnceEdgeLogic.scala: units balance is updated accordingly when orders are generated
- A3-0573 — BrokerAccountTopicSubscriberCommunicationLogic.scala: Since it’s within investment svc, should we inject refProvider and just use ``` investmentRequests <- refProvider.getPlanInvestmentManagerEntityRef(UU
- A3-0576 — Alts cashOnlyFee test:1.5M holding,10K pending,5K cash,12381.46 fee waits for funding
- A3-0577 — CashSmartUSD cashOnlyFee=false test:173.74 fee eagerly reserves cash and completes
- A3-0578 — 15K top-up funds Alts fee before earlier investment;12381.46 fee completes
- A3-0603 — FeeChargeRequestProjection.scala: If cash reservation fails, we will log this error and delete the fee charge request. We would have separate dashboard/admin screen to keep track of wh
- A3-0604 — Alts cash-reservation remote call in projection; Kafka request/result ideal lacks trading events
- A3-0613 — package.scala: Use `terminalTradeStatuses` ?
- A3-0631 — : Tested in d34. ### Invest manually with one instrument in an existing plan with 2 instruments 50-50 After investment settles, MV is updated and thresh
- A3-0632 — : Trigger the endpoint to accept all threshold breach requests And settle the rebalance trade ``` { "rebalanceRequestId": "", "status": "REBALANCING_COM
- A3-0662 — package.scala: The comment above says new txn would have `DISTRIBUTION_RECEIVED` but we are removing it?
- A3-0666 — package.scala: use `CREATED_AND_PENDING_INTERNAL_BROKER_SUBMISSION` for requested status
- A3-0672 — TransactionTypes.scala: RequestedUnitStatusDetailsDto \{ transactionStatus // required `CREATED_AND_PENDING_INTERNAL_BROKER_SUBMISSION` requestedUnits requestedAt \}
- A3-0673 — TransactionTypes.scala: PendingUnitStatusDetailsDto \{ transactionStatus // required `...` requestedUnits requestedAt \}
- A3-0674 — TransactionTypes.scala: `SettledUnitsStatusDetails`\{ transactionStatus // SETTLEMENT\_CONFIRM settledUnits settledAt settledPrice settledPriceDate \}
- A3-0675 — TransactionTypes.scala: If rejected also contains units, we can drop this field
- A3-0700 — PortfolioVersionUpgradeRebalanceRequestsGenerator.scala: Hmm looks like we need same check in auto RPC via `RebalanceCompletedEvt` too?
- A3-0704 — Historical event-handler change accepted as specific exception, supporting Jira unavailable
- A3-0706 — Missing PlanSubscriber: inactive fine, active requires manual investigation/add-back
- A3-0735 — common.conf: `silver.entity-ref.ask-timeout` to make it clear that this timeout is only used for the EntityRef?
- A3-0740 — Rebalance cash-release timing: pending-MV double-count window until buy export
- A3-0745 — HkRebalanceTopicSubscriber.scala: that makes sense. Our earmark as of now is immutable, so I’m not updating it yet. When we need to, I’ll revisit this flow :thumbsup: For now, using th
- A3-0822 — Recurring failure email: actual reason, event-domain coupling and direct-publish deferral
- A3-0856 — CustomerAdvisoryProfileCommands.scala: Cmd starts with verb… so it’s CheckExpiryCmd…
- A3-0863 — SgServiceLogicImpl.scala: Why don’t we read from entity here?
- A3-0864 — SgServiceLogicImpl.scala: Ah this is just to compare between charge entity and charge readside? I think we can skip this, cuz we will anyhow fetch from entity and write again -
- A3-0919 — CraManager.scala: Hmm this will emit `ExpiryDateOverriddenEvt` which is not what happening here… I think we will need another pair of cmd/event
- A3-0928 — CRA expiry override versus check: date-update event separate from expired-flag event
- A3-0943 — CraManager.scala: I guess no need to add “maybe” bit - it’s already part of `simulateOnly` flag? maybe just `internalSubmitCra` or something like that?
- A3-0961 — CraManager.scala: put a comment here, or even an error log that if `daysUntilExpiry` < 0… because if so, `riskProfileStatus` should have been updated to Expired
- A3-0984 — InvestmentCommunicationV2EventProcessor.scala: `SettlementAssumed` won’t have these confirmed fields…
- A3-0985 — InvestmentCommunicationV2EventProcessor.scala: confirmed fields are only populated when the status is settlement confirmed
- A3-1046 — HkServiceLogicImpl.scala: We don’t need this cuz the cmd already returns Done?
- A3-1051 — Recurring acknowledgement retained dormant; next schedule refreshes it
- A3-1109 — PlanAcknowledgementManagerEvents.scala: Cmd I guess we can merge them all in single `RemoveAcknowledgementsCmd`, but let’s not merge them in events
- A3-1112 — ModifyPlanAcknowledgementsLogic.scala: Hmm now that I see this, I want to break the request \+ cmd out too… if customer sends request to delete recurring investment schedule, we will automa
- A3-1120 — Ack compensation/recon alternative tolerates eventual correction unlike CR earmark
- A3-1133 — QueryTradingRestrictionLogic.scala: Hmm, not every plan would have persisted acks?
- A3-1134 — QueryTradingRestrictionLogic.scala: Right ok, so we lookup for all plans, and the entity has initial empty state if no acks. Should be able to lazy this, and only lookup acks if plan has
- A3-1183 — TransactionService.scala: customerId is there for old endpoint because the entity is at customer level
- A3-1187 — TransactionService.scala: We still need ability to override txn if needed in HK though
- A3-1189 — package.scala: Should be ok to drop this I think. Once order moves to confirmed state, we should no longer need to use data from assumed state.
- A3-1190 — TransactionTypes.scala: I’m not sure how we are planning to use this DTO… accepting a transactionStatus in constructor and enforce it to be exactly one value always… this loo
- A3-1191 — TransactionTypes.scala: Right, pending might have different statuses
- A3-1193 — Pending order has amount or units; settlement both; mixed lists and latest-state model
- A3-1197 — PlanAcknowledgementManagerEvents.scala: Generally, we want to capture events as facts that happened, so this should be `CraCat2AckedEvt`
- A3-1203 — PlanAcknowledgementManagerEntity.scala: I’m thinking this should be set in Cmd instead…
- A3-1213 — TradingRestrictionLogic.scala: If request is an instance of `RecurringInvestmentRestrictionRequest`, we would load the ack from persisted state, and then refresh the timestamp in th
- A3-1214 — CustomerAdvisoryProfileEntity.scala: purely just in case. Because I can’t apply the event on this state anyway
- A3-1233 — TradingRestrictionLogic.scala: Should we move this “get acks” as a method on the request itself? This looks messy
- A3-1237 — TradingRestrictionRequest.scala: Can we remove the default impl and explicitly return empty set in the Recurring request instance? I think it’s better that way, since if we add new re
- A3-1246 — TradingRestrictionLogic.scala: But then again, when customer goes thru the invest-once flow in UI, they will see the current TAA in PlanDto…. the TaaModificationEarmark should reall
- A3-1247 — Supplied TAA+ack sufficient for request; customer CR must honor TaaModificationEarmark
- A3-1251 — CustomerTradingEarmarkManagerCommands.scala: release earmark command should just require BuyEarkmarkId - and we drop exactly that earmark, without checking amount
- A3-1252 — CustomerTradingEarmarkManagerCommands.scala: add `requestedBy` too. This is useful for manual flow. In normal subscriber flow, maybe we can set requestedBy = the subscriber class itself
- A3-1253 — TradingEarmarkModificationRequest.scala: I’m thinking if we should just add DTO corresponding to BuyEarmarkId, and then have single request payload for the release request which contains buyE
- A3-1254 — TradingEarmarkModificationRequest.scala: Also, are you adding the REST endpoint for this too? If so, let’s mark it as internal
- A3-1256 — CustomerTradingEarmarkManagerCommands.scala: I was thinking we should distinguish between releasing an earmark due to full utilisation \(when the investment is submitted externally for settlement
- A3-1257 — ReleaseEarmarkSpec.scala: Should we add another assertion checking the earmark state? Otherwise, we would always get a Done as result - whether the earmark is found or not
- A3-1258 — Earmark-release e2e: simulate failure, release, simulate success
- A3-1279 — Recurring-instance acks belong to compliance persistence, not investment/trading request
- A3-1280 — TradingRestrictionRequest.scala: So when customer create goal with recurring investment, that ack needs to be sent. Compliance would check and persist that ack. When time comes for `R
- A3-1292 — BuyEarmark sameID/amount idempotency validated in command, event appends only
- A3-1293 — ConcentrationRiskValidator.scala: This duplicate pattern matching on request type seems to suggest we should break down by type earlier. Example for the simulation flow: ```scala def v
- A3-1294 — ConcentrationRiskValidator.scala: This way, for confirmation flow, the skeleton private method would accept 2 functions returning Future: * one for the investment values * another for 
- A3-1296 — CustomerTradingEarmarkManagerEntity.scala: the idea is we validate and reject in command handler, so that event handler can be dumb and just append
- A3-1298 — Same earmarkID+amount returns Done without event
- A3-1301 — CustomerTradingEarmarkManagerCommands.scala: Can we drop “Customer” here? We have “Customer” in entity name to suggest the aggregate is at customer level, but I think we don’t need it anymore in 
- A3-1302 — CustomerTradingEarmarkManagerEvents.scala: Can we also drop “Trading” here? “TradingEarmark” was intended to be general name for all the earmark types.
- A3-1303 — CustomerTradingEarmarkManagerEntity.scala: How about we refactor this a bit? Using pattern match on the find? ```scala state.buyEarmarks.find(_.id == cmd.buyEarmark.id) match { case Some(existi
- A3-1308 — CustomerTradingEarmarkEntityTest.scala: I think test is a bit clearer if we do this step 1 as state setup instead. Can use `withCustomizedEntitySetup`
- A3-1318 — CustomerTradingEarmarkManagerEntity.scala: I still want it to reject… what if caller will actually process that same command twice :grimacing: ?
- A3-1319 — BuyEarmark currentVersion then ID+amount branch matrix
- A3-1323 — TradingRestrictionResponse.scala: not leak this version I think…
- A3-1325 — CustomerTradingEarmarkManagerEvents.scala: Hmmm one action should only create one BuyEarmark I think. Only action that would trigger multiple earmark is modification of a multiple-plan goal. Bu
- A3-1326 — CustomerTradingEarmarkManagerEntity.scala: Ah I think the event should contain only the new earmark, and we append inside `handleEvents` instead of here
- A3-1329 — package.scala: Why do we need to return wrapped TransactionData?
- A3-1330 — TransactionState NotInitialized/Initialized alternative to Option
- A3-1331 — package.scala: true. But using simple Option means State might go from Some to None, whereas using named state would make people think twice before trying to change 
- A3-1333 — HkServiceLogicImpl.scala: Ah this one is internal error with “invalid state” reason is because I expect VC / Expired status to be caught outside already. So this case should ne
- A3-1337 — TransactionTypes.scala: This means `DepositBasedStatusDetailsDto` etc. must always be empty trait, and we simply use it to define the available statuses of a transaction type
- A3-1338 — TransactionTypes.scala: Any example of existing transaction types that doesn’t support a particular status?
- A3-1343 — TransactionTypes.scala: Just a thought. I may create a `RequestedAmountStatusDetailsDto` with `transactionStatus = SETTLEMENT_CONFIRMED` with this modelling? Mapping each tra
- A3-1353 — transactionTypes.scala: Just a thought, do we want to add a case class representing the status which contains amount \+ updatedAt field? Then we can get rid of these optional
- A3-1355 — transactionTypes.scala: on point \(3\), it’s not about losing data. Old data is still there in events, we just want latest snapshot in State \(ideally\). From readside point 
- A3-1372 — ServiceLogicImpl.scala: Ah yes.. `withResult`… blind me
- R-3363 — We reuse this Cmd here which does not protect us from concurrent modification in entity logic. But should be ok for now, since we do not officially support
- R-3376 — At some point, I guess we should split PlanProfile out of Entity. Local cache built from Kafka should just be updated directly, no need to maintain event t
- R-3378 — Oiii ctx.commandFailed
- R-3390 — This is pure mapper method… it won’t know. I want this endpoint to force override as well, so it won’t know anything about the context of the overridden da
- R-3391 — Override concurrency requires expected state and entity-side compare-and-set validation
- R-3392 — Updated expectedExistingTransaction/targetTransaction request and stale-state BadRequest
- R-3402 — PlanEventProcessor ServiceClient dependency moves wiring from Components to Application
- R-3456 — Is it better to leave these kind of checks to the entity? I think I prefer input validation in cmd handler \+ state validation in entity
- R-3457 — Want to include the result of `hasOnlyZeroRebateAmount` here? Or maybe split the if similar to how we check settledCcy?
- R-3481 — I have one side question. This DB handler is not tied to any event processor, so we have to call `handler.createTables` here. If there is a readside event 
- R-3506 — Take a step back, so if state has instrumentCcy, then we use it directly, and ignore the value from command. Otherwise we use from cmd This means we only r
- R-3517 — Added `Deleted` to the cases in `deleteRelatedTransaction` I see `DeleteCmd` is already handled correctly by the entity if in `Deleted` state
- R-3527 — I mark this deprecated, and will remove after we verify everything is fixed in prod. For same reason, I will reuse existing `DividendReinvestedEvt` since t
- R-3528 — No we sync only Confirmed ones. Assumed dividends \(if any\) would eventually be confirmed, and get processed by new logic
- R-3594 — As chatted, I’ll check how we can write svcImplTest with real entity \(and hopefully without too much saga about mock entity > test driver > real entity :f
- R-3604 — ServiceImplTest mocks client boundaries; EntityTest checks command, state, events and response
- R-3605 — Historical e2e exploration from ServiceImpl avoids committing to flaky EmbeddedCassandra

## Full source cases

## A1-0021 — CustomerAdvisoryProfileEntity intentionally does not update lastUpdatedTS

**Source stance:** explanation

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileEntity.scala; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> That is intended. No changes here, only added comment to explain the lack-of updating the `lastUpdatedTS`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:21 · comment 823070586 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileEntity.scala`

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

## A1-0113 — Place SgPlanAcknowledgementManagerEntity error log in command handler

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/entities/SgPlanAcknowledgementManagerEntity.scala; operation: [INV-5597] feat(advisory compliance goal instrument investment rebalance trading): add etf and car ack; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Event-handler log sends Sentry alert on every rehydration; notify only on occurrence

**Source-preserving request, proposal, or question:**

> Can we review this logic again? Error logs if any should be in cmd handler, not event handler.
> 
> We want to notify only when it happen. Currently, we get sentry alert for this log every time the entity is rehydrated.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:116 · comment 814805910 · PR 13979 · 2026-06-19

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/entities/SgPlanAcknowledgementManagerEntity.scala`

**Explicit source context (pr_title):**

> [INV-5597] feat(advisory compliance goal instrument investment rebalance trading): add etf and car ack

## A1-0433 — Deleting all plan-fee instructions conflicts with DeletePlanFeeInstructionCmd semantics

**Source stance:** open-question

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala; operation: Resolve INV-5291: Eam profile validation integrations, fix up table name; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> I’m a bit hesitant on this due to the existing logic of `DeletePlanFeeInstructionCmd`
> 
> * do not allow to delete if there’s only one instruction → we are deleting all
> * populate the endDate to be next instruction’s startDate - 1 → we are blind setting to same `effectiveEndDate`
> 
> ‌
> 
> Having said that, the logic of `effectiveEndDate` in existing code feels a bit off already
> 
> * not used anywhere - outside of entity, we only care about the start date
> * in upsert cmd
> 
>     * if new instruction is added in the middle → it will have proper end date
>     * if it is added at the end → it will not have end date, which is correct…. but by right, we should have also updated the end date of the previous instruction?
>     
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Single instruction cannot delete; endDate should follow next start minus one; current effectiveEndDate logic itself questioned including previous-instruction update.

**Evidence:** anon-1.jsonl:440 · comment 793415775 · PR 13798 · 2026-05-06

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala`

**Explicit source context (pr_title):**

> Resolve INV-5291: Eam profile validation integrations, fix up table name

## A1-0434 — Use ResetAll command/event with reset date and clear instructions

**Source stance:** suggestion

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala; operation: Resolve INV-5291: Eam profile validation integrations, fix up table name; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Avoid multiple deleted events

**Source-preserving request, proposal, or question:**

> I’m thinking if it’s better to rename this cmd & event to “ResetAll” or sth along that line. The event would only have reset date, and its event handler will simply change the instructions to empty, instead of emitting multiple deleted events

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:441 · comment 793446614 · PR 13798 · 2026-05-06

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala`

**Explicit source context (pr_title):**

> Resolve INV-5291: Eam profile validation integrations, fix up table name

## A1-0474 — Operation belongs in entity

**Source stance:** requested-change

**Context:**

> component: report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/cache/InstrumentDataProvider.scala; operation: [INV-5505] initial commit for statement v3; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This one goes to entity

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:481 · comment 791769875 · PR 13705 · 2026-05-04

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/cache/InstrumentDataProvider.scala`

**Explicit source context (pr_title):**

> [INV-5505] initial commit for statement v3

**Evidence:** anon-1.jsonl:481 · comment 791769875 · PR 13705 · 2026-05-04

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/cache/InstrumentDataProvider.scala`

**Explicit source context (hunk):**

> +        allLoader = Some(fetchInstruments)
> +      )
> +
> +  private def fetchInstruments(instrumentIds: Iterable[String]): Future[Map[String, InstrumentCacheData]] =
> +    instrumentService
> +      .getInstrumentByIds(instrumentIds.mkString(","))
> +      .map(_.map(dto => dto.id -> toInstrumentCacheData(dto)).toMap)
> +
> +  private def toInstrumentCacheData(dto: InstrumentInfoDto): InstrumentCacheData =

## A1-0769 — Manual cancellation gets encapsulation command; system cancellation uses existing no-encapsulation

**Source stance:** suggestion

**Context:**

> component: investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/DetectExpiredInvestmentRequestProcessor.scala; operation: Feat/INV-5010 multi system rrt; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Preserves customer-action-only theme

**Source-preserving request, proposal, or question:**

> Maybe consider adding `InitiateManualCancellationFlowCmd` that is encapsulation cmd.
> 
> Let existing cmd be no-encapsulation, and use that for system triggered cancellation.
> 
> This way we are consistent with customer-action-only theme

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:781 · comment 738495318 · PR 13145 · 2026-01-14

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/DetectExpiredInvestmentRequestProcessor.scala`

**Explicit source context (pr_title):**

> Feat/INV-5010 multi system rrt

## A1-0790 — Use InvestmentRrtCommandContext with rrtContext None instead of SystemTriggeredCommand

**Source stance:** suggestion

**Context:**

> component: investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/PlanTopicSubscriber.scala; operation: Feat/INV-5010 multi system rrt; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Customer acted so retain RRT entry, exclude from recently-updated-investment filter

**Source-preserving request, proposal, or question:**

> Doesnt feel right to use `SystemTriggeredCommand` here. Maybe `InvestmentRrtCommandContext` but with `rrtContext = None`?
> 
> This way we still have rrt entry for it \(because customer did sth\), but it won’t satisfy the filter condition of “recently updated investments”

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:802 · comment 744755283 · PR 13145 · 2026-01-27

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/PlanTopicSubscriber.scala`

**Explicit source context (pr_title):**

> Feat/INV-5010 multi system rrt

## A1-0823 — Financial SIP patch needs event identity or remark distinguishing system patch from reanswer

**Source stance:** suggestion

**Context:**

> component: customer-impl/src/main/scala/com/endowus/silver/customer/impl/customer/handlers/impls/PatchFinancialSIPQuestionsCmdHandler.scala; operation: feat(PG-1759): Add patch endpoint for financial SIP questions; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Latest timestamp in same event hides history

**Source-preserving request, proposal, or question:**

> I think PM already discussed in the incident channel that it’s ok to resend the trading restriction comms, if any.
> 
> Just some thoughts on this patch event,
> 
> * We are using the same event with latest timestamp here. That means a few months from now, if someone looks at the customer entity inspect, it would be pretty tough to know if this was a re-answer by customer, or it was a system patch.
> * I’m wondering if we should still go with a new event type, or at minimum with some optional remark field just to capture the Jira for context of this patch.
> * We might also consider taking the previous `updatedAt` as input and use it here, so that it can be considered as a “pure revert”. This might add a side benefit of not resending comms too \(since communication id would be the same\), if customer doesn’t have any schedule changes compared to their last failure, but we have established that we don’t have to worry about this.
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Could reuse previous updatedAt as pure revert and communication-ID dedup; resend already acceptable.

**Evidence:** anon-1.jsonl:835 · comment 744273143 · PR 13270 · 2026-01-26

Source path: `customer-impl/src/main/scala/com/endowus/silver/customer/impl/customer/handlers/impls/PatchFinancialSIPQuestionsCmdHandler.scala`

**Explicit source context (pr_title):**

> feat(PG-1759): Add patch endpoint for financial SIP questions

## A1-0824 — Events must preserve what happened beyond temporary logs Jira and sheets

**Source stance:** explanation

**Context:**

> component: customer-impl/src/main/scala/com/endowus/silver/customer/impl/customer/handlers/impls/PatchFinancialSIPQuestionsCmdHandler.scala; operation: feat(PG-1759): Add patch endpoint for financial SIP questions; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> There’s only one thing in our system that will stand the test of time, events. It’s much better to capture what-happened in events, than logs/jira/gsheet. This is the whole point of event sourcing.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:836 · comment 744275087 · PR 13270 · 2026-01-26

Source path: `customer-impl/src/main/scala/com/endowus/silver/customer/impl/customer/handlers/impls/PatchFinancialSIPQuestionsCmdHandler.scala`

**Explicit source context (pr_title):**

> feat(PG-1759): Add patch endpoint for financial SIP questions

## A1-0992 — Update only acknowledgement keys matching scheduleId rather than replace all

**Source stance:** suggestion

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/entities/SgPlanAcknowledgementManagerEntity.scala; operation: [INV-5045] feat(compliance): implement state changes for sip ack; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> I think to be on safe side, we should only update for keys with matching scheduleId instead of replacing all

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1008 · comment 728905335 · PR 13004 · 2025-12-18

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/entities/SgPlanAcknowledgementManagerEntity.scala`

**Explicit source context (pr_title):**

> [INV-5045] feat(compliance): implement state changes for sip ack

## A1-1025 — Capture all acknowledgements together to avoid overriding

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/SgTradingRestrictionLogicImpl.scala; operation: [INV-5014] feat(compliance): implement trading restriction for all the actions; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We need to capture all the acks tgt, otherwise it will override each other

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1041 · comment 720729541 · PR 12948 · 2025-12-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/SgTradingRestrictionLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-5014] feat(compliance): implement trading restriction for all the actions

**Evidence:** anon-1.jsonl:1041 · comment 720729541 · PR 12948 · 2025-12-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/SgTradingRestrictionLogicImpl.scala`

**Explicit source context (hunk):**

> +
> +  private def checkCustomerUnsuitableForSipAckRestrictions(
> +    resolverConfigsByPlanId: Map[UUID, TradingRestrictionResolverConfig],
> +  ): SgCustomerDto => Future[TradingRestrictionCheckResult] = { customer: SgCustomerDto =>
> +    checkPlanAcknowledgmentRestrictions(
> +      resolverConfigsByPlanId,
> +      planAckRestrictionLogic = (planId, resolverConfig) =>
> +        computeUnsuitableForSipRestrictionCheckResult(
> +          planId = planId,

## A1-1028 — Separate threshold-breach acknowledgements from recurring investment schedule acknowledgements

**Source stance:** open-question

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/SgTradingRestrictionLogicImpl.scala; operation: [INV-5014] feat(compliance): implement trading restriction for all the actions; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** RPC may need own persistence later

**Source-preserving request, proposal, or question:**

> Doesn’t look right that we use `recurringInvestmentScheduleAcks` for both RecurringInvestment / ThresholdBreachedRebalance. Do we need separate acks persisted for ThresholdBreachedRebalance and maybe RPC later?
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1044 · comment 720730471 · PR 12948 · 2025-12-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/SgTradingRestrictionLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-5014] feat(compliance): implement trading restriction for all the actions

## A1-1136 — Use parallelism one for commands to same entity

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala; operation: [INV-5017] feat(compliance): implement ack, warnings block and trading restriction apis; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Entity cannot execute commands in parallel

**Source-preserving request, proposal, or question:**

> Use parallelism = 1 here since we are accessing same entity, the cmd can’t be parallelized anyway

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1153 · comment 724004432 · PR 13025 · 2025-12-08

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-5017] feat(compliance): implement ack, warnings block and trading restriction apis

## A1-1194 — PlanAcknowledgementState keys recurring transfer acknowledgements by sourcePlanId

**Source stance:** suggestion

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/planAcks/entities/ces/PlanAcknowledgementState.scala; operation: [INV-5047] feat(compliance): create entity for customer acks; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Actually on 2nd thought, we can’t keep track of acks in State by relying on actionContext:
> 
> * Both get/removal use case would be per recurring investment/transfer, but regardless of which actionContext triggers the acks \(either during schedule creation / update / posthoc\)
> * For removal, we might be able to map for all possible combination, but it doesn’t make sense for get
> 
> ‌
> 
> Maybe we should go with explicit acks per recurring schedules
> 
> ```scala
> case class PlanAcknowledgementState(
>   recurringInvestmentScheduleAcks: Set[PlanAcknowledgement],
>   recurringTransferScheduleAcks: Map[SourcePlanId, Set[PlanAcknowledgement]]
> )
> ```
> 
> * Note we key using sourcePlanId for the recurring schedules. If scheduleId changes, we still override at sourcePlanId level.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Replace on capture, derive specific removals in cmd, preserve unrelated acks in evt, top up on separate Add cmd; transfer keyed by sourcePlanId despite scheduleId changes.
- Selected source excerpts preserve this specific case; incidental identities and repetitive logs are omitted. This record does not claim an unreported implementation outcome.

**Evidence:** anon-1.jsonl:1211 · comment 718849319 · PR 12925 · 2025-11-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/planAcks/entities/ces/PlanAcknowledgementState.scala`

**Explicit source context (pr_title):**

> [INV-5047] feat(compliance): create entity for customer acks

## A1-1195 — CapturePlanAcknowledgments replaces the complete matching schedule acknowledgement set

**Source stance:** suggestion

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/planAcks/entities/ces/PlanAcknowledgementState.scala; operation: [INV-5047] feat(compliance): create entity for customer acks; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> * For `CapturePlanAcknowledgmentsCmd(actionContext, acks)` flow:
> 
>     * we keep event as is `PlanAcknowledgmentsCapturedEvt(actionContext, acks)`
>     * in event handler
>     
>         * again we have mapper logic from `actionContext` to update the State accordingly, if required
>         * the new acks should replace the existing set completely

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Replace on capture, derive specific removals in cmd, preserve unrelated acks in evt, top up on separate Add cmd; transfer keyed by sourcePlanId despite scheduleId changes.
- Selected source excerpts preserve this specific case; incidental identities and repetitive logs are omitted. This record does not claim an unreported implementation outcome.

**Evidence:** anon-1.jsonl:1211 · comment 718849319 · PR 12925 · 2025-11-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/planAcks/entities/ces/PlanAcknowledgementState.scala`

**Explicit source context (pr_title):**

> [INV-5047] feat(compliance): create entity for customer acks

## A1-1196 — RemovePlanAcknowledgmentCmd derives removals and preserves unrelated acknowledgement state

**Source stance:** suggestion

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/planAcks/entities/ces/PlanAcknowledgementState.scala; operation: [INV-5047] feat(compliance): create entity for customer acks; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> * For `RemovePlanAcknowledgmentCmd(ackRemovalContext)` flow:
> 
>     * in cmd handler
>     
>         * the caller should only provide the removal context, and cmd handler would derive which persisted ack\(s\) to remove, e.g. AI status / SIP result upgrade would remove only SIP ack, but schedule removal should remove all acks
>         * hence the removal event\(s\) can’t be generic as we design before, it would have to follow the State fields, e.g. `PlanAcknowledgementRemovedEvt(ackRemovalContext, removedRecurringInvestmentScheduleAcks, removedRecurringTransferScheduleAcks)` 
>         
>     * in event handler
>     
>         * update the State accordingly, should only remove the matching ack while keeping others intact

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Replace on capture, derive specific removals in cmd, preserve unrelated acks in evt, top up on separate Add cmd; transfer keyed by sourcePlanId despite scheduleId changes.
- Selected source excerpts preserve this specific case; incidental identities and repetitive logs are omitted. This record does not claim an unreported implementation outcome.

**Evidence:** anon-1.jsonl:1211 · comment 718849319 · PR 12925 · 2025-11-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/planAcks/entities/ces/PlanAcknowledgementState.scala`

**Explicit source context (pr_title):**

> [INV-5047] feat(compliance): create entity for customer acks

## A1-1197 — AddPlanAcknowledgmentsCmd tops up posthoc acknowledgement without replacing existing set

**Source stance:** suggestion

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/planAcks/entities/ces/PlanAcknowledgementState.scala; operation: [INV-5047] feat(compliance): create entity for customer acks; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> * For additional ack flow, we need new cmd, e.g. `AddPlanAcknowledgmentsCmd(actionContext, ack)`
> 
>     * new event `PlanAcknowledgmentsAddedEvt(actionContext, ack)`
>     * in event handler
>     
>         * unlike the capture flow, we want to top up the ack, not replacing the existing set
>         
>     
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Replace on capture, derive specific removals in cmd, preserve unrelated acks in evt, top up on separate Add cmd; transfer keyed by sourcePlanId despite scheduleId changes.
- Selected source excerpts preserve this specific case; incidental identities and repetitive logs are omitted. This record does not claim an unreported implementation outcome.

**Evidence:** anon-1.jsonl:1211 · comment 718849319 · PR 12925 · 2025-11-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/planAcks/entities/ces/PlanAcknowledgementState.scala`

**Explicit source context (pr_title):**

> [INV-5047] feat(compliance): create entity for customer acks

## A1-1203 — Initialize plan acknowledgement entity

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/ComplianceApplication.scala; operation: [INV-5047] feat(compliance): create entity for customer acks; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Need to init the entity here

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1217 · comment 719255641 · PR 12925 · 2025-11-28

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/ComplianceApplication.scala`

**Explicit source context (pr_title):**

> [INV-5047] feat(compliance): create entity for customer acks

## A1-1204 — Register plan acknowledgement entity

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/ComplianceApplication.scala; operation: [INV-5047] feat(compliance): create entity for customer acks; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Need to register the entity here

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1218 · comment 719255787 · PR 12925 · 2025-11-28

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/ComplianceApplication.scala`

**Explicit source context (pr_title):**

> [INV-5047] feat(compliance): create entity for customer acks

## A1-1211 — Replace acks by acknowledgement identity rather than Set entry

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/entities/SgPlanAcknowledgementManagerEntity.scala; operation: [INV-5047] feat(compliance): create entity for customer acks; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Timestamp differences prevent equality-based replacement

**Source-preserving request, proposal, or question:**

> We need to replace by checking ack, can’t rely on Set\[Entry\] since timestamp is different

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1225 · comment 719947542 · PR 12925 · 2025-12-01

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/entities/SgPlanAcknowledgementManagerEntity.scala`

**Explicit source context (pr_title):**

> [INV-5047] feat(compliance): create entity for customer acks

**Evidence:** anon-1.jsonl:1225 · comment 719947542 · PR 12925 · 2025-12-01

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/entities/SgPlanAcknowledgementManagerEntity.scala`

**Explicit source context (hunk):**

> +
> +    case (evt: PlanAcknowledgmentsAddedEvt, state) =>
> +      evt.actionContext match {
> +        case PosthocRecurringInvestmentSchedule =>
> +          val updatedAcks = state.recurringInvestmentScheduleAcks + PlanAcknowledgementEntry(evt.ack, evt.ackTime)
> +          state.copy(recurringInvestmentScheduleAcks = updatedAcks)
> +        case PosthocRecurringTransferSchedule(_, scheduleId) =>
> +          val currentAcks = state.recurringTransferScheduleAcksByScheduleId.getOrElse(scheduleId, Set.empty)
> +          val updatedAcks = currentAcks + PlanAcknowledgementEntry(evt.ack, evt.ackTime)

## A1-1212 — Posthoc action should update schedule-state acks rather than persist as own state context

**Source stance:** open-question

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/entities/SgPlanAcknowledgementManagerEntity.scala; operation: [INV-5047] feat(compliance): create entity for customer acks; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** GoalCreation/PlanCreation need more data than case objects

**Source-preserving request, proposal, or question:**

> Hmmm we don’t expect the posthoc actions to be here right? We want to store in state for the schedule creation/update action instead?
> 
> I think we need more data fields just the case object GoalCreation/PlanCreation actionContext

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1226 · comment 719946215 · PR 12925 · 2025-12-01

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/entities/SgPlanAcknowledgementManagerEntity.scala`

**Explicit source context (pr_title):**

> [INV-5047] feat(compliance): create entity for customer acks

## A1-1214 — Removal result must return being-removed acks rather than remaining

**Source stance:** open-question

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/entities/SgPlanAcknowledgementManagerEntity.scala; operation: [INV-5047] feat(compliance): create entity for customer acks; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Is this wrong? We want to returned the being-removed acks, not the remaining?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1228 · comment 720714816 · PR 12925 · 2025-12-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/entities/SgPlanAcknowledgementManagerEntity.scala`

**Explicit source context (pr_title):**

> [INV-5047] feat(compliance): create entity for customer acks

**Evidence:** anon-1.jsonl:1228 · comment 720714816 · PR 12925 · 2025-12-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/entities/SgPlanAcknowledgementManagerEntity.scala`

**Explicit source context (hunk):**

> +    ackRemovalTime: Instant,
> +    state: PlanAcknowledgementState,
> +  ): Map[UUID, Set[PlanAcknowledgementEntry]] = ackRemovalContext match {
> +    case CustomerInvestorStatusUpgradedFromRetailToAi | CustomerSipQuestionnairePassed =>
> +      state.recurringTransferScheduleAcksByScheduleId.view
> +        .mapValues(ackEntries => ackEntries.filter(ackEntry => ackEntry.ackTime.isBefore(ackRemovalTime) && ackEntry.ack == UnsuitableForSipAck))
> +        .filter(_._2.nonEmpty)
> +        .toMap
> +    case PlanRecurringTransferScheduleRemoved(_, scheduleId) =>

## A1-1215 — Persist removal event only after checking removed results nonempty

**Source stance:** suggestion

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/entities/SgPlanAcknowledgementManagerEntity.scala; operation: [INV-5047] feat(compliance): create entity for customer acks; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Maybe check if both the results are non-empty before persisting the removedEvt?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1229 · comment 720712448 · PR 12925 · 2025-12-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/entities/SgPlanAcknowledgementManagerEntity.scala`

**Explicit source context (pr_title):**

> [INV-5047] feat(compliance): create entity for customer acks

**Evidence:** anon-1.jsonl:1229 · comment 720712448 · PR 12925 · 2025-12-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/entities/SgPlanAcknowledgementManagerEntity.scala`

**Explicit source context (hunk):**

> +        ackRemovalTime = cmd.ackRemovalTime,
> +        state = state
> +      )
> +      if (acknowledgementsToBeRemovedForRecurringInvestment.nonEmpty || acknowledgementsToBeRemovedForRecurringTransfer.nonEmpty) {
> +        Effect
> +          .persist(
> +            PlanAcknowledgmentRemovedEvt(
> +              ackRemovalContext = cmd.ackRemovalContext,
> +              removedRecurringInvestmentScheduleAcks = acknowledgementsToBeRemovedForRecurringInvestment,

## A1-1270 — Trade deletion before external export already nonterminal; force transition may unnecessary

**Source stance:** open-question

**Context:**

> component: transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala; operation: [INV-4972] feat(transaction): Remove force update on intermediate and terminal status; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> If deleted when reinvestment/withdrawal is not exported, wouldn’t the existing txn status be `SUBMITTED_INTERNALLY_AND_PENDING_EXTERNAL_BROKER_SUBMISSION` - which is not terminal status, the entity won’t block the transition right? Why do we need to force?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1285 · comment 716093297 · PR 12870 · 2025-11-20

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> [INV-4972] feat(transaction): Remove force update on intermediate and terminal status

## A1-1464 — DeleteFeeChargeRequestCmdHandler acknowledgements refusal can leave undeleted charge

**Source stance:** observed-defect

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/BaseServiceLogicImpl.scala; operation: [INV-4562] feat(charge, redemption, trading): Automate fee handling; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Need thrown/handled failure or replacement may waive

**Source-preserving request, proposal, or question:**

> `DeleteFeeChargeRequestCmdHandler` logic is like this
> 
> ```scala
> if (!cmd.forceDelete.contains(true) && !deletableStatusSet.contains(existingFeeCharge.status)) {
>   logger.error(s"FeeManagerEntity [$entityId] cannot be deleted because it is in the [${existingFeeCharge.status}] status. Retry with force if intended.")
>   return Effect.ack(cmd.replyTo)
> }
> ```
> 
> ‌
> 
> I think we need to throw and handle properly, otherwise this won’t get deleted and the replaced charge will be waived?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1481 · comment 697468661 · PR 12500 · 2025-10-09

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-4562] feat(charge, redemption, trading): Automate fee handling

## A1-1653 — Typed top-level ActorSystem failed with Lagom ScaladslKafkaSubscriber

**Source stance:** reported-verification

**Context:**

> component: silver-commons/src/main/scala/com/endowus/silver/commons/kamon/KamonInit.scala; operation: [INV-4466] feat(common): Front load heavy application init before joining Cluster; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Classic actorOf throws UnsupportedOperationException with custom guardian

**Source-preserving request, proposal, or question:**

> Ah I was hopeful thinking I can remove the class TopActorSystem, and create typed one right away, since we can access the classicSystem from typed. Hence this KamonInitApp would be obsolete, and can be removed.
> 
> ‌
> 
> But I tested just now, and it doesn’t work :rofl:  The comment left by Scalac team is indeed legit
> 
> ```
> // TODO: remove transition to typed after migration of Lagom Kafka clients
> ```
> 
> Because the Lagom `ScaladslKafkaSubscriber` uses classic `system.actorOf`. This would throw the `UnsupportedOperationException` if the classic system was not as “top level”
> 
> ```
>   def actorOf(props: Props, name: String): ActorRef =
>     if (guardianProps.isEmpty) guardian.underlying.attachChild(props, name, systemService = false)
>     else
>       throw new UnsupportedOperationException(
>         s"cannot create top-level actor [$name] from the outside on ActorSystem with custom user guardian")
> ```
> 
> ‌
> […incidental material or intervening source omitted…]
> should be finishing with Lagom client removal for silver-server soon. I’ll come back to this bit later. Have reverted back the changes for now

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Reverted; TopActorSystem removal waits for Lagom Kafka clients migration.

**Evidence:** anon-1.jsonl:1669 · comment 646309866 · PR 12081 · 2025-06-18

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kamon/KamonInit.scala`

> Ah I was hopeful thinking I can remove the class TopActorSystem, and create typed one right away, since we can access the classicSystem from typed. Hence this KamonInitApp would be obsolete, and can be removed.
> 
> ‌
> 
> But I tested just now, and it doesn’t work :rofl:  The comment left by Scalac team is indeed legit
> 
> ```
> // TODO: remove transition to typed after migration of Lagom Kafka clients
> ```
> 
> Because the Lagom `ScaladslKafkaSubscriber` uses classic `system.actorOf`. This would throw the `UnsupportedOperationException` if the classic system was not as “top level”
> 
> ```
>   def actorOf(props: Props, name: String): ActorRef =
>     if (guardianProps.isEmpty) guardian.underlying.attachChild(props, name, systemService = false)
>     else
>       throw new UnsupportedOperationException(
>         s"cannot create top-level actor [$name] from the outside on ActorSystem with custom user guardian")
> ```
> 
> ‌

**Explicit source context (pr_title):**

> [INV-4466] feat(common): Front load heavy application init before joining Cluster

**Evidence:** anon-1.jsonl:1669 · comment 646309866 · PR 12081 · 2025-06-18

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/kamon/KamonInit.scala`

> should be finishing with Lagom client removal for silver-server soon. I’ll come back to this bit later. Have reverted back the changes for now

## A1-1707 — If delete cmd carries instrumentCcy validate matches state

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataEventProcessorForMultiCcy.scala; operation: [INV-4723] feat(marketdata): create delete api for daily prices; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Ok I guess you have `instrumentCcy` in the cmd & event is to support this condition. If so, then let’s put the same validation as other cmd
> 
> ```scala
> if (state.instrumentCcy.exists(_ != cmd.instrumentCcy)) {
>   return Effect.invalidCommand(cmd.replyTo)(
>     s"Instrument Ccy in state [${state.instrumentCcy}] is not matching with ${cmd.getClass.getSimpleName} [${cmd.instrumentCcy}]"
>   )
> }
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1725 · comment 680270913 · PR 12527 · 2025-09-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataEventProcessorForMultiCcy.scala`

**Explicit source context (pr_title):**

> [INV-4723] feat(marketdata): create delete api for daily prices

## A1-1710 — Add same state-versus-command instrument currency validation here

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/InstrumentMarketDataEntity.scala; operation: [INV-4723] feat(marketdata): create delete api for daily prices; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s add this instrument ccy validation
> 
> ```scala
> if (state.instrumentCcy.exists(_ != cmd.instrumentCcy)) {
>   return Effect.invalidCommand(cmd.replyTo)(
>     s"Instrument Ccy in state [${state.instrumentCcy}] is not matching with ${cmd.getClass.getSimpleName} [${cmd.instrumentCcy}]"
>   )
> }
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1728 · comment 682595933 · PR 12527 · 2025-09-12

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/InstrumentMarketDataEntity.scala`

**Explicit source context (pr_title):**

> [INV-4723] feat(marketdata): create delete api for daily prices

## A1-1720 — Do not send expired comms merely after successful remove command

**Source stance:** observed-defect

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringTransferScheduleManager.scala; operation: Resolve INV-4304: Add logic to trigger comms for inter-goal transfers; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Stale invalid schedule command may acknowledge without removal

**Source-preserving request, proposal, or question:**

> This chained future is not safe right? If the trigger is stale with invalid schedule, `RemovePlanRecurringTransferScheduleCmd`  will return success and we would still proceed to trigger expired comms.
> 
> I think safest is still do 2 steps. Only trigger cmd here - which may or may not remove the schedule, as per its validation. But if removed, we send comms in projection.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Send only from removal-event projection.

**Evidence:** anon-1.jsonl:1738 · comment 675853462 · PR 12010 · 2025-08-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringTransferScheduleManager.scala`

**Explicit source context (pr_title):**

> Resolve INV-4304: Add logic to trigger comms for inter-goal transfers

## A1-1739 — Notify failure and update next date in same command handler

**Source stance:** suggestion

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/investmentTransfer/processors/InvestmentTransferEventProcessor.scala; operation: [INV-4302] feat(advisory, goal, trading, projection): inter-goal transfer v2 base; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> While it’s good to have separate cmd to update next upcoming date, I’m thinking it would be better here if we perform both notify failure and update next date in same cmd handler

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1757 · comment 639853214 · PR 11795 · 2025-06-02

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/investmentTransfer/processors/InvestmentTransferEventProcessor.scala`

**Explicit source context (pr_title):**

> [INV-4302] feat(advisory, goal, trading, projection): inter-goal transfer v2 base

## A1-1740 — Recurring-transfer nextUpcomingDate rollout needs complete population and every-trigger advance

**Source stance:** open-question

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/investmentTransfer/handlers/schedule/TriggerRecurringInvestmentTransfersCmdHandler.scala; operation: [INV-4302] feat(advisory, goal, trading, projection): inter-goal transfer v2 base; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> I’m a bit confused about the sequence. If I understand correctly:
> 
> * existing schedules do not have `nextUpcomingDate`, and the processor would send `TriggerRecurringInvestmentTransferCmd` for all entities \(customer \+ trading account\)
> * current impl in this PR would:
> 
>     * if not meant to be triggered yet, only emit `NextUpcomingInterGoalTransferDateUpdatedEvt`
>     * if meant to be trigger, only emit `RecurringInvestmentTransferRequestedEvt` or `UpcomingInvestmentTransferScheduleDetectedEvt`, but `nextUpcomingDate` is not updated
>     
> * in the projection, if `RecurringInvestmentTransferRequestedEvt` but failed validation, then trigger `UpdateNextUpcomingInterGoalTransferDateCmd`
> 
> ‌
> 
> What this means, after we release this change on day T:
> 
> * schedules that’s not supposed to trigger on T will have `nextUpcomingDate` populated
> * schedules that’s supposed to trigger sth on T \(either transfer or reminder\) will NOT have `nextUpcomingDate` populated, unless their actual transfer validation fails
> * let this run for a few days \(I guess at least 2 days?\) then we would have `nextUpcomingDate` for all?
> * then we refactor this `TriggerRecurringInvestmentTransfersCmdHandler` to honour `nextUpcomingDate` instead
> 
> Is there any chance of race condition, if schedule is updated \+ triggered on same date, then its `nextUpcomingDate` won’t be updated to next date?
> 
> ‌
> 
> How about this?
> 
> * if `nextUpcomingDate` is populated, follow it \(\*\), otherwise, logger error and don’t do anything
> * after we release, trigger a script to mass populate `nextUpcomingDate` for all existing schedules - as long as we complete this before the next day’s cronjob, we’re good
> * we can even version the `TriggerRecurringInvestmentTransferCmd` and the cronjob’s endpoint if we need more time, and only switch to new cmd after all data has been populated
> 
> Regarding \(\*\) above,
> 
> * current impl only move it to next date if validation fails, but don’t we need to move always after every trigger, regardless of passed or failed validation?
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Source traces day-T gaps and asks mass backfill before cron or versioned cmd/endpoint; later1760 notes update in request handler already.

**Evidence:** anon-1.jsonl:1759 · comment 639861521 · PR 11795 · 2025-06-02

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/investmentTransfer/handlers/schedule/TriggerRecurringInvestmentTransfersCmdHandler.scala`

**Explicit source context (pr_title):**

> [INV-4302] feat(advisory, goal, trading, projection): inter-goal transfer v2 base

## A1-1741 — RequestInvestmentTransferWithRedemptionCmdHandler also advances nextUpcomingDate

**Source stance:** explanation

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/investmentTransfer/handlers/schedule/TriggerRecurringInvestmentTransfersCmdHandler.scala; operation: [INV-4302] feat(advisory, goal, trading, projection): inter-goal transfer v2 base; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Still considers moving advance directly into trigger handler before eventual projection

**Source-preserving request, proposal, or question:**

> ok
> […incidental material or intervening source omitted…]
> pointed out that we also update `nextUpcomingDate` in `RequestInvestmentTransferWithRedemptionCmdHandler`, so at least current impl won’t have any issues.
> 
> I’m thinking do we want to delay this update after successful/failed trigger? Or should we just update it right in this `TriggerRecurringInvestmentTransfersCmdHandler`. The `RecurringInvestmentTransferRequestedEvt` will be handled eventually in projection anyway.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1760 · comment 640286052 · PR 11795 · 2025-06-03

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/investmentTransfer/handlers/schedule/TriggerRecurringInvestmentTransfersCmdHandler.scala`

> ok

**Explicit source context (pr_title):**

> [INV-4302] feat(advisory, goal, trading, projection): inter-goal transfer v2 base

**Evidence:** anon-1.jsonl:1760 · comment 640286052 · PR 11795 · 2025-06-03

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/investmentTransfer/handlers/schedule/TriggerRecurringInvestmentTransfersCmdHandler.scala`

> pointed out that we also update `nextUpcomingDate` in `RequestInvestmentTransferWithRedemptionCmdHandler`, so at least current impl won’t have any issues.
> 
> I’m thinking do we want to delay this update after successful/failed trigger? Or should we just update it right in this `TriggerRecurringInvestmentTransfersCmdHandler`. The `RecurringInvestmentTransferRequestedEvt` will be handled eventually in projection anyway.

## A1-1809 — CustomerEmployeeEmailV2 producer already wired and eagerly creates topic

**Source stance:** explanation

**Context:**

> component: communication-impl/src/main/scala/com/endowus/silver/communication/impl/CommunicationApplication.scala; operation: [INV-4417] feat(common): Akka Cluster startup sequence; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Yea it’s already wired a few lines above F338-T348
> 
> ```
> lazy val customerEmployeeEmailV2TopicProducer = wire[CustomerEmployeeEmailV2TopicProducer]
> ```
> 
> ‌
> 
> and `createTopic` is called as val in the class
> 
> ```
> private val topic = createTopic
> 
> def createTopic = new TypedTopicProducer[CustomerEmployeeEmailRequestMsgV2](Topic)
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1828 · comment 637693092 · PR 11901 · 2025-05-27

Source path: `communication-impl/src/main/scala/com/endowus/silver/communication/impl/CommunicationApplication.scala`

**Explicit source context (pr_title):**

> [INV-4417] feat(common): Akka Cluster startup sequence

## A1-1871 — Deprecate old events but retain no-op state handlers

**Source stance:** requested-change

**Context:**

> component: portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/entities/portfolio/ModelPortfolioEntity.scala; operation: [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s mark these events deprecated, but we will need to provide evt handler for them. Just that we return the state as in in those handlers

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1891 · comment 632602018 · PR 11812 · 2025-05-14

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/entities/portfolio/ModelPortfolioEntity.scala`

**Explicit source context (pr_title):**

> [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio

## A1-1909 — Bulk price command overrides whole state: merge combinedPrices with manual prices

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; operation: [INV-4569] feat(marketdata): support source of price update; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Filtering or history-only merge loses data

**Source-preserving request, proposal, or question:**

> The `UpdateDailyPricesInBulkCmd` will just override the whole data completely I think, so here we need to merge, not filter. Also we should merge the `combinedPrices` with manual prices, not just `historyDailyPrices` alone

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1929 · comment 664716149 · PR 12355 · 2025-08-01

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-4569] feat(marketdata): support source of price update

## A1-2008 — Retain still-needed entity in this PR; eventual removal separate

**Source stance:** explanation

**Context:**

> component: rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/RebalancePlanEventProcessor.scala; operation: [INV-1946] feat(rebalance): remove taa entity; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We still need this right? This entity should also be remove one day, but it’s another day, we still need it in this PR

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2027 · comment 657149974 · PR 12157 · 2025-07-15

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/processors/RebalancePlanEventProcessor.scala`

**Explicit source context (pr_title):**

> [INV-1946] feat(rebalance): remove taa entity

## A1-2040 — Fee command duplicate initiatingFullRedemptionRequestId check makes topic handling idempotent

**Source stance:** explanation

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/RedemptionTopicSubscriber.scala; operation: [INV-4265] feat(charge): Full redemption charge fixes; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Yea, same as any other msg handler in TopicSubscriber. The cmd handler already has checks for duplicated `initiatingFullRedemptionRequestId`, so it should be idempotent as well

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2060 · comment 621188121 · PR 11639 · 2025-04-17

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/RedemptionTopicSubscriber.scala`

**Explicit source context (pr_title):**

> [INV-4265] feat(charge): Full redemption charge fixes

## A1-2157 — Approval operation state change needs revisit

**Source stance:** open-question

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgPlanUpsertPortfolioSummaryBehaviour.scala; operation: [INV-3426] feat(bff, workflowengine, advisory, goal, investment): Create subsequent investment for existing goal; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> There’s state change involved here. To revisit

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2174 · comment 582801599 · PR 10480 · 2025-01-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgPlanUpsertPortfolioSummaryBehaviour.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, workflowengine, advisory, goal, investment): Create subsequent investment for existing goal

**Evidence:** anon-1.jsonl:2174 · comment 582801599 · PR 10480 · 2025-01-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgPlanUpsertPortfolioSummaryBehaviour.scala`

**Explicit source context (hunk):**

> +      portfolioW12mFut = RiskToleranceHelper
> +        .w12m(portfolioSummary.mayBePortfolioPerformance)
> +        .map(Future.successful)
> +        .getOrElse(Future.failed(new RuntimeException(s"Portfolio w12m is not present for given portfolio")))
> +      applicableAdvisoryQuestionnaires <- deriveApplicableAdvisoryQuestionnaires(portfolioSummary.instruments, allowedInstrumentsResponse.instrumentGoalTypes)
> +        .flatMap(getAdvisoryQuestionnaire(_)(portfolioSummary.instruments, portfolioW12mFut))
> +      performanceMetricsSummaries <- getPerformanceMetricsSummaries(applicableAdvisoryQuestionnaires, maybePortfolioPerformance, portfolioSummary)
> +      goalFeesRange <- calculateGoalFeeRange(tenantId, request.tradingAccountType)
> +    } yield

## A1-2300 — Why entity was never initialized with ClusterSharding

**Source stance:** open-question

**Context:**

> component: applying-impl/src/main/scala/com/endowus/silver/applying/impl/ApplyingApplication.scala; operation: [INV-3987] Ensure clusterSharding.init(Entity) are called first during application init; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Not sure why we didnt init this entity with ClusterSharding before.
> […incidental material or intervening source omitted…]
> was it intended?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2317 · comment 598596187 · PR 11197 · 2025-02-21

Source path: `applying-impl/src/main/scala/com/endowus/silver/applying/impl/ApplyingApplication.scala`

> Not sure why we didnt init this entity with ClusterSharding before.

**Explicit source context (pr_title):**

> [INV-3987] Ensure clusterSharding.init(Entity) are called first during application init

**Evidence:** anon-1.jsonl:2317 · comment 598596187 · PR 11197 · 2025-02-21

Source path: `applying-impl/src/main/scala/com/endowus/silver/applying/impl/ApplyingApplication.scala`

> was it intended?

## A1-2336 — Akka ExtensionId singleton per actor system

**Source stance:** explanation

**Context:**

> component: admin-impl/src/main/scala/com/endowus/silver/admin/impl/AdminApplication.scala; operation: [INV-3987] Use akka v2.6.21. Eager init *Application via *ApplicationExtension; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Akka extensions are singleton \(with ExtensionId\) in an actor system

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2353 · comment 597192689 · PR 11145 · 2025-02-17

Source path: `admin-impl/src/main/scala/com/endowus/silver/admin/impl/AdminApplication.scala`

**Explicit source context (pr_title):**

> [INV-3987] Use akka v2.6.21. Eager init *Application via *ApplicationExtension

**Evidence:** anon-1.jsonl:2353 · comment 597192689 · PR 11145 · 2025-02-17

Source path: `admin-impl/src/main/scala/com/endowus/silver/admin/impl/AdminApplication.scala`

**Explicit source context (hunk):**

> -        }
> +      system,
> +      () => AdminApplicationExtension(system),
> +      () => {
> +        val httpServerStartup = HttpServerStartup(system, AdminApplicationExtension(system).httpRoutes)
> +        Await.result(httpServerStartup.start(), 60.seconds)
>        }
>      )
>    }

## A1-2337 — Eager application init exposed manual cluster join hidden in Lagom client

**Source stance:** reported-verification

**Context:**

> component: admin-impl/src/main/scala/com/endowus/silver/admin/impl/AdminApplication.scala; operation: [INV-3987] Use akka v2.6.21. Eager init *Application via *ApplicationExtension; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** New nodes could not join/form cluster; HTTP service locator does not require join

**Source-preserving request, proposal, or question:**

> I was testing this PR in dynamic ,and new nodes with this change simply couldn’t join the existing cluster. Even complete scale down to 0 and 3, and the new nodes couldn’t form a cluster together. It only “see” itself.
> 
> Spent so much checking the release notes to find any incompatibility issue, only to realize much later that we have this manual join step when defining the Lagom ServiceClient
> 
> * it’s “hidden” previously because we used to init \*Application after member UP status, so this join is noop
> * it’s not even required to use the ServiceClient since this is purely http via the service locator
> 
> I can’t recall why we added this initially, but I think it makes sense to remove it
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Remove legacy join; original reason unknown.

**Evidence:** anon-1.jsonl:2355 · comment 597456123 · PR 11145 · 2025-02-18

Source path: `admin-impl/src/main/scala/com/endowus/silver/admin/impl/AdminApplication.scala`

**Explicit source context (pr_title):**

> [INV-3987] Use akka v2.6.21. Eager init *Application via *ApplicationExtension

## A1-2338 — Eager init reduces AskTimeout during restarts but coordinator deletion still causes some

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-3987] Use akka v2.6.21. Eager init *Application via *ApplicationExtension; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Noncoordinator deletion no errors; rolling restart similar; shard distribution influences

**Source-preserving request, proposal, or question:**

> Testing completed. The change helps to reduce the AskTimeout occurrences during pod restart/deployment, however do not remove it completely.
> 
> ‌
> 
> Test setup: a simple client that repeatedly hit an endpoint that would hit an entity & interfere with the cluster while the client is running and observe any errors
> 
> ```
> execFut {
>   Source
>     .tick(1.second, 100.millis, "tick")
>     .runForeach { _ =>
>       if (counter.incrementAndGet() % 100 == 0) {
>         logger.info("Still running")
>       }
>       Source(1 to 10)
>         .map(_ => UUID.randomUUID())
>         .mapAsync(4) {
>           chargeService.getPlanProfile(_).invoke().recover {
>             case e => logger.error(s"FAILED with ${e.getMessage}")
>           }
>         }
>         .runWith(Sink.ignore)
>     }
> }
> ```
> 
> ‌
> 
> Before the change:
> 
> * Delete any node \(simulate node consolidation\) would trigger the AskTimeout errors, particularly worse if the node is currently the ShardCoordinator \(oldest node\)
> * Rolling restart \(i.e. simulate deployment\) would trigger AskTimeout errors
> 
> ‌
> 
> After the change:
> 
> * Deleting non-ShardCoordinator node does not trigger any AskTimeout errors. No errors from the ShardCoordinator either
> * Deleting ShardCoordinator node still trigger a few AskTimeout errors, however much fewer number of errors as compared to before the change. Still no errors logged by the new ShardCoordinator, so it’s likely just extra latency caused by the shard rebalancing. Indeed can observe less AskTimeout errors if deleting the node when the shard allocation is more even. Could be related to [
> […incidental material or intervening source omitted…]
> * Rolling restart exhibit similar pattern: no errors for younger nodes, fewer errors for the oldest ShardCoordinator node
> 
> ‌
> 
> I can try with the experiment to enable faster shard rebalance in next PR \([
> […incidental material or intervening source omitted…]
> introduced since v.2.6.10 with a note that it would be the new default however disabled by default, and only rebalance one shard at a time\), but I think this one is good to go.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Faster rebalance experiment next PR, historical2.6.10 default-off single-shard note.

**Evidence:** anon-1.jsonl:2356 · comment 597494111 · PR 11145 · 2025-02-18

> Testing completed. The change helps to reduce the AskTimeout occurrences during pod restart/deployment, however do not remove it completely.
> 
> ‌
> 
> Test setup: a simple client that repeatedly hit an endpoint that would hit an entity & interfere with the cluster while the client is running and observe any errors
> 
> ```
> execFut {
>   Source
>     .tick(1.second, 100.millis, "tick")
>     .runForeach { _ =>
>       if (counter.incrementAndGet() % 100 == 0) {
>         logger.info("Still running")
>       }
>       Source(1 to 10)
>         .map(_ => UUID.randomUUID())
>         .mapAsync(4) {
>           chargeService.getPlanProfile(_).invoke().recover {
>             case e => logger.error(s"FAILED with ${e.getMessage}")
>           }
>         }
>         .runWith(Sink.ignore)
>     }
> }
> ```
> 
> ‌
> 
> Before the change:
> 
> * Delete any node \(simulate node consolidation\) would trigger the AskTimeout errors, particularly worse if the node is currently the ShardCoordinator \(oldest node\)
> * Rolling restart \(i.e. simulate deployment\) would trigger AskTimeout errors
> 
> ‌
> 
> After the change:
> 
> * Deleting non-ShardCoordinator node does not trigger any AskTimeout errors. No errors from the ShardCoordinator either
> * Deleting ShardCoordinator node still trigger a few AskTimeout errors, however much fewer number of errors as compared to before the change. Still no errors logged by the new ShardCoordinator, so it’s likely just extra latency caused by the shard rebalancing. Indeed can observe less AskTimeout errors if deleting the node when the shard allocation is more even. Could be related to [

**Explicit source context (pr_title):**

> [INV-3987] Use akka v2.6.21. Eager init *Application via *ApplicationExtension

**Evidence:** anon-1.jsonl:2356 · comment 597494111 · PR 11145 · 2025-02-18

> * Rolling restart exhibit similar pattern: no errors for younger nodes, fewer errors for the oldest ShardCoordinator node
> 
> ‌
> 
> I can try with the experiment to enable faster shard rebalance in next PR \([

**Evidence:** anon-1.jsonl:2356 · comment 597494111 · PR 11145 · 2025-02-18

> introduced since v.2.6.10 with a note that it would be the new default however disabled by default, and only rebalance one shard at a time\), but I think this one is good to go.

## A2-0021 — PortfolioUnderlyingManager: This will go to entity? Do we need that or readside is ok?

**Source stance:** open-question

**Context:**

> PR 10991 (Feat/EN-4318 portfolio aaa bff integration), portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/PortfolioUnderlyingManager.scala; original row 21.

**Source-preserving request, proposal, or question:**

> This will go to entity? Do we need that or readside is ok?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:21 · comment 608508619 · PR 10991 · 2025-03-13

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/PortfolioUnderlyingManager.scala`

**Evidence:** anon-2.jsonl:21 · comment 608508619 · PR 10991 · 2025-03-13

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/managers/PortfolioUnderlyingManager.scala`

**Explicit source context (pr_title):**

> Feat/EN-4318 portfolio aaa bff integration

## A2-0025 — package: We may decide to make it required field in DTO after successful backfill \(or adding on-the-fly lookup\), but here it must stay optional as [person] said, due to histor...

**Source stance:** explanation

**Context:**

> PR 11333 ([EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/state/package.scala; original row 25.

**Concern stated in the source:** Historical events and snapshots can lack tenantId.

**Source-preserving request, proposal, or question:**

> We may decide to make it required field in DTO after successful backfill \(or adding on-the-fly lookup\), but here it must stay optional as [person] said, due to historical events & snapshots

**Conditions and limits:**

- The DTO may become required after successful backfill or on-the-fly lookup; historical events/snapshots must remain optional.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:25 · comment 609023920 · PR 11333 · 2025-03-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/state/package.scala`

> We may decide to make it required field in DTO after successful backfill \(or adding on-the-fly lookup\), but here it must stay optional as

**Evidence:** anon-2.jsonl:25 · comment 609023920 · PR 11333 · 2025-03-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/state/package.scala`

> said, due to historical events & snapshots

**Evidence:** anon-2.jsonl:25 · comment 609023920 · PR 11333 · 2025-03-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/state/package.scala`

**Explicit source context (pr_title):**

> [EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles

## A2-0026 — BackfillPlanProfileTenantIdCmdHandler: Let’s also return without events if same tenantId already exists. Then we won’t have duplicated events, as the subscriber might process a ...

**Source stance:** requested-change

**Context:**

> PR 11333 ([EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/BackfillPlanProfileTenantIdCmdHandler.scala; original row 26.

**Concern stated in the source:** A subscriber can process a task more than once and generate duplicate tenant-backfill events.

**Source-preserving request, proposal, or question:**

> Let’s also return without events if same tenantId already exists. Then we won’t have duplicated events, as the subscriber might process a task multiple times.

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:26 · comment 609026873 · PR 11333 · 2025-03-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/BackfillPlanProfileTenantIdCmdHandler.scala`

**Evidence:** anon-2.jsonl:26 · comment 609026873 · PR 11333 · 2025-03-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/BackfillPlanProfileTenantIdCmdHandler.scala`

**Explicit source context (pr_title):**

> [EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles

## A2-0027 — BackfillPlanProfileTenantIdTaskTopicSubscriber: We shouldn’t need planId as part of the cmd since it’s already entityId

**Source stance:** explanation

**Context:**

> PR 11333 ([EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/task/BackfillPlanProfileTenantIdTaskTopicSubscriber.scala; original row 27.

**Source-preserving request, proposal, or question:**

> We shouldn’t need planId as part of the cmd since it’s already entityId

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:27 · comment 609023439 · PR 11333 · 2025-03-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/task/BackfillPlanProfileTenantIdTaskTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:27 · comment 609023439 · PR 11333 · 2025-03-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/task/BackfillPlanProfileTenantIdTaskTopicSubscriber.scala`

**Explicit source context (pr_title):**

> [EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles

## A2-0028 — PlanProfileJdbcProjectionV3: Since we have the full PlanProfile in the `PlanProfileTenantIdBackFilledEvt`, let’s use it directly instead of fetching from entity again.

**Source stance:** explanation

**Context:**

> PR 11333 ([EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/PlanProfileJdbcProjectionV3.scala; original row 28.

**Concern stated in the source:** The event already contains the full PlanProfile; fetching entity state again is unnecessary for this event.

**Source-preserving request, proposal, or question:**

> Since we have the full PlanProfile in the `PlanProfileTenantIdBackFilledEvt`, let’s use it directly instead of fetching from entity again.
> 
> One day we need to for all these existing events as well, to have separate update query for them that doesn’t rely on fetching whole PlanProfile

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:28 · comment 609335815 · PR 11333 · 2025-03-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/PlanProfileJdbcProjectionV3.scala`

**Evidence:** anon-2.jsonl:28 · comment 609335815 · PR 11333 · 2025-03-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/PlanProfileJdbcProjectionV3.scala`

**Explicit source context (pr_title):**

> [EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles

## A2-0031 — BackfillPlanProfileTenantIdTaskTopicSubscriber: I realize we could have made the task keyed by customerId instead, then in this subscriber, we query planProfiles by customerId a...

**Source stance:** suggestion

**Context:**

> PR 11333 ([EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/task/BackfillPlanProfileTenantIdTaskTopicSubscriber.scala; original row 31.

**Source-preserving request, proposal, or question:**

> I realize we could have made the task keyed by customerId instead, then in this subscriber, we query planProfiles by customerId and invoke the cmd as usual. It’s one time exercise so this is ok too

**Conditions and limits:**

- The customerId-keyed alternative is explicitly considered optional because this is a one-time exercise.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:31 · comment 609631484 · PR 11333 · 2025-03-17

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/task/BackfillPlanProfileTenantIdTaskTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:31 · comment 609631484 · PR 11333 · 2025-03-17

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/task/BackfillPlanProfileTenantIdTaskTopicSubscriber.scala`

**Explicit source context (pr_title):**

> [EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles

## A2-0039 — BaseRedemptionCommunicationV2Projection: Naming can be a little confusing now

**Source stance:** suggestion

**Context:**

> PR 11207 ([EN-4396] feat(redemption)(communication) Support B2B redemption emails and migrate to Communicator V2), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala; original row 39.

**Concern stated in the source:** The actual HK projection inherits BaseRedemptionCommunicationV2Projection, the actual SG projection does not, and two new CommunicationManagers do.

**Source-preserving request, proposal, or question:**

> Naming can be a little confusing now
> 
> * HkRedemptionCommunicationV2Projection \(actual projection\) extends BaseRedemptionCommunicationV2Projection
> * but SgRedemptionCommunicationV2Projection \(actual projection\) does not, and yet the 2 new CommunicationManger extends BaseRedemptionCommunicationV2Projection
> 
> We can refactor later. This is just a note for now
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:39 · comment 610709720 · PR 11207 · 2025-03-19

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Evidence:** anon-2.jsonl:39 · comment 610709720 · PR 11207 · 2025-03-19

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> [EN-4396] feat(redemption)(communication) Support B2B redemption emails and migrate to Communicator V2

## A2-0052 — SgWorkflowEngineE4s: Can we double check this endpoint with workflow-engine again? I think the ActorRole here is supposed to be for assignee type?

**Source stance:** open-question

**Context:**

> PR 10812 ([INV-3426] feat(bff, workflow-engine, advisory): Portfolio / Investment summaries), workflowengine-api/src/main/scala/com/endowus/silver/workflowengine/api/SgWorkflowEngineE4s.scala; original row 52.

**Source-preserving request, proposal, or question:**

> Can we double check this endpoint with workflow-engine again? I think the ActorRole here is supposed to be for assignee type?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:52 · comment 585700363 · PR 10812 · 2025-01-13

Source path: `workflowengine-api/src/main/scala/com/endowus/silver/workflowengine/api/SgWorkflowEngineE4s.scala`

**Evidence:** anon-2.jsonl:52 · comment 585700363 · PR 10812 · 2025-01-13

Source path: `workflowengine-api/src/main/scala/com/endowus/silver/workflowengine/api/SgWorkflowEngineE4s.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, workflow-engine, advisory): Portfolio / Investment summaries

## A2-0077 — FixV3FeeRedemptionTransactions: Temp code so maybe ok, but I remember we have a refactored version of this code in transaction svc…

**Source stance:** suggestion

**Context:**

> PR 7209 ([INV-1976] feat(amend): Scripts to amend dividends, redemption and deleted order transactions), amend-scripts/src/main/scala/transaction/FixV3FeeRedemptionTransactions.scala; original row 77.

**Source-preserving request, proposal, or question:**

> Temp code so maybe ok, but I remember we have a refactored version of this code in transaction svc…

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:77 · comment 436528467 · PR 7209 · 2023-10-17

Source path: `amend-scripts/src/main/scala/transaction/FixV3FeeRedemptionTransactions.scala`

**Evidence:** anon-2.jsonl:77 · comment 436528467 · PR 7209 · 2023-10-17

Source path: `amend-scripts/src/main/scala/transaction/FixV3FeeRedemptionTransactions.scala`

**Explicit source context (pr_title):**

> [INV-1976] feat(amend): Scripts to amend dividends, redemption and deleted order transactions

## A2-0081 — CreateFixedMaturityProductGoal: If small number of goals then it’s ok, but ideally we could use an async loading cache here \+ go to readside instead of entity

**Source stance:** suggestion

**Context:**

> PR 9462 (Resolve INV-3172: Amend script to create goals for fixed maturity product customers.), amend-scripts/src/main/scala/goal/CreateFixedMaturityProductGoal.scala; original row 81.

**Concern stated in the source:** Entity calls are acceptable for few goals; an async loading cache with readside lookup is preferable at larger volume.

**Source-preserving request, proposal, or question:**

> If small number of goals then it’s ok, but ideally we could use an async loading cache here \+ go to readside instead of entity

**Conditions and limits:**

- The comment explicitly permits the existing approach for a small number of goals.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:81 · comment 514391773 · PR 9462 · 2024-06-28

Source path: `amend-scripts/src/main/scala/goal/CreateFixedMaturityProductGoal.scala`

**Evidence:** anon-2.jsonl:81 · comment 514391773 · PR 9462 · 2024-06-28

Source path: `amend-scripts/src/main/scala/goal/CreateFixedMaturityProductGoal.scala`

**Explicit source context (pr_title):**

> Resolve INV-3172: Amend script to create goals for fixed maturity product customers.

## A2-0095 — InstrumentTransferService: Do we need to specify brokerAccountId in this cmd? Since it’s possible to have multiple broker accounts?

**Source stance:** open-question

**Context:**

> PR 11820 (TT-5817 Use case for full transfer plan out), trading-impl/src/main/scala/com/endowus/silver/trading/impl/logic/service/InstrumentTransferService.scala; original row 95.

**Concern stated in the source:** Multiple broker accounts can exist.

**Source-preserving request, proposal, or question:**

> Do we need to specify brokerAccountId in this cmd? Since it’s possible to have multiple broker accounts?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:95 · comment 632628854 · PR 11820 · 2025-05-14

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/logic/service/InstrumentTransferService.scala`

**Evidence:** anon-2.jsonl:95 · comment 632628854 · PR 11820 · 2025-05-14

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/logic/service/InstrumentTransferService.scala`

**Explicit source context (pr_title):**

> TT-5817 Use case for full transfer plan out

## A2-0106 — GoalSupportingDataProjection: This block probably can refactor to avoid repeating the code vs `handleGoalCreationApprovedHandler`

**Source stance:** suggestion

**Context:**

> PR 10896 ([INV-3426] feat(bff, advisory, goal, investment): Approval flow), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalSupportingDataProjection.scala; original row 106.

**Source-preserving request, proposal, or question:**

> This block probably can refactor to avoid repeating the code vs `handleGoalCreationApprovedHandler`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:106 · comment 587734350 · PR 10896 · 2025-01-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalSupportingDataProjection.scala`

**Evidence:** anon-2.jsonl:106 · comment 587734350 · PR 10896 · 2025-01-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalSupportingDataProjection.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, advisory, goal, investment): Approval flow

## A2-0120 — InvestmentPlanEntity: The request would be upserted by `InvestmentRequestCreatedEvt`. We don’t need to do anything here for the state

**Source stance:** explanation

**Context:**

> PR 10896 ([INV-3426] feat(bff, advisory, goal, investment): Approval flow), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/InvestmentPlanEntity.scala; original row 120.

**Concern stated in the source:** InvestmentRequestCreatedEvt already upserts the request.

**Source-preserving request, proposal, or question:**

> The request would be upserted by `InvestmentRequestCreatedEvt`. We don’t need to do anything here for the state

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:120 · comment 587730635 · PR 10896 · 2025-01-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/InvestmentPlanEntity.scala`

**Evidence:** anon-2.jsonl:120 · comment 587730635 · PR 10896 · 2025-01-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/InvestmentPlanEntity.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, advisory, goal, investment): Approval flow

## A2-0140 — InvestOnceCmdHandler: Nit: `maybeInvestmentRequestCreationApprovedEvt.toList` is sufficient

**Source stance:** suggestion

**Context:**

> PR 10896 ([INV-3426] feat(bff, advisory, goal, investment): Approval flow), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InvestOnceCmdHandler.scala; original row 140.

**Source-preserving request, proposal, or question:**

> Nit: `maybeInvestmentRequestCreationApprovedEvt.toList` is sufficient

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:140 · comment 601749287 · PR 10896 · 2025-03-04

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InvestOnceCmdHandler.scala`

**Evidence:** anon-2.jsonl:140 · comment 601749287 · PR 10896 · 2025-03-04

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InvestOnceCmdHandler.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, advisory, goal, investment): Approval flow

## A2-0143 — StopRecurringInvestmentScheduleCmdHandler: Same here and the cmd handler below. Can use Option#toList

**Source stance:** suggestion

**Context:**

> PR 10896 ([INV-3426] feat(bff, advisory, goal, investment): Approval flow), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/StopRecurringInvestmentScheduleCmdHandler.scala; original row 143.

**Source-preserving request, proposal, or question:**

> Same here and the cmd handler below. Can use Option#toList

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:143 · comment 601752486 · PR 10896 · 2025-03-04

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/StopRecurringInvestmentScheduleCmdHandler.scala`

**Evidence:** anon-2.jsonl:143 · comment 601752486 · PR 10896 · 2025-03-04

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/StopRecurringInvestmentScheduleCmdHandler.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, advisory, goal, investment): Approval flow

## A2-0171 — CreateGoalWithPlansCmdHandler: map

**Source stance:** requested-change

**Context:**

> PR 10120 (Feat/INV-3508 goal create b2b), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/CreateGoalWithPlansCmdHandler.scala; original row 171.

**Source-preserving request, proposal, or question:**

> map

**Conditions and limits:**

- The short comment "map" refers to event-list construction shown in the hunk; the comment itself supplies no fuller replacement.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:171 · comment 550968154 · PR 10120 · 2024-10-10

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/CreateGoalWithPlansCmdHandler.scala`

**Evidence:** anon-2.jsonl:171 · comment 550968154 · PR 10120 · 2024-10-10

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/CreateGoalWithPlansCmdHandler.scala`

**Explicit source context (hunk):**

> val events = List(maybeGoalCreationApprovedEvt ++ Some(GoalCreatedEvt(goal))).flatten ++ plans.map(PlanCreatedEvt(_))

**Evidence:** anon-2.jsonl:171 · comment 550968154 · PR 10120 · 2024-10-10

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/CreateGoalWithPlansCmdHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3508 goal create b2b

## A2-0200 — InitiateCancellationFlowCmdHandler: This `INVALID_CANCEL_ATTEMPT` is mapped to NotFound right now. It seems not used, so maybe change it to BadRequest instead?

**Source stance:** suggestion

**Context:**

> PR 10714 ([INV-3798] feat(investment): Throw error on cancellation failed in investment service), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala; original row 200.

**Concern stated in the source:** INVALID_CANCEL_ATTEMPT currently maps to NotFound; throwing always can violate expected idempotent best-effort cancellation from projections/subscribers.

**Source-preserving request, proposal, or question:**

> This `INVALID_CANCEL_ATTEMPT` is mapped to NotFound right now. It seems not used, so maybe change it to BadRequest instead?
> 
> Generally, we want these cmd to be idempotent especially when they are used in projection / kafka subscriber. I think all these use cases that trigger investment cancellation from BE \(redemption / expiry / compliance\) understand that it is best effort basis. So it’s better to expose a flag to ignore this error instead of throwing always?

**Conditions and limits:**

- Best-effort cancellation is specifically discussed for backend redemption/expiry/compliance triggers; the source proposes an ignore-error flag.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:200 · comment 580810035 · PR 10714 · 2024-12-23

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala`

**Evidence:** anon-2.jsonl:200 · comment 580810035 · PR 10714 · 2024-12-23

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala`

**Explicit source context (pr_title):**

> [INV-3798] feat(investment): Throw error on cancellation failed in investment service

## A2-0201 — InitiateCancellationFlowCmdHandler: If you stick with throwing, need to add handling in compliance svc’s state change logic as well

**Source stance:** requested-change

**Context:**

> PR 10714 ([INV-3798] feat(investment): Throw error on cancellation failed in investment service), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala; original row 201.

**Source-preserving request, proposal, or question:**

> If you stick with throwing, need to add handling in compliance svc’s state change logic as well

**Conditions and limits:**

- Only applies if the implementation keeps throwing cancellation errors.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:201 · comment 580810352 · PR 10714 · 2024-12-23

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala`

**Evidence:** anon-2.jsonl:201 · comment 580810352 · PR 10714 · 2024-12-23

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala`

**Explicit source context (pr_title):**

> [INV-3798] feat(investment): Throw error on cancellation failed in investment service

## A2-0202 — InitiateCancellationFlowCmdHandler: We will need to add another `InvestmentSvcException` in investment-impl otherwise it won’t work in cluster mode

**Source stance:** explanation

**Context:**

> PR 10714 ([INV-3798] feat(investment): Throw error on cancellation failed in investment service), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala; original row 202.

**Concern stated in the source:** InvestmentSvcException must also exist in investment-impl for cluster-mode serialization.

**Source-preserving request, proposal, or question:**

> We will need to add another `InvestmentSvcException` in investment-impl otherwise it won’t work in cluster mode

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:202 · comment 580808908 · PR 10714 · 2024-12-23

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala`

**Evidence:** anon-2.jsonl:202 · comment 580808908 · PR 10714 · 2024-12-23

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala`

**Explicit source context (pr_title):**

> [INV-3798] feat(investment): Throw error on cancellation failed in investment service

## A2-0210 — BffServiceE4s: Yea unfortunately we will have to type out the `Schema` for all data models that are \(recursively\) used in endpoints' input/output. It’s not exactly a refactor ...

**Source stance:** suggestion

**Context:**

> PR 10301 ([AD-2061] feat(advisory-portal,bff): Added BrokerAccountCashBalances endpoint), bff-api/src/main/scala/com/endowus/silver/bff/api/BffServiceE4s.scala; original row 210.

**Concern stated in the source:** Endpoint schemas must exist recursively for all input/output models; migration can be tracked in a backlog TODO.

**Source-preserving request, proposal, or question:**

> Yea unfortunately we will have to type out the `Schema` for all data models that are \(recursively\) used in endpoints' input/output. It’s not exactly a refactor tho, and there’s some utility in Intellij \(live template\) to aid with that.
> 
> I guess for starter, let’s make a TODO with a backlog ticket for trading team, so that we can migrate these endpoints later.

**Conditions and limits:**

- The backlog TODO is an accepted initial step; recursive schema migration is not claimed complete.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:210 · comment 563708143 · PR 10301 · 2024-11-11

Source path: `bff-api/src/main/scala/com/endowus/silver/bff/api/BffServiceE4s.scala`

**Evidence:** anon-2.jsonl:210 · comment 563708143 · PR 10301 · 2024-11-11

Source path: `bff-api/src/main/scala/com/endowus/silver/bff/api/BffServiceE4s.scala`

**Explicit source context (pr_title):**

> [AD-2061] feat(advisory-portal,bff): Added BrokerAccountCashBalances endpoint

## A2-0211 — package: [person] [person] Looks the issue to due to `BrokerAccountCashBalanceDto` containing a nested field of itself

**Source stance:** suggestion

**Context:**

> PR 10301 ([AD-2061] feat(advisory-portal,bff): Added BrokerAccountCashBalances endpoint), trading-api/src/main/scala/com/endowus/silver/trading/api/models/package.scala; original row 211.

**Concern stated in the source:** BrokerAccountCashBalanceDto recursively nests itself; proposed data extraction removes that recursion.

**Source-preserving request, proposal, or question:**

> [person] [person] Looks the issue to due to `BrokerAccountCashBalanceDto` containing a nested field of itself
> 
> We should refactor this a bit, to avoid this recursion. Maybe something along this line
> 
> ```
> case class BrokerAccountCashBalanceData(
>     availableAmount: BigDecimal,
>     payableAmount: BigDecimal,
>     receivableAmount: BigDecimal,
>     receivableAmountFromFeeRedemption: Option[BigDecimal]
> )
> 
> case class BrokerAccountCashBalanceDto(
>     customerId: UUID,
>     tradingAccountType: TradingAccountType,
>     accountCcy: CurrencyUnit,
>     broker: Broker,
>     brokerAccountNumber: String,
>     updatedAt: Instant,
>     data: BrokerAccountCashBalanceData
>     displayCcy: Option[CurrencyUnit],
>     originalData: Option[BrokerAccountCashBalanceData]
> )
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:211 · comment 564444609 · PR 10301 · 2024-11-13

Source path: `trading-api/src/main/scala/com/endowus/silver/trading/api/models/package.scala`

> Looks the issue to due to `BrokerAccountCashBalanceDto` containing a nested field of itself
> 
> We should refactor this a bit, to avoid this recursion. Maybe something along this line
> 
> ```
> case class BrokerAccountCashBalanceData(
>     availableAmount: BigDecimal,
>     payableAmount: BigDecimal,
>     receivableAmount: BigDecimal,
>     receivableAmountFromFeeRedemption: Option[BigDecimal]
> )
> 
> case class BrokerAccountCashBalanceDto(
>     customerId: UUID,
>     tradingAccountType: TradingAccountType,
>     accountCcy: CurrencyUnit,
>     broker: Broker,
>     brokerAccountNumber: String,
>     updatedAt: Instant,
>     data: BrokerAccountCashBalanceData
>     displayCcy: Option[CurrencyUnit],
>     originalData: Option[BrokerAccountCashBalanceData]
> )
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:211 · comment 564444609 · PR 10301 · 2024-11-13

Source path: `trading-api/src/main/scala/com/endowus/silver/trading/api/models/package.scala`

**Explicit source context (pr_title):**

> [AD-2061] feat(advisory-portal,bff): Added BrokerAccountCashBalances endpoint

## A2-0219 — SgGoalCreateApprovalSummaryBehaviour: State change applies here. Let’s check w PM \+ designer

**Source stance:** open-question

**Context:**

> PR 10561 (Feat/INV-3699 approval summary endpoint), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreateApprovalSummaryBehaviour.scala; original row 219.

**Source-preserving request, proposal, or question:**

> State change applies here. Let’s check w PM \+ designer

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- State-change applicability requires PM/designer checking; no settled action is provided.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:219 · comment 577242886 · PR 10561 · 2024-12-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreateApprovalSummaryBehaviour.scala`

**Evidence:** anon-2.jsonl:219 · comment 577242886 · PR 10561 · 2024-12-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreateApprovalSummaryBehaviour.scala`

**Explicit source context (hunk):**

> +      }
> +
> +      allowedInstrumentsResponse <- corporateProductRuleService.allowedInstrumentsBasedOnCorporateProfileForTenant(
> +        tenantId = tenantId,
> +        maybeTradingAccountType = Some(request.tradingAccountType),
> +        maybeGoalType = None,
> +        instruments = portfolioSummary.instruments,

**Evidence:** anon-2.jsonl:219 · comment 577242886 · PR 10561 · 2024-12-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreateApprovalSummaryBehaviour.scala`

**Explicit source context (pr_title):**

> Feat/INV-3699 approval summary endpoint

## A2-0230 — RebalancePlanTableV4: Remove all the index on customerId/goalId/tradingAccountType/planCcy - we don’t use them at all.

**Source stance:** explanation

**Context:**

> PR 10592 ([INV-3707] feat(rebalance): Support blacklisting auto-rebalance for specific plan), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalancePlanTableV4.scala; original row 230.

**Concern stated in the source:** customerId/goalId/tradingAccountType/planCcy indices are unused; portfolioId is anticipated for TAA entity removal.

**Source-preserving request, proposal, or question:**

> Remove all the index on customerId/goalId/tradingAccountType/planCcy - we don’t use them at all.
> 
> Add index on portfolioId in anticipation for removal of TAA entity

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:230 · comment 576285462 · PR 10592 · 2024-12-10

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalancePlanTableV4.scala`

**Evidence:** anon-2.jsonl:230 · comment 576285462 · PR 10592 · 2024-12-10

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalancePlanTableV4.scala`

**Explicit source context (pr_title):**

> [INV-3707] feat(rebalance): Support blacklisting auto-rebalance for specific plan

## A2-0231 — ClientEntity: You will need to add `TenantSvcException` in tenant-impl that extends `PlayJsonSerializable` otherwise serdes will fail in cluster mode

**Source stance:** explanation

**Context:**

> PR 10576 ([ONB-4302][ONB-4308] B2C tenantId fallback and Not Found error for getClientById), tenant-impl/src/main/scala/com/endowus/silver/tenant/impl/client/entities/ClientEntity.scala; original row 231.

**Concern stated in the source:** TenantSvcException in tenant-impl must extend PlayJsonSerializable for cluster-mode serialization.

**Source-preserving request, proposal, or question:**

> You will need to add `TenantSvcException` in tenant-impl that extends `PlayJsonSerializable` otherwise serdes will fail in cluster mode

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:231 · comment 576372484 · PR 10576 · 2024-12-10

Source path: `tenant-impl/src/main/scala/com/endowus/silver/tenant/impl/client/entities/ClientEntity.scala`

**Evidence:** anon-2.jsonl:231 · comment 576372484 · PR 10576 · 2024-12-10

Source path: `tenant-impl/src/main/scala/com/endowus/silver/tenant/impl/client/entities/ClientEntity.scala`

**Explicit source context (pr_title):**

> [ONB-4302][ONB-4308] B2C tenantId fallback and Not Found error for getClientById

## A2-0244 — SgGoalApprovedForCreationBehaviour: Ideally `validate` should return the resolved objects that all these create steps can use without further validation.

**Source stance:** suggestion

**Context:**

> PR 10425 ([INV-3508] Add goal flow advisory logic), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalApprovedForCreationBehaviour.scala; original row 244.

**Concern stated in the source:** Throwing after portfolio/goal creation obscures what happens to those created entities; validate ideally returns resolved objects.

**Source-preserving request, proposal, or question:**

> Ideally `validate` should return the resolved objects that all these create steps can use without further validation.
> 
> I guess we can refactor this code another day, but for this PR, it’s probably easier to just call `.get` here with comment that it’s validated. Instead of throwing and viewer might think “if throw, what do we do with the created portfolio/goal above”

**Conditions and limits:**

- For this PR, .get with an already-validated comment is suggested as a temporary choice; returning resolved validated objects is a later refactor.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:244 · comment 570132153 · PR 10425 · 2024-11-26

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalApprovedForCreationBehaviour.scala`

**Evidence:** anon-2.jsonl:244 · comment 570132153 · PR 10425 · 2024-11-26

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalApprovedForCreationBehaviour.scala`

**Explicit source context (pr_title):**

> [INV-3508] Add goal flow advisory logic

## A2-0263 — InstrumentTransfer: Yea the trigger endpoint is one plan only cuz that’s the max safety we can guarantee \(via PlanTraderEntity\). I allow simulation to accept multiple source p...

**Source stance:** explanation

**Context:**

> PR 10432 (feat(broker)(marketdata)(rebalance)(report)(trading)(transaction)(timeseries): InterPlan InstrumentTransfer), trading-api/src/main/scala/com/endowus/silver/trading/api/requests/InstrumentTransfer.scala; original row 263.

**Concern stated in the source:** PlanTraderEntity provides safety for only one source plan at trigger time; simulation can estimate multiple-source AAA vs TAA before target creation/TAA changes.

**Source-preserving request, proposal, or question:**

> Yea the trigger endpoint is one plan only cuz that’s the max safety we can guarantee \(via PlanTraderEntity\). I allow simulation to accept multiple source plan, in case customer doesn’t have a target plan yet, or want to modify target plan’s TAA after all the transfer. So the simulation allows to estimate AAA vs TAA upfront

**Conditions and limits:**

- Trigger remains one-plan-only; the broader scope is simulation, including target-not-yet-created and later target-TAA modification cases.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:263 · comment 571286722 · PR 10432 · 2024-11-28

Source path: `trading-api/src/main/scala/com/endowus/silver/trading/api/requests/InstrumentTransfer.scala`

**Evidence:** anon-2.jsonl:263 · comment 571286722 · PR 10432 · 2024-11-28

Source path: `trading-api/src/main/scala/com/endowus/silver/trading/api/requests/InstrumentTransfer.scala`

**Explicit source context (pr_title):**

> feat(broker)(marketdata)(rebalance)(report)(trading)(transaction)(timeseries): InterPlan InstrumentTransfer

## A2-0264 — AcceptRebalanceSellTradeRequestCmdHandler: We agreed to leave this intact. It will be short circuited later due to no sell orders.

**Source stance:** explanation

**Context:**

> PR 10432 (feat(broker)(marketdata)(rebalance)(report)(trading)(transaction)(timeseries): InterPlan InstrumentTransfer), trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/AcceptRebalanceSellTradeRequestCmdHandler.scala; original row 264.

**Concern stated in the source:** This branch will short-circuit later because there are no sell orders.

**Source-preserving request, proposal, or question:**

> We agreed to leave this intact. It will be short circuited later due to no sell orders.
> 
> We can change this another time

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:264 · comment 571308684 · PR 10432 · 2024-11-28

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/AcceptRebalanceSellTradeRequestCmdHandler.scala`

**Evidence:** anon-2.jsonl:264 · comment 571308684 · PR 10432 · 2024-11-28

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/AcceptRebalanceSellTradeRequestCmdHandler.scala`

**Explicit source context (pr_title):**

> feat(broker)(marketdata)(rebalance)(report)(trading)(transaction)(timeseries): InterPlan InstrumentTransfer

## A2-0274 — ChargeHelpers: `state.feeInstructions.to(TreeMap)` is sufficient I think

**Source stance:** suggestion

**Context:**

> PR 10097 ([EN-3954] (charge) integrate fee instruction with context), charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/ChargeHelpers.scala; original row 274.

**Source-preserving request, proposal, or question:**

> `state.feeInstructions.to(TreeMap)` is sufficient I think

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:274 · comment 552732398 · PR 10097 · 2024-10-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/ChargeHelpers.scala`

**Evidence:** anon-2.jsonl:274 · comment 552732398 · PR 10097 · 2024-10-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/ChargeHelpers.scala`

**Explicit source context (pr_title):**

> [EN-3954] (charge) integrate fee instruction with context

## A2-0276 — PlanFeeInstructionEntity: Do we need to error here? Just return ack without any events?

**Source stance:** open-question

**Context:**

> PR 10030 ([EN-3952] (charge) Create new PlanFeeInstructionEntity), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala; original row 276.

**Source-preserving request, proposal, or question:**

> Do we need to error here? Just return ack without any events?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:276 · comment 552089047 · PR 10030 · 2024-10-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala`

**Evidence:** anon-2.jsonl:276 · comment 552089047 · PR 10030 · 2024-10-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala`

**Explicit source context (pr_title):**

> [EN-3952] (charge) Create new PlanFeeInstructionEntity

## A2-0278 — PlanFeeInstructionEntity: Similarly, for upsert command, overriding whole Map with single entry from an empty map is the same if we add that entry directly. So there’s no value ...

**Source stance:** explanation

**Context:**

> PR 10030 ([EN-3952] (charge) Create new PlanFeeInstructionEntity), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala; original row 278.

**Concern stated in the source:** Upserting one entry into an empty map is equivalent to replacing that map, so initialized/creation branch split adds no value.

**Source-preserving request, proposal, or question:**

> Similarly, for upsert command, overriding whole Map with single entry from an empty map is the same if we add that entry directly. So there’s no value to split between “for creation” vs “for initialized”

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:278 · comment 552089346 · PR 10030 · 2024-10-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala`

**Evidence:** anon-2.jsonl:278 · comment 552089346 · PR 10030 · 2024-10-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala`

**Explicit source context (pr_title):**

> [EN-3952] (charge) Create new PlanFeeInstructionEntity

## A2-0281 — FeeInstruction: Alright, I’m ok if you prefer this approach too. Just one small ask to return the Map from GetCmd, and you can define the period case class \+ conversion logic i...

**Source stance:** suggestion

**Context:**

> PR 10030 ([EN-3952] (charge) Create new PlanFeeInstructionEntity), charge-impl/src/main/scala/com/endowus/silver/charge/impl/commons/models/FeeInstruction.scala; original row 281.

**Concern stated in the source:** Alright, I’m ok if you prefer this approach too. Just one small ask to return the Map from GetCmd, and you can define the period case class \+ conversion logic in a helper so that we keep this purely at logic / representation layer, instead of entity

**Source-preserving request, proposal, or question:**

> Alright, I’m ok if you prefer this approach too. Just one small ask to return the Map from GetCmd, and you can define the period case class \+ conversion logic in a helper so that we keep this purely at logic / representation layer, instead of entity

**Conditions and limits:**

- The alternative approach is accepted if GetCmd returns Map and period representation/conversion stays in a helper rather than entity.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:281 · comment 552095380 · PR 10030 · 2024-10-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/commons/models/FeeInstruction.scala`

**Evidence:** anon-2.jsonl:281 · comment 552095380 · PR 10030 · 2024-10-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/commons/models/FeeInstruction.scala`

**Explicit source context (pr_title):**

> [EN-3952] (charge) Create new PlanFeeInstructionEntity

## A2-0282 — PlanFeeInstructionEntity: The entity state is default with empty fee instructions, it means the plan always exists, just without any data. Modelling it this way means you can’t ...

**Source stance:** open-question

**Context:**

> PR 10030 ([EN-3952] (charge) Create new PlanFeeInstructionEntity), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala; original row 282.

**Concern stated in the source:** Empty default instructions cannot distinguish never-initialized from upserted-then-deleted plan state.

**Source-preserving request, proposal, or question:**

> The entity state is default with empty fee instructions, it means the plan always exists, just without any data. Modelling it this way means you can’t distinguish between a uninitialized plan vs a plan with upserted-then-deleted fee instructions.
> 
> If we care enough about this, then we probably should make state a sealed trait, default with case object NotInitialized, otherwise it’s case class Initialized\(feeInstructions\). Then you can throw for GetCmd/DeleteCmd on NotInitialized. And no-op without error if deleting already deleted fee instruction for Initialized, and even throw if deleting last entry for Initialized \(to ensure there’s always an entry to support the fee rate query\)

**Conditions and limits:**

- The sealed NotInitialized/Initialized state is conditional on caring about that distinction; no-op deletion and last-entry rejection are proposals within that model.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:282 · comment 552218834 · PR 10030 · 2024-10-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala`

**Evidence:** anon-2.jsonl:282 · comment 552218834 · PR 10030 · 2024-10-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala`

**Explicit source context (pr_title):**

> [EN-3952] (charge) Create new PlanFeeInstructionEntity

## A2-0283 — PlanFeeInstructionEntity: Just thinking out loud, I’m not sure about capturing this effectiveEndDate in the event

**Source stance:** open-question

**Context:**

> PR 10030 ([EN-3952] (charge) Create new PlanFeeInstructionEntity), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala; original row 283.

**Concern stated in the source:** effectiveEndDate is derived, cannot be reconstructed at event-creation state by projection, and changing one instruction generally affects two instruction end dates.

**Source-preserving request, proposal, or question:**

> Just thinking out loud, I’m not sure about capturing this effectiveEndDate in the event
> 
> * It’s derived data, but I understand the concern that projection is not able to derive by itself since projection does not have access to the state at the point of event creation
> * It’s somewhat incomplete, because we would typically affect effectiveEndDate of 2 instructions, but we only emit for the one being upserted / deleted
> 
> If the intention is to provide ability for projection \(or even external topic subscriber\) to reconstruct the exact state, we can consider emit 2 events instead, one for the individual change, and one for the state \(pattern “Event-Carried State Transfer”\). This comes with its own pros & cons, but I think it’s cleaner and more flexible than stamping single effective end date here.
> 
> ‌
> 
> The field is logically optional right now. We can revisit this later if needed.

**Conditions and limits:**

- Two events (individual change plus state transfer) are an option with pros/cons; effectiveEndDate is currently logically optional and may be revisited.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:283 · comment 552730699 · PR 10030 · 2024-10-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala`

**Evidence:** anon-2.jsonl:283 · comment 552730699 · PR 10030 · 2024-10-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala`

**Explicit source context (pr_title):**

> [EN-3952] (charge) Create new PlanFeeInstructionEntity

## A2-0286 — FeeRangeManager: It seems the later PRs assume that firm’s fee range config is already in good state. So maybe we should add validation here to ensure the config is properly con...

**Source stance:** suggestion

**Context:**

> PR 9952 ([EN-3951] (charge) Add apis and table for Range configuration setup), charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeRangeManager.scala; original row 286.

**Concern stated in the source:** Later PRs assume firm fee-range configuration is already valid; invalid input should not be accepted and fail later.

**Source-preserving request, proposal, or question:**

> It seems the later PRs assume that firm’s fee range config is already in good state. So maybe we should add validation here to ensure the config is properly configured here \(rather than letting invalid go thru, and we throw later on\)

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:286 · comment 552091369 · PR 9952 · 2024-10-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeRangeManager.scala`

**Evidence:** anon-2.jsonl:286 · comment 552091369 · PR 9952 · 2024-10-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeRangeManager.scala`

**Explicit source context (pr_title):**

> [EN-3951] (charge) Add apis and table for Range configuration setup

## A2-0289 — common: Removed since wrong existing config. `report` doesn’t have any entity anymore

**Source stance:** explanation

**Context:**

> PR 10485 ([INV-3738] feat(common): Make eventual-consistency-delay configurable), report-impl/src/main/resources/common.conf; original row 289.

**Concern stated in the source:** report has no entities and its old config was wrong.

**Source-preserving request, proposal, or question:**

> Removed since wrong existing config. `report` doesn’t have any entity anymore

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:289 · comment 571846824 · PR 10485 · 2024-11-29

Source path: `report-impl/src/main/resources/common.conf`

**Evidence:** anon-2.jsonl:289 · comment 571846824 · PR 10485 · 2024-11-29

Source path: `report-impl/src/main/resources/common.conf`

**Explicit source context (pr_title):**

> [INV-3738] feat(common): Make eventual-consistency-delay configurable

## A2-0291 — common: Removed since wrong existing config. `projection` doesn’t have any entity anymore

**Source stance:** explanation

**Context:**

> PR 10485 ([INV-3738] feat(common): Make eventual-consistency-delay configurable), projection-impl/src/main/resources/common.conf; original row 291.

**Concern stated in the source:** projection has no entities and its old config was wrong.

**Source-preserving request, proposal, or question:**

> Removed since wrong existing config. `projection` doesn’t have any entity anymore

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:291 · comment 571846792 · PR 10485 · 2024-11-29

Source path: `projection-impl/src/main/resources/common.conf`

**Evidence:** anon-2.jsonl:291 · comment 571846792 · PR 10485 · 2024-11-29

Source path: `projection-impl/src/main/resources/common.conf`

**Explicit source context (pr_title):**

> [INV-3738] feat(common): Make eventual-consistency-delay configurable

## A2-0293 — common: Correct config but still removed, cuz `composition` doesn’t have any entity anymore

**Source stance:** explanation

**Context:**

> PR 10485 ([INV-3738] feat(common): Make eventual-consistency-delay configurable), composition-impl/src/main/resources/common.conf; original row 293.

**Concern stated in the source:** composition has no entities even though the removed config was correct.

**Source-preserving request, proposal, or question:**

> Correct config but still removed, cuz `composition` doesn’t have any entity anymore

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:293 · comment 571846630 · PR 10485 · 2024-11-29

Source path: `composition-impl/src/main/resources/common.conf`

**Evidence:** anon-2.jsonl:293 · comment 571846630 · PR 10485 · 2024-11-29

Source path: `composition-impl/src/main/resources/common.conf`

**Explicit source context (pr_title):**

> [INV-3738] feat(common): Make eventual-consistency-delay configurable

## A2-0294 — common: Removed since wrong existing config. And `performance` doesn’t have any entity anymore.

**Source stance:** explanation

**Context:**

> PR 10485 ([INV-3738] feat(common): Make eventual-consistency-delay configurable), performance-impl/src/main/resources/common.conf; original row 294.

**Concern stated in the source:** performance has no entities and the removed config was wrong.

**Source-preserving request, proposal, or question:**

> Removed since wrong existing config. And `performance` doesn’t have any entity anymore.

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:294 · comment 571846769 · PR 10485 · 2024-11-29

Source path: `performance-impl/src/main/resources/common.conf`

**Evidence:** anon-2.jsonl:294 · comment 571846769 · PR 10485 · 2024-11-29

Source path: `performance-impl/src/main/resources/common.conf`

**Explicit source context (pr_title):**

> [INV-3738] feat(common): Make eventual-consistency-delay configurable

## A2-0297 — common: Removed. Existing config is wrong \+ `admin` ~~doesn’t have any entity~~ was using default value

**Source stance:** explanation

**Context:**

> PR 10485 ([INV-3738] feat(common): Make eventual-consistency-delay configurable), admin-impl/src/main/resources/common.conf; original row 297.

**Concern stated in the source:** The original no-entity claim about admin was explicitly struck through; admin was using default due to wrong config.

**Source-preserving request, proposal, or question:**

> Removed. Existing config is wrong \+ `admin` ~~doesn’t have any entity~~ was using default value
> 
> ‌

**Conditions and limits:**

- Do not reproduce the struck-through claim that admin has no entities as settled fact.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:297 · comment 571846443 · PR 10485 · 2024-11-29

Source path: `admin-impl/src/main/resources/common.conf`

**Evidence:** anon-2.jsonl:297 · comment 571846443 · PR 10485 · 2024-11-29

Source path: `admin-impl/src/main/resources/common.conf`

**Explicit source context (pr_title):**

> [INV-3738] feat(common): Make eventual-consistency-delay configurable

## A2-0300 — BackfillPlanInvestmentCmdHandler: I think this could be confusing to read, e.g. what if existing but doesn’t match the resolve? Well it cannot be, due to how we resolve. So mayb...

**Source stance:** suggestion

**Context:**

> PR 10417 (Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/BackfillPlanInvestmentCmdHandler.scala; original row 300.

**Concern stated in the source:** The existing branching appears to imply a possible existing-but-different resolved value, although resolution rules make it impossible.

**Source-preserving request, proposal, or question:**

> I think this could be confusing to read, e.g. what if existing but doesn’t match the resolve? Well it cannot be, due to how we resolve. So maybe we can write this part differently
> 
> ```
> val maybeInitialInvestmentBackfilledEvt = plan.initialInvestmentRequest match {
>   case None => Some(....)
>   case Some(_) => None
> }
> 
> val maybeRecurringInvestmentScheduleBackfilledEvt = plan.recurringInvestmentSchedule.flatMap { schedule =>
>   schedule.fundingInstructions match {
>     case None => Some(...)
>     case Some(_) => None
>   }
> }
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:300 · comment 570115418 · PR 10417 · 2024-11-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/BackfillPlanInvestmentCmdHandler.scala`

**Evidence:** anon-2.jsonl:300 · comment 570115418 · PR 10417 · 2024-11-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/BackfillPlanInvestmentCmdHandler.scala`

**Explicit source context (pr_title):**

> Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.

## A2-0301 — BaseServiceLogicImpl: The cmd is idempotent anyway, so maybe we just trigger from goal level instead? No need to double lookup

**Source stance:** suggestion

**Context:**

> PR 10417 (Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.), goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala; original row 301.

**Concern stated in the source:** The backfill command is already idempotent, making a double lookup unnecessary.

**Source-preserving request, proposal, or question:**

> The cmd is idempotent anyway, so maybe we just trigger from goal level instead? No need to double lookup

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:301 · comment 570115832 · PR 10417 · 2024-11-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:301 · comment 570115832 · PR 10417 · 2024-11-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.

## A2-0302 — UpdateInvestmentPlanInitialInvestmentRequestCmdHandler: So how do we get of this invalid data state?

**Source stance:** open-question

**Context:**

> PR 10417 (Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/UpdateInvestmentPlanInitialInvestmentRequestCmdHandler.scala; original row 302.

**Source-preserving request, proposal, or question:**

> So how do we get of this invalid data state?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:302 · comment 570116120 · PR 10417 · 2024-11-25

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/UpdateInvestmentPlanInitialInvestmentRequestCmdHandler.scala`

**Evidence:** anon-2.jsonl:302 · comment 570116120 · PR 10417 · 2024-11-25

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/UpdateInvestmentPlanInitialInvestmentRequestCmdHandler.scala`

**Explicit source context (pr_title):**

> Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.

## A2-0303 — UpdateInvestmentPlanInitialInvestmentRequestCmdHandler: And how will we sync? If there is endpoint already, let’s document it in this error msg as well

**Source stance:** open-question

**Context:**

> PR 10417 (Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/UpdateInvestmentPlanInitialInvestmentRequestCmdHandler.scala; original row 303.

**Concern stated in the source:** Operators need the problematic planId and any existing sync endpoint in the error message.

**Source-preserving request, proposal, or question:**

> And how will we sync? If there is endpoint already, let’s document it in this error msg as well
> 
> Put planId in the message so that we know which one is problematic

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:303 · comment 570151586 · PR 10417 · 2024-11-25

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/UpdateInvestmentPlanInitialInvestmentRequestCmdHandler.scala`

**Evidence:** anon-2.jsonl:303 · comment 570151586 · PR 10417 · 2024-11-25

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/UpdateInvestmentPlanInitialInvestmentRequestCmdHandler.scala`

**Explicit source context (pr_title):**

> Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.

## A2-0308 — BackfillPlanInvestmentCmdHandler: Move the resolve logic to this `case None`, and no need to check `plan.initialInvestmentRequest` anymore

**Source stance:** suggestion

**Context:**

> PR 10417 (Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/BackfillPlanInvestmentCmdHandler.scala; original row 308.

**Source-preserving request, proposal, or question:**

> Move the resolve logic to this `case None`, and no need to check `plan.initialInvestmentRequest` anymore

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:308 · comment 570149877 · PR 10417 · 2024-11-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/BackfillPlanInvestmentCmdHandler.scala`

**Evidence:** anon-2.jsonl:308 · comment 570149877 · PR 10417 · 2024-11-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/BackfillPlanInvestmentCmdHandler.scala`

**Explicit source context (pr_title):**

> Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.

## A2-0309 — BackfillPlanInvestmentCmdHandler: Wrong id

**Source stance:** observed-defect

**Context:**

> PR 10417 (Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/BackfillPlanInvestmentCmdHandler.scala; original row 309.

**Source-preserving request, proposal, or question:**

> Wrong id

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- The hunk contains PlanInitialInvestmentRequestBackfilledEvt planId/goalId/customerId assignments; source says wrong id but does not specify replacement. Preserve that unresolved scope.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:309 · comment 570149964 · PR 10417 · 2024-11-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/BackfillPlanInvestmentCmdHandler.scala`

**Evidence:** anon-2.jsonl:309 · comment 570149964 · PR 10417 · 2024-11-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/BackfillPlanInvestmentCmdHandler.scala`

**Explicit source context (hunk):**

> +            .map(InitialInvestmentRequest.fromFundingInstructions)
> +            .getOrElse(InitialInvestmentRequest.fromAmount(plan.initialInvestmentAmount))
> +          Some(
> +            PlanInitialInvestmentRequestBackfilledEvt(
> +              planId = plan.planId,
> +              goalId = plan.goalId,
> +              customerId = plan.customerId,

**Evidence:** anon-2.jsonl:309 · comment 570149964 · PR 10417 · 2024-11-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/BackfillPlanInvestmentCmdHandler.scala`

**Explicit source context (pr_title):**

> Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.

## A2-0310 — UpdateInvestmentPlanInitialInvestmentRequestCmdHandler: Not sure about refreshing the updatedAt here. Is it used for anything related to customer, if not then safe

**Source stance:** open-question

**Context:**

> PR 10417 (Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/UpdateInvestmentPlanInitialInvestmentRequestCmdHandler.scala; original row 310.

**Concern stated in the source:** Refreshing updatedAt is safe only if no customer-facing behavior relies on it; that use is unresolved.

**Source-preserving request, proposal, or question:**

> Not sure about refreshing the updatedAt here. Is it used for anything related to customer, if not then safe

**Conditions and limits:**

- Whether updatedAt is used for customer behavior is left unresolved.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:310 · comment 570152368 · PR 10417 · 2024-11-25

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/UpdateInvestmentPlanInitialInvestmentRequestCmdHandler.scala`

**Evidence:** anon-2.jsonl:310 · comment 570152368 · PR 10417 · 2024-11-25

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/UpdateInvestmentPlanInitialInvestmentRequestCmdHandler.scala`

**Explicit source context (pr_title):**

> Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.

## A2-0311 — UpdateRecurringInvestmentScheduleCmdHandler: Yea ok this shouldn’t happen in the first place. Agree let’s put error alert and skip. We will decide what to do when it happens :th...

**Source stance:** suggestion

**Context:**

> PR 10417 (Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/UpdateRecurringInvestmentScheduleCmdHandler.scala; original row 311.

**Source-preserving request, proposal, or question:**

> Yea ok this shouldn’t happen in the first place. Agree let’s put error alert and skip. We will decide what to do when it happens :thumbsup:

**Conditions and limits:**

- Agreed behavior is error alert plus skip; remediation is deliberately deferred until the invalid state occurs.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:311 · comment 570530187 · PR 10417 · 2024-11-26

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/UpdateRecurringInvestmentScheduleCmdHandler.scala`

**Evidence:** anon-2.jsonl:311 · comment 570530187 · PR 10417 · 2024-11-26

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/UpdateRecurringInvestmentScheduleCmdHandler.scala`

**Explicit source context (pr_title):**

> Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.

## A2-0315 — UpdateInvestmentPlanRecurringInvestmentScheduleCmdHandler: Let’s name these cmd as “Backfill” cmd as well? Not good to name them “Update” but actually if any change is include w...

**Source stance:** suggestion

**Context:**

> PR 10417 (Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/UpdateInvestmentPlanRecurringInvestmentScheduleCmdHandler.scala; original row 315.

**Concern stated in the source:** Update naming is misleading if any actual change results in an error.

**Source-preserving request, proposal, or question:**

> Let’s name these cmd as “Backfill” cmd as well? Not good to name them “Update” but actually if any change is include will make error log

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:315 · comment 570862707 · PR 10417 · 2024-11-27

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/UpdateInvestmentPlanRecurringInvestmentScheduleCmdHandler.scala`

**Evidence:** anon-2.jsonl:315 · comment 570862707 · PR 10417 · 2024-11-27

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/UpdateInvestmentPlanRecurringInvestmentScheduleCmdHandler.scala`

**Explicit source context (pr_title):**

> Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.

## A2-0317 — InstrumentMarketDataEventProcessorForMultiCcy: We don’t need this check here, then entity has the logic already

**Source stance:** explanation

**Context:**

> PR 10400 ([INV-3609] feat(marketdata, instrument): improve marketdata monthly changes reliability), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataEventProcessorForMultiCcy.scala; original row 317.

**Concern stated in the source:** The entity already acknowledges identical monthlyChanges with triggerFxConversion=false without events.

**Source-preserving request, proposal, or question:**

> We don’t need this check here, then entity has the logic already
> 
> ```
> if (cmd.monthlyChanges.toSet == state.monthlyChanges.toSet && cmd.triggerFxConversion.contains(false)) {
>   Effect.ack(cmd.replyTo)
> }
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:317 · comment 568222103 · PR 10400 · 2024-11-20

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataEventProcessorForMultiCcy.scala`

**Evidence:** anon-2.jsonl:317 · comment 568222103 · PR 10400 · 2024-11-20

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataEventProcessorForMultiCcy.scala`

**Explicit source context (pr_title):**

> [INV-3609] feat(marketdata, instrument): improve marketdata monthly changes reliability

## A2-0324 — MarketDataUploader: Here we want to check. It’s same rationale as `safeUploadMonthlyChanges` because we are setting `triggerFxConversion` = true, which will override the logic i...

**Source stance:** explanation

**Context:**

> PR 10400 ([INV-3609] feat(marketdata, instrument): improve marketdata monthly changes reliability), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; original row 324.

**Concern stated in the source:** triggerFxConversion=true overrides the entity guard, requiring endpoint comparison; optional false is inappropriate when data actually changes.

**Source-preserving request, proposal, or question:**

> Here we want to check. It’s same rationale as `safeUploadMonthlyChanges` because we are setting `triggerFxConversion` = true, which will override the logic in entity.
> 
> This current endpoint puts `triggerFxConversion` as Optional and default to true - but it doesn’t make sense to not trigger fx, if there is indeed updates. I think let’s remove the option, and trigger fx always

**Conditions and limits:**

- Source proposes removing triggerFxConversion option and always triggering FX when monthly changes are updated.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:324 · comment 568253582 · PR 10400 · 2024-11-20

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:324 · comment 568253582 · PR 10400 · 2024-11-20

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-3609] feat(marketdata, instrument): improve marketdata monthly changes reliability

## A2-0363 — CreateGoalWithPlansCmdHandler: ```

**Source stance:** requested-change

**Context:**

> PR 10335 (Feat/INV-3508 goal create projections), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/CreateGoalWithPlansCmdHandler.scala; original row 363.

**Source-preserving request, proposal, or question:**

> ```
> val events = GoalCreatedEvt(goal) :: List(maybeGoalCreationApprovedEvt).flatten ++ plans.map(PlanCreatedEvt(_))
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:363 · comment 564839920 · PR 10335 · 2024-11-14

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/CreateGoalWithPlansCmdHandler.scala`

**Evidence:** anon-2.jsonl:363 · comment 564839920 · PR 10335 · 2024-11-14

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/CreateGoalWithPlansCmdHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3508 goal create projections

## A2-0378 — TenantAwareInstrumentManager: Need to check whitelisting as well. Better to refactor to sharing common code, same approach as FundList/FundDetails

**Source stance:** suggestion

**Context:**

> PR 10184 ([INV-3559] feat(bff, advisory): Portfolio Builder Portfolio Summary), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/TenantAwareInstrumentManager.scala; original row 378.

**Concern stated in the source:** Whitelisting must also be checked; FundList/FundDetails share the desired approach.

**Source-preserving request, proposal, or question:**

> Need to check whitelisting as well. Better to refactor to sharing common code, same approach as FundList/FundDetails

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:378 · comment 562905956 · PR 10184 · 2024-11-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/TenantAwareInstrumentManager.scala`

**Evidence:** anon-2.jsonl:378 · comment 562905956 · PR 10184 · 2024-11-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/TenantAwareInstrumentManager.scala`

**Explicit source context (pr_title):**

> [INV-3559] feat(bff, advisory): Portfolio Builder Portfolio Summary

## A2-0476 — BffServiceImpl: Ok so my above example would be when FA performs operation on-behalf of customer, so employee would be there.

**Source stance:** suggestion

**Context:**

> PR 10258 ([INV-3639] feat(bff): Capture and propagate Customer/Employee context in BFF), bff-impl/src/main/scala/com/endowus/silver/bff/impl/BffServiceImpl.scala; original row 476.

**Concern stated in the source:** Ok so my above example would be when FA performs operation on-behalf of customer, so employee would be there.

For same endpoint to support PartnerOps user, I will need to change this `manageCustomer` guard’s logic:

* extract customerId from endpoint request properties
* query `tenantClient <- tenantService.Api.getClientById()(customerId)`
* validate:

    * if `requestWithAuthResponse.employeeIdFromToken` is available, its value must match `tenantClient.managerId`
    * else `requestWithAuthResponse.authResponse.identity.issuer.tenant.id` must match `tenantClient.tenantId`
    

‌

**Source-preserving request, proposal, or question:**

> Ok so my above example would be when FA performs operation on-behalf of customer, so employee would be there.
> 
> For same endpoint to support PartnerOps user, I will need to change this `manageCustomer` guard’s logic:
> 
> * extract customerId from endpoint request properties
> * query `tenantClient <- tenantService.Api.getClientById()(customerId)`
> * validate:
> 
>     * if `requestWithAuthResponse.employeeIdFromToken` is available, its value must match `tenantClient.managerId`
>     * else `requestWithAuthResponse.authResponse.identity.issuer.tenant.id` must match `tenantClient.tenantId`
>     
> 
> ‌

**Conditions and limits:**

- Employee token branch must match managerId; otherwise authenticated identity tenant must match tenantClient.tenantId.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:476 · comment 560738494 · PR 10258 · 2024-11-04

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/BffServiceImpl.scala`

**Evidence:** anon-2.jsonl:476 · comment 560738494 · PR 10258 · 2024-11-04

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/BffServiceImpl.scala`

**Explicit source context (pr_title):**

> [INV-3639] feat(bff): Capture and propagate Customer/Employee context in BFF

## A2-0502 — package: Same here, let’s not stamp it here. Rather we add the resolved fee to `CreateInvestmentPlanCmd` as separate field like other cmd I think

**Source stance:** suggestion

**Context:**

> PR 10096 (Resolve INV-3454: Add transaction fee config in investment requests and populate from necessary places.), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/models/package.scala; original row 502.

**Concern stated in the source:** Same here, let’s not stamp it here. Rather we add the resolved fee to `CreateInvestmentPlanCmd` as separate field like other cmd I think

**Source-preserving request, proposal, or question:**

> Same here, let’s not stamp it here. Rather we add the resolved fee to `CreateInvestmentPlanCmd` as separate field like other cmd I think

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:502 · comment 553466655 · PR 10096 · 2024-10-16

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/models/package.scala`

**Evidence:** anon-2.jsonl:502 · comment 553466655 · PR 10096 · 2024-10-16

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/models/package.scala`

**Explicit source context (pr_title):**

> Resolve INV-3454: Add transaction fee config in investment requests and populate from necessary places.

## A2-0505 — package: Should we drop this field in the cmd?

**Source stance:** open-question

**Context:**

> PR 10096 (Resolve INV-3454: Add transaction fee config in investment requests and populate from necessary places.), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/ces/commands/package.scala; original row 505.

**Source-preserving request, proposal, or question:**

> Should we drop this field in the cmd?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:505 · comment 553475001 · PR 10096 · 2024-10-16

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/ces/commands/package.scala`

**Evidence:** anon-2.jsonl:505 · comment 553475001 · PR 10096 · 2024-10-16

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/ces/commands/package.scala`

**Explicit source context (pr_title):**

> Resolve INV-3454: Add transaction fee config in investment requests and populate from necessary places.

## A2-0520 — HkFeeManagerProjection: There is no tax in HK at all, so maybe simpler solution would be to have `HkFeeManagerProjection` only handle `FeeChargeDiscountAppliedEvt` which would t...

**Source stance:** suggestion

**Context:**

> PR 10103 (Release/EN-3547 hk fee charge), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkFeeManagerProjection.scala; original row 520.

**Concern stated in the source:** There is no tax in HK at all, so maybe simpler solution would be to have `HkFeeManagerProjection` only handle `FeeChargeDiscountAppliedEvt` which would trigger `InitiateFeeRedemptionCmd` always.

Original intention of making `FeeManagerProjection` region aware is that we can support different discount/tax flow \(not just basic injection of taxHelper\). E.g. South Korean would tax first and discount later

**Source-preserving request, proposal, or question:**

> There is no tax in HK at all, so maybe simpler solution would be to have `HkFeeManagerProjection` only handle `FeeChargeDiscountAppliedEvt` which would trigger `InitiateFeeRedemptionCmd` always.
> 
> Original intention of making `FeeManagerProjection` region aware is that we can support different discount/tax flow \(not just basic injection of taxHelper\). E.g. South Korean would tax first and discount later

**Conditions and limits:**

- HK no-tax handling and possible South Korean tax-before-discount are region-flow examples; future flows are not implemented facts.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:520 · comment 547220574 · PR 10103 · 2024-10-01

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkFeeManagerProjection.scala`

**Evidence:** anon-2.jsonl:520 · comment 547220574 · PR 10103 · 2024-10-01

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkFeeManagerProjection.scala`

**Explicit source context (pr_title):**

> Release/EN-3547 hk fee charge

## A2-0534 — HkFeeManagerEntityTest: We don’t need this test cuz there is no split logic at entity level?

**Source stance:** open-question

**Context:**

> PR 10103 (Release/EN-3547 hk fee charge), charge-impl/src/test/scala/com/endowus/silver/charge/impl/HkFeeManagerEntityTest.scala; original row 534.

**Concern stated in the source:** We don’t need this test cuz there is no split logic at entity level?

**Source-preserving request, proposal, or question:**

> We don’t need this test cuz there is no split logic at entity level?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:534 · comment 549740654 · PR 10103 · 2024-10-07

Source path: `charge-impl/src/test/scala/com/endowus/silver/charge/impl/HkFeeManagerEntityTest.scala`

**Evidence:** anon-2.jsonl:534 · comment 549740654 · PR 10103 · 2024-10-07

Source path: `charge-impl/src/test/scala/com/endowus/silver/charge/impl/HkFeeManagerEntityTest.scala`

**Explicit source context (pr_title):**

> Release/EN-3547 hk fee charge

## A2-0536 — HkCustomerDailyAltsFeesCalculator: Actually this const makes me more paranoid and having to check in 2 places to ensure `FiveHundredThousand` having the correct value. However w...

**Source stance:** suggestion

**Context:**

> PR 10103 (Release/EN-3547 hk fee charge), charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/hk/HkCustomerDailyAltsFeesCalculator.scala; original row 536.

**Concern stated in the source:** Actually this const makes me more paranoid and having to check in 2 places to ensure `FiveHundredThousand` having the correct value. However we just keep the constant here \(it’s not like we would refactor `FiveHundredThousand` to another value anyway\). And you can add underscore to make it easier on the eyes, e.g. `500_000`

**Source-preserving request, proposal, or question:**

> Actually this const makes me more paranoid and having to check in 2 places to ensure `FiveHundredThousand` having the correct value. However we just keep the constant here \(it’s not like we would refactor `FiveHundredThousand` to another value anyway\). And you can add underscore to make it easier on the eyes, e.g. `500_000`

**Conditions and limits:**

- Preserve the literal 500_000 formatting example and reluctance to create a FiveHundredThousand constant.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:536 · comment 549763014 · PR 10103 · 2024-10-07

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/hk/HkCustomerDailyAltsFeesCalculator.scala`

**Evidence:** anon-2.jsonl:536 · comment 549763014 · PR 10103 · 2024-10-07

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/hk/HkCustomerDailyAltsFeesCalculator.scala`

**Explicit source context (pr_title):**

> Release/EN-3547 hk fee charge

## A2-0537 — HkFeeManagerEntityTest: There is no logical change in the entity/cmd handler. It’s better to have the waiver bit injected, and keep the existing test in tact. Then you can unit ...

**Source stance:** suggestion

**Context:**

> PR 10103 (Release/EN-3547 hk fee charge), charge-impl/src/test/scala/com/endowus/silver/charge/impl/HkFeeManagerEntityTest.scala; original row 537.

**Concern stated in the source:** There is no logical change in the entity/cmd handler. It’s better to have the waiver bit injected, and keep the existing test in tact. Then you can unit test the waiver limit in isolation

**Source-preserving request, proposal, or question:**

> There is no logical change in the entity/cmd handler. It’s better to have the waiver bit injected, and keep the existing test in tact. Then you can unit test the waiver limit in isolation

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:537 · comment 549763340 · PR 10103 · 2024-10-07

Source path: `charge-impl/src/test/scala/com/endowus/silver/charge/impl/HkFeeManagerEntityTest.scala`

**Evidence:** anon-2.jsonl:537 · comment 549763340 · PR 10103 · 2024-10-07

Source path: `charge-impl/src/test/scala/com/endowus/silver/charge/impl/HkFeeManagerEntityTest.scala`

**Explicit source context (pr_title):**

> Release/EN-3547 hk fee charge

## A2-0544 — HkChargeCommunicationProjection: This logic actually exists in `InitiateFeeRedemptionCmdHandler`, it’s best we rely on sequence of events, rather than duplicating it again.

**Source stance:** suggestion

**Context:**

> PR 10103 (Release/EN-3547 hk fee charge), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkChargeCommunicationProjection.scala; original row 544.

**Concern stated in the source:** This logic actually exists in `InitiateFeeRedemptionCmdHandler`, it’s best we rely on sequence of events, rather than duplicating it again.

The communication logic in fact can be region agnostic as well \(the same way `InitiateFeeRedemptionCmdHandler` doesn’t care about sg or hk\). We can simply use the `redemptionDetails` \(instead of using amount from `discountDetails`, and having to assume that there is no tax involved\)

```
event.feeChargeRequest.redemptionDetails match {
  case Some(redemptionDetails) =>
    redemptionDetails.redeemedAmount match {
      case Some(chargeAmount) =>
        ...communication logic goes here...
      case None =>
        logger.error("... <unexpected-please-check> ... ")
        Future.successful(Done)
    }
  case None =>
    // waived without vouchers
    Future.successful(Done)
}
```

‌

**Source-preserving request, proposal, or question:**

> This logic actually exists in `InitiateFeeRedemptionCmdHandler`, it’s best we rely on sequence of events, rather than duplicating it again.
> 
> The communication logic in fact can be region agnostic as well \(the same way `InitiateFeeRedemptionCmdHandler` doesn’t care about sg or hk\). We can simply use the `redemptionDetails` \(instead of using amount from `discountDetails`, and having to assume that there is no tax involved\)
> 
> ```
> event.feeChargeRequest.redemptionDetails match {
>   case Some(redemptionDetails) =>
>     redemptionDetails.redeemedAmount match {
>       case Some(chargeAmount) =>
>         ...communication logic goes here...
>       case None =>
>         logger.error("... <unexpected-please-check> ... ")
>         Future.successful(Done)
>     }
>   case None =>
>     // waived without vouchers
>     Future.successful(Done)
> }
> ```
> 
> ‌

**Conditions and limits:**

- Communication follows FeeChargeCompletedEvt redemptionDetails: Some redeemedAmount sends; missing redeemedAmount logs unexpected and returns Done; None redemptionDetails is waived without vouchers and returns Done.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:544 · comment 550155826 · PR 10103 · 2024-10-08

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkChargeCommunicationProjection.scala`

**Evidence:** anon-2.jsonl:544 · comment 550155826 · PR 10103 · 2024-10-08

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/hk/HkChargeCommunicationProjection.scala`

**Explicit source context (pr_title):**

> Release/EN-3547 hk fee charge

## A2-0558 — DistributionCalculatorHelperHk: Can we retry \+ fallback to entity for this, just to be on safe side?

**Source stance:** suggestion

**Context:**

> PR 10121 (TT-5089 remove cache customer status for HK trailer rebate), rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/distro/DistributionCalculatorHelperHk.scala; original row 558.

**Concern stated in the source:** Can we retry \+ fallback to entity for this, just to be on safe side?

**Source-preserving request, proposal, or question:**

> Can we retry \+ fallback to entity for this, just to be on safe side?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:558 · comment 549741742 · PR 10121 · 2024-10-07

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/distro/DistributionCalculatorHelperHk.scala`

**Evidence:** anon-2.jsonl:558 · comment 549741742 · PR 10121 · 2024-10-07

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/distro/DistributionCalculatorHelperHk.scala`

**Explicit source context (pr_title):**

> TT-5089 remove cache customer status for HK trailer rebate

## A2-0579 — UpdateProductCharacteristicsCmdHandler: If this cmd handler does not support B2B types, let match and reject it outside, then pass in only the resolved B2C type

**Source stance:** explanation

**Context:**

> PR 10010 (Feat/INV-3472 b2b product line), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/UpdateProductCharacteristicsCmdHandler.scala; original row 579.

**Concern stated in the source:** If this cmd handler does not support B2B types, let match and reject it outside, then pass in only the resolved B2C type

```
def handleUpdateProductCharacteristicsCmd(cmd: UpdateProductCharacteristicsCmd, state: GoalState): Reply = {
  cmd.newProductLineAndIntent match {
      case x: productline.B2CProductLineAndIntent =>
        handleUpdateB2CProductCharacteristicsCmd(cmd, state, x)
      case _: productline.B2BProductLineAndIntent =>
        Effect.reply(cmd.replyTo)(
          GoalSvcException("Invalid product line and intent, only supports B2C product lines", GoalSvcErrorType.???).error
        )
  }
} 
```

‌

If this cmd handler can be generic, then we simply don’t emit the B2C events instead of throwing

**Source-preserving request, proposal, or question:**

> If this cmd handler does not support B2B types, let match and reject it outside, then pass in only the resolved B2C type
> 
> ```
> def handleUpdateProductCharacteristicsCmd(cmd: UpdateProductCharacteristicsCmd, state: GoalState): Reply = {
>   cmd.newProductLineAndIntent match {
>       case x: productline.B2CProductLineAndIntent =>
>         handleUpdateB2CProductCharacteristicsCmd(cmd, state, x)
>       case _: productline.B2BProductLineAndIntent =>
>         Effect.reply(cmd.replyTo)(
>           GoalSvcException("Invalid product line and intent, only supports B2C product lines", GoalSvcErrorType.???).error
>         )
>   }
> } 
> ```
> 
> ‌
> 
> If this cmd handler can be generic, then we simply don’t emit the B2C events instead of throwing

**Conditions and limits:**

- Two branches depend on intended command scope: reject B2B before B2C-only handling, or if generic avoid emitting B2C events instead of throwing.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:579 · comment 545899290 · PR 10010 · 2024-09-26

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/UpdateProductCharacteristicsCmdHandler.scala`

**Evidence:** anon-2.jsonl:579 · comment 545899290 · PR 10010 · 2024-09-26

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/UpdateProductCharacteristicsCmdHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3472 b2b product line

## A2-0582 — UpdateProductCharacteristicsCmdHandler: Let’s also validate that we can’t change B2C ↔︎ B2B productlines?

**Source stance:** suggestion

**Context:**

> PR 10010 (Feat/INV-3472 b2b product line), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/UpdateProductCharacteristicsCmdHandler.scala; original row 582.

**Concern stated in the source:** Let’s also validate that we can’t change B2C ↔︎ B2B productlines?

**Source-preserving request, proposal, or question:**

> Let’s also validate that we can’t change B2C ↔︎ B2B productlines?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:582 · comment 545964766 · PR 10010 · 2024-09-26

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/UpdateProductCharacteristicsCmdHandler.scala`

**Evidence:** anon-2.jsonl:582 · comment 545964766 · PR 10010 · 2024-09-26

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/UpdateProductCharacteristicsCmdHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3472 b2b product line

## A2-0590 — UpdateProductCharacteristicsCmdHandler: private

**Source stance:** suggestion

**Context:**

> PR 10010 (Feat/INV-3472 b2b product line), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/UpdateProductCharacteristicsCmdHandler.scala; original row 590.

**Source-preserving request, proposal, or question:**

> private

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:590 · comment 545964502 · PR 10010 · 2024-09-26

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/UpdateProductCharacteristicsCmdHandler.scala`

**Evidence:** anon-2.jsonl:590 · comment 545964502 · PR 10010 · 2024-09-26

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/UpdateProductCharacteristicsCmdHandler.scala`

**Explicit source context (hunk):**

> +  }
> +
> +  private def generateEventsForB2BProductCharacteristicsCmd(cmd: UpdateProductCharacteristicsCmd, state: GoalState, newProductLine: productline.B2BProductLineAndIntent): List[GoalEvt] = {
> +    //TODO create b2b specific product characteristic changed events
> +    List.empty
> +  }
> +

**Evidence:** anon-2.jsonl:590 · comment 545964502 · PR 10010 · 2024-09-26

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/UpdateProductCharacteristicsCmdHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3472 b2b product line

## A2-0592 — UpdateProductCharacteristicsCmdHandler: immutable List instead? Same for b2b

**Source stance:** suggestion

**Context:**

> PR 10010 (Feat/INV-3472 b2b product line), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/UpdateProductCharacteristicsCmdHandler.scala; original row 592.

**Source-preserving request, proposal, or question:**

> immutable List instead? Same for b2b

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:592 · comment 545964247 · PR 10010 · 2024-09-26

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/UpdateProductCharacteristicsCmdHandler.scala`

**Evidence:** anon-2.jsonl:592 · comment 545964247 · PR 10010 · 2024-09-26

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/UpdateProductCharacteristicsCmdHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3472 b2b product line

## A2-0596 — ModelPortfolioEntity: Can we update this to check TAA changed OR EffectiveDate changed

**Source stance:** suggestion

**Context:**

> PR 10034 (Resolve INV-3485: Changes to wait for response in subscriber, react to PortfolioAllocationTargetUpdatedMsg in rebalance.), portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/entities/portfolio/ModelPortfolioEntity.scala; original row 596.

**Concern stated in the source:** Can we update this to check TAA changed OR EffectiveDate changed

**Source-preserving request, proposal, or question:**

> Can we update this to check TAA changed OR EffectiveDate changed

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:596 · comment 544819651 · PR 10034 · 2024-09-24

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/entities/portfolio/ModelPortfolioEntity.scala`

**Evidence:** anon-2.jsonl:596 · comment 544819651 · PR 10034 · 2024-09-24

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/entities/portfolio/ModelPortfolioEntity.scala`

**Explicit source context (pr_title):**

> Resolve INV-3485: Changes to wait for response in subscriber, react to PortfolioAllocationTargetUpdatedMsg in rebalance.

## A2-0597 — ModelPortfolioEntity: So there are 2 events:

**Source stance:** suggestion

**Context:**

> PR 10034 (Resolve INV-3485: Changes to wait for response in subscriber, react to PortfolioAllocationTargetUpdatedMsg in rebalance.), portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/entities/portfolio/ModelPortfolioEntity.scala; original row 597.

**Concern stated in the source:** So there are 2 events:

* `PortfolioMovedToNewAllocationTargetEvt` is purely for TAA change. You can see `handleUpdateCurrentAllocationTargetCmd` \(the real cmd handler for emitting this evt\) only checks `effectiveDate` and `List[AllocationTarget]`
* `PortfolioAllocationTargetUpdatedEvt` is intended to update underlying instrument profile \(of the `AllocationTarget`\). We don’t really need this evt for the clone purpose. And even if needed, it should come via the instrument cloning instead.

‌

Advisory’s ProductPortfolio handles both PortfolioMovedToNewAllocationTargetMsg and PortfolioAllocationTargetUpdatedMsg. I don’t remember if we have migrated everything to refresh instrument data always, but this entity has a rework as we discussed in the past \(it just needs to store the tagging, and fetch fresh or projection portfolio/instrument data\). I think until then, let’s just leave it.

‌

**Source-preserving request, proposal, or question:**

> So there are 2 events:
> 
> * `PortfolioMovedToNewAllocationTargetEvt` is purely for TAA change. You can see `handleUpdateCurrentAllocationTargetCmd` \(the real cmd handler for emitting this evt\) only checks `effectiveDate` and `List[AllocationTarget]`
> * `PortfolioAllocationTargetUpdatedEvt` is intended to update underlying instrument profile \(of the `AllocationTarget`\). We don’t really need this evt for the clone purpose. And even if needed, it should come via the instrument cloning instead.
> 
> ‌
> 
> Advisory’s ProductPortfolio handles both PortfolioMovedToNewAllocationTargetMsg and PortfolioAllocationTargetUpdatedMsg. I don’t remember if we have migrated everything to refresh instrument data always, but this entity has a rework as we discussed in the past \(it just needs to store the tagging, and fetch fresh or projection portfolio/instrument data\). I think until then, let’s just leave it.
> 
> ‌

**Conditions and limits:**

- Keep TAA/effectiveDate change events separate from instrument-profile update events. ProductPortfolio still handles both, with broader redesign deferred.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:597 · comment 545564269 · PR 10034 · 2024-09-25

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/entities/portfolio/ModelPortfolioEntity.scala`

**Evidence:** anon-2.jsonl:597 · comment 545564269 · PR 10034 · 2024-09-25

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/entities/portfolio/ModelPortfolioEntity.scala`

**Explicit source context (pr_title):**

> Resolve INV-3485: Changes to wait for response in subscriber, react to PortfolioAllocationTargetUpdatedMsg in rebalance.

## A2-0598 — ModelPortfolioEntity: It’s not a problem/caveat in advisory, cuz it handles both `PortfolioMovedToNewTargetAllocationMsg` and `PortfolioAllocationTargetUpdatedMsg`

**Source stance:** explanation

**Context:**

> PR 10034 (Resolve INV-3485: Changes to wait for response in subscriber, react to PortfolioAllocationTargetUpdatedMsg in rebalance.), portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/entities/portfolio/ModelPortfolioEntity.scala; original row 598.

**Concern stated in the source:** It’s not a problem/caveat in advisory, cuz it handles both `PortfolioMovedToNewTargetAllocationMsg` and `PortfolioAllocationTargetUpdatedMsg`

**Source-preserving request, proposal, or question:**

> It’s not a problem/caveat in advisory, cuz it handles both `PortfolioMovedToNewTargetAllocationMsg` and `PortfolioAllocationTargetUpdatedMsg`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:598 · comment 545583100 · PR 10034 · 2024-09-25

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/entities/portfolio/ModelPortfolioEntity.scala`

**Evidence:** anon-2.jsonl:598 · comment 545583100 · PR 10034 · 2024-09-25

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/entities/portfolio/ModelPortfolioEntity.scala`

**Explicit source context (pr_title):**

> Resolve INV-3485: Changes to wait for response in subscriber, react to PortfolioAllocationTargetUpdatedMsg in rebalance.

## A2-0604 — HkFundSmartCollectionManager: This step is common between the two. Should be able to refactor a bit so that we only branch on customerId when checking corp profile. Same for SG

**Source stance:** suggestion

**Context:**

> PR 9835 (Resolve INV-3401: Expose endpoints for instrument/collection details for public webflow), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkFundSmartCollectionManager.scala; original row 604.

**Concern stated in the source:** This step is common between the two. Should be able to refactor a bit so that we only branch on customerId when checking corp profile. Same for SG

**Source-preserving request, proposal, or question:**

> This step is common between the two. Should be able to refactor a bit so that we only branch on customerId when checking corp profile. Same for SG

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:604 · comment 544376194 · PR 9835 · 2024-09-23

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkFundSmartCollectionManager.scala`

**Evidence:** anon-2.jsonl:604 · comment 544376194 · PR 9835 · 2024-09-23

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkFundSmartCollectionManager.scala`

**Explicit source context (pr_title):**

> Resolve INV-3401: Expose endpoints for instrument/collection details for public webflow

## A2-0646 — GoalModifyBehaviourHelpers: Same here. Switch to calling the new `findProductPortfolio(advisoryTag, newRiskTarget)`

**Source stance:** suggestion

**Context:**

> PR 9715 ([INV-3238] feat(advisory): create apis for goal modify flow), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/GoalModifyBehaviourHelpers.scala; original row 646.

**Source-preserving request, proposal, or question:**

> Same here. Switch to calling the new `findProductPortfolio(advisoryTag, newRiskTarget)`
> 
> Then can refactor common code with above method

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:646 · comment 531576677 · PR 9715 · 2024-08-16

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/GoalModifyBehaviourHelpers.scala`

**Evidence:** anon-2.jsonl:646 · comment 531576677 · PR 9715 · 2024-08-16

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/GoalModifyBehaviourHelpers.scala`

**Explicit source context (pr_title):**

> [INV-3238] feat(advisory): create apis for goal modify flow

## A2-0693 — DividendEntity: Let’s check for all states - you can’t delete if data mismatch, regardless of state

**Source stance:** explanation

**Context:**

> PR 9784 (Resolve INV-3403: Add checks in handlers and populate necessary data in commands for duplicate distributions.), dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/DividendEntity.scala; original row 693.

**Concern stated in the source:** Let’s check for all states - you can’t delete if data mismatch, regardless of state

**Source-preserving request, proposal, or question:**

> Let’s check for all states - you can’t delete if data mismatch, regardless of state

**Conditions and limits:**

- Dividend-data mismatch blocks deletion in every state.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:693 · comment 532118181 · PR 9784 · 2024-08-19

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/DividendEntity.scala`

**Evidence:** anon-2.jsonl:693 · comment 532118181 · PR 9784 · 2024-08-19

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/DividendEntity.scala`

**Explicit source context (pr_title):**

> Resolve INV-3403: Add checks in handlers and populate necessary data in commands for duplicate distributions.

## A2-0694 — DividendEntity: Let’s use the new check method?

**Source stance:** suggestion

**Context:**

> PR 9784 (Resolve INV-3403: Add checks in handlers and populate necessary data in commands for duplicate distributions.), dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/DividendEntity.scala; original row 694.

**Source-preserving request, proposal, or question:**

> Let’s use the new check method?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:694 · comment 532118959 · PR 9784 · 2024-08-19

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/DividendEntity.scala`

**Evidence:** anon-2.jsonl:694 · comment 532118959 · PR 9784 · 2024-08-19

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/DividendEntity.scala`

**Explicit source context (pr_title):**

> Resolve INV-3403: Add checks in handlers and populate necessary data in commands for duplicate distributions.

## A2-0695 — DividendEntity: Let’s give more context for all these error message. We want to warn support person that data mismatch, and that we are ignoring the command, please investigate ...

**Source stance:** suggestion

**Context:**

> PR 9784 (Resolve INV-3403: Add checks in handlers and populate necessary data in commands for duplicate distributions.), dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/DividendEntity.scala; original row 695.

**Concern stated in the source:** Let’s give more context for all these error message. We want to warn support person that data mismatch, and that we are ignoring the command, please investigate the resolve the root cause of mismatch and reattempt the flow, e.g. delete clashed unit dividends and redistribute

**Source-preserving request, proposal, or question:**

> Let’s give more context for all these error message. We want to warn support person that data mismatch, and that we are ignoring the command, please investigate the resolve the root cause of mismatch and reattempt the flow, e.g. delete clashed unit dividends and redistribute

**Conditions and limits:**

- Errors should explain command is ignored, investigate/resolve mismatch, then reattempt; example is deleting clashed unit dividends and redistributing.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:695 · comment 532120004 · PR 9784 · 2024-08-19

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/DividendEntity.scala`

**Evidence:** anon-2.jsonl:695 · comment 532120004 · PR 9784 · 2024-08-19

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/DividendEntity.scala`

**Explicit source context (pr_title):**

> Resolve INV-3403: Add checks in handlers and populate necessary data in commands for duplicate distributions.

## A2-0696 — Review: Since we do not support topping up unit dividend on top of existing \(cash or unit\) dividend at all, let’s also check the trigger endpoint of unit dividend, and add que...

**Source stance:** suggestion

**Context:**

> PR 9784 (Resolve INV-3403: Add checks in handlers and populate necessary data in commands for duplicate distributions.), no inline path; original row 696.

**Concern stated in the source:** Since we do not support topping up unit dividend on top of existing \(cash or unit\) dividend at all, let’s also check the trigger endpoint of unit dividend, and add query readside of DividendEntity there and reject such request if any entries already exist

**Source-preserving request, proposal, or question:**

> Since we do not support topping up unit dividend on top of existing \(cash or unit\) dividend at all, let’s also check the trigger endpoint of unit dividend, and add query readside of DividendEntity there and reject such request if any entries already exist

**Conditions and limits:**

- Unit dividends cannot top up existing cash or unit dividends; trigger endpoint should reject any readside entry.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:696 · comment 532121285 · PR 9784 · 2024-08-19

**Evidence:** anon-2.jsonl:696 · comment 532121285 · PR 9784 · 2024-08-19

**Explicit source context (pr_title):**

> Resolve INV-3403: Add checks in handlers and populate necessary data in commands for duplicate distributions.

## A2-0718 — PortfolioMonthlyChangesHelper: I think there are 2 types of race conditions we might see here:

**Source stance:** observed-defect

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala; original row 718.

**Concern stated in the source:** I think there are 2 types of race conditions we might see here:

1. We get event that instrument mc is updated, and we trigger this method which will query instrument mc from readside - that might not have latest data yet… cuz they are 2 independent projections

    * We override the data for the instrument being updated, but it’s not bullet proof, e.g. db projection is super lagged for some reason
    
        * event of instrumentA, its data A2 is overridden on top of existing readside A1 & B1
        * then event of instrumentB, its data B2 is overridden on top of stale A1 & B1
        
    
2. Multiple instruments might be updated at once, each of them triggering this method… their upsert might override each other

    * This was protected with Portfolio entity last time. So we might need some impl of optimistic locking here
    

‌

**Source-preserving request, proposal, or question:**

> I think there are 2 types of race conditions we might see here:
> 
> 1. We get event that instrument mc is updated, and we trigger this method which will query instrument mc from readside - that might not have latest data yet… cuz they are 2 independent projections
> 
>     * We override the data for the instrument being updated, but it’s not bullet proof, e.g. db projection is super lagged for some reason
>     
>         * event of instrumentA, its data A2 is overridden on top of existing readside A1 & B1
>         * then event of instrumentB, its data B2 is overridden on top of stale A1 & B1
>         
>     
> 2. Multiple instruments might be updated at once, each of them triggering this method… their upsert might override each other
> 
>     * This was protected with Portfolio entity last time. So we might need some impl of optimistic locking here
>     
> 
> ‌

**Conditions and limits:**

- Two separate races remain: independent projection lag can pair new B2 with stale A1 despite per-event override, and concurrent instrument-triggered portfolio upserts can overwrite each other. Optimistic locking is proposed as entity replacement protection.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:718 · comment 524670185 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala`

**Evidence:** anon-2.jsonl:718 · comment 524670185 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0747 — DividendEntity: Let’s log error for both `BrokerAccountReinvestDividendCmd` and `BrokerAccountDistributeDividendCmd` if dividend data mismatch between entity and cmd. So that if...

**Source stance:** observed-defect

**Context:**

> PR 9780 (Resolve INV-3403: Unwire BrokerAccountDividendsMigrationProjection.), dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/DividendEntity.scala; original row 747.

**Concern stated in the source:** Let’s log error for both `BrokerAccountReinvestDividendCmd` and `BrokerAccountDistributeDividendCmd` if dividend data mismatch between entity and cmd. So that if we run into this issue again, we have Sentry alerts, instead of silence ignore

**Source-preserving request, proposal, or question:**

> Let’s log error for both `BrokerAccountReinvestDividendCmd` and `BrokerAccountDistributeDividendCmd` if dividend data mismatch between entity and cmd. So that if we run into this issue again, we have Sentry alerts, instead of silence ignore

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:747 · comment 531690399 · PR 9780 · 2024-08-16

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/DividendEntity.scala`

**Evidence:** anon-2.jsonl:747 · comment 531690399 · PR 9780 · 2024-08-16

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/DividendEntity.scala`

**Explicit source context (pr_title):**

> Resolve INV-3403: Unwire BrokerAccountDividendsMigrationProjection.

## A2-0748 — DividendEntity: You need to handle this `BrokerAccountDeleteDividendCmd`, not `DeleteCmd`

**Source stance:** observed-defect

**Context:**

> PR 9780 (Resolve INV-3403: Unwire BrokerAccountDividendsMigrationProjection.), dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/DividendEntity.scala; original row 748.

**Concern stated in the source:** You need to handle this `BrokerAccountDeleteDividendCmd`, not `DeleteCmd`

**Source-preserving request, proposal, or question:**

> You need to handle this `BrokerAccountDeleteDividendCmd`, not `DeleteCmd`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:748 · comment 531690493 · PR 9780 · 2024-08-16

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/DividendEntity.scala`

**Evidence:** anon-2.jsonl:748 · comment 531690493 · PR 9780 · 2024-08-16

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/DividendEntity.scala`

**Explicit source context (pr_title):**

> Resolve INV-3403: Unwire BrokerAccountDividendsMigrationProjection.

## A2-0750 — DividendEntity: This entity doesn’t even distinguish between unit vs cash dividend. So I don’t know we can safely handle this….

**Source stance:** open-question

**Context:**

> PR 9780 (Resolve INV-3403: Unwire BrokerAccountDividendsMigrationProjection.), dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/DividendEntity.scala; original row 750.

**Concern stated in the source:** This entity doesn’t even distinguish between unit vs cash dividend. So I don’t know we can safely handle this….

**Source-preserving request, proposal, or question:**

> This entity doesn’t even distinguish between unit vs cash dividend. So I don’t know we can safely handle this….

**Conditions and limits:**

- Safe handling remains unresolved because the entity cannot distinguish unit vs cash dividends.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:750 · comment 531692200 · PR 9780 · 2024-08-16

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/DividendEntity.scala`

**Evidence:** anon-2.jsonl:750 · comment 531692200 · PR 9780 · 2024-08-16

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/DividendEntity.scala`

**Explicit source context (pr_title):**

> Resolve INV-3403: Unwire BrokerAccountDividendsMigrationProjection.

## A2-0753 — SplitCashReservationsForFullRedemptionFeeChargeCmdHandler: It starts from None, and then capture the fee charge amount so far for the full redemption. It might have 2 fee charge...

**Source stance:** explanation

**Context:**

> PR 9750 ([INV-3155] feat(redemption): Idempotency for fee redemption of full redemption), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/handlers/SplitCashReservationsForFullRedemptionFeeChargeCmdHandler.scala; original row 753.

**Concern stated in the source:** It starts from None, and then capture the fee charge amount so far for the full redemption. It might have 2 fee charges, for prev and current quarter.

Existing impl in `OverrideRedemptionCashReservationsCmdHandler` do lookup from state, but since we already protect the idempotency here, we can simply apply the incremental amount

**Source-preserving request, proposal, or question:**

> It starts from None, and then capture the fee charge amount so far for the full redemption. It might have 2 fee charges, for prev and current quarter.
> 
> Existing impl in `OverrideRedemptionCashReservationsCmdHandler` do lookup from state, but since we already protect the idempotency here, we can simply apply the incremental amount

**Conditions and limits:**

- Accrued fee-charge amount begins None and can include prior plus current quarter. Protected idempotency permits incremental application rather than re-reading current state.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:753 · comment 530672407 · PR 9750 · 2024-08-13

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/handlers/SplitCashReservationsForFullRedemptionFeeChargeCmdHandler.scala`

**Evidence:** anon-2.jsonl:753 · comment 530672407 · PR 9750 · 2024-08-13

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/handlers/SplitCashReservationsForFullRedemptionFeeChargeCmdHandler.scala`

**Explicit source context (pr_title):**

> [INV-3155] feat(redemption): Idempotency for fee redemption of full redemption

## A2-0760 — CustomerStatusHelper: Let’s use same approach as goal svc

**Source stance:** suggestion

**Context:**

> PR 9702 (Feat/INV-3237/create plan upsert apis), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/customer/CustomerStatusHelper.scala; original row 760.

**Concern stated in the source:** Let’s use same approach as goal svc

```
def customerService: BaseCustomerService

def getInvestorTypeFromTradingAccount(customerId, tradingAccountType) = {
  InvestorType.getInvestorTypeFromTradingAccount(
    tradingAccountType,
    customerService.getRegionalCustomer(customerId).invoke().map(getCashInvestorType)
  )
}
```

‌

Let’s also make sure we still have isActive check in place after this refactoring

**Source-preserving request, proposal, or question:**

> Let’s use same approach as goal svc
> 
> ```
> def customerService: BaseCustomerService
> 
> def getInvestorTypeFromTradingAccount(customerId, tradingAccountType) = {
>   InvestorType.getInvestorTypeFromTradingAccount(
>     tradingAccountType,
>     customerService.getRegionalCustomer(customerId).invoke().map(getCashInvestorType)
>   )
> }
> ```
> 
> ‌
> 
> Let’s also make sure we still have isActive check in place after this refactoring

**Conditions and limits:**

- Refactor still must preserve isActive validation.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:760 · comment 528914681 · PR 9702 · 2024-08-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/customer/CustomerStatusHelper.scala`

**Evidence:** anon-2.jsonl:760 · comment 528914681 · PR 9702 · 2024-08-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/customer/CustomerStatusHelper.scala`

**Explicit source context (pr_title):**

> Feat/INV-3237/create plan upsert apis

## A2-0776 — SgRecommendedInvestmentManager: Can we refactor so that we can avoid calling Option.get

**Source stance:** suggestion

**Context:**

> PR 9739 (Feat/EN-3683 sg create a new api to get recommended investment amount), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManager.scala; original row 776.

**Concern stated in the source:** Can we refactor so that we can avoid calling Option.get

Example:

```
private case class MyInfoCpfRecommendation(
  myInfoUpdatedAt: LocalDate,
  cpfInvestibleBalance: BigDecimal,
  cpfMonthlyContribution: Option[BigDecimal]
)

def deriveRecommandationFromMyInfo(myInfoFinancialData: MyInfoCustomerFinancialDataDto): Option[RecommendedInvestmentDto] = ???
def deriveRecommandationFromIncomeTier(level: TierLevel, recommndationMapping: Map[TierLevel, BigDecimal]): RecommendedInvestmentDto = ???
```

‌

then you can use it here

```
val myInfoFinancialData = getMyInfoFinancialData(maybeCustomerMyInfoFinancialData, onboardingData)
deriveRecommandationFromMyInfo(myInfoFinancialData)
  .getOrElse(deriveRecommandationFromIncomeTier(level, RecommendedRecurringMonthlyAmountCpfBasedOnIncomeLevelMap))
```

‌

and for SGD cash we just use

```
deriveRecommandationFromIncomeTier(level, RecommendedRecurringMonthlyAmountSgdCashBasedOnIncomeLevelMap)
```

‌

**Source-preserving request, proposal, or question:**

> Can we refactor so that we can avoid calling Option.get
> 
> Example:
> 
> ```
> private case class MyInfoCpfRecommendation(
>   myInfoUpdatedAt: LocalDate,
>   cpfInvestibleBalance: BigDecimal,
>   cpfMonthlyContribution: Option[BigDecimal]
> )
> 
> def deriveRecommandationFromMyInfo(myInfoFinancialData: MyInfoCustomerFinancialDataDto): Option[RecommendedInvestmentDto] = ???
> def deriveRecommandationFromIncomeTier(level: TierLevel, recommndationMapping: Map[TierLevel, BigDecimal]): RecommendedInvestmentDto = ???
> ```
> 
> ‌
> 
> then you can use it here
> 
> ```
> val myInfoFinancialData = getMyInfoFinancialData(maybeCustomerMyInfoFinancialData, onboardingData)
> deriveRecommandationFromMyInfo(myInfoFinancialData)
>   .getOrElse(deriveRecommandationFromIncomeTier(level, RecommendedRecurringMonthlyAmountCpfBasedOnIncomeLevelMap))
> ```
> 
> ‌
> 
> and for SGD cash we just use
> 
> ```
> deriveRecommandationFromIncomeTier(level, RecommendedRecurringMonthlyAmountSgdCashBasedOnIncomeLevelMap)
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:776 · comment 529606869 · PR 9739 · 2024-08-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManager.scala`

**Evidence:** anon-2.jsonl:776 · comment 529606869 · PR 9739 · 2024-08-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManager.scala`

**Explicit source context (pr_title):**

> Feat/EN-3683 sg create a new api to get recommended investment amount

## A2-0783 — SgRecommendedInvestmentManager: Best if we can refactor to avoid make unnecessary calls

**Source stance:** suggestion

**Context:**

> PR 9739 (Feat/EN-3683 sg create a new api to get recommended investment amount), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManager.scala; original row 783.

**Concern stated in the source:** Best if we can refactor to avoid make unnecessary calls

```
lazy val tierLevelFut = getCustomerIncomeTierLevel(customerId)
lazy val myInfoFinancialDataFut = getMyInfoFinancialData(customerId)

tradingAccountType match {
  case TradingAccountType.SINGAPORE_SGD_CASH_ACCOUNT =>
    tierLevelFut.map { level =>
      deriveRecommendationFromIncomeTier(level, RecommendedRecurringMonthlyAmountSgdCashBasedOnIncomeLevelMap)
    }

  case TradingAccountType.SINGAPORE_CPF_OA_ACCOUNT =>
    for {
      myInfoFinancialData <- myInfoFinancialDataFut
      response <- deriveRecommendationFromMyInfo(myInfoFinancialData) match {
        case Some(recommendation) =>
          Future.successful(recommendation)
        case None =>
          tierLevelFut.map { level =>
            deriveRecommendationFromIncomeTier(level, RecommendedRecurringMonthlyAmountCpfBasedOnIncomeLevelMap)
          }
      }
    } yield response

  case _ =>
    Future.successful(RecommendedInvestmentDto.noRecommendation())
}
```

‌

No need to split the helper methods too fine, especially when they are not used in more than one place

* `getCustomerIncomeTierLevel` can do both customer lookup and perform mapping to TierLevel
* `getMyInfoFinancialData` can do myinfo lookup, if found then return, else only then do onboarding lookup and perform mapping

‌

**Source-preserving request, proposal, or question:**

> Best if we can refactor to avoid make unnecessary calls
> 
> ```
> lazy val tierLevelFut = getCustomerIncomeTierLevel(customerId)
> lazy val myInfoFinancialDataFut = getMyInfoFinancialData(customerId)
> 
> tradingAccountType match {
>   case TradingAccountType.SINGAPORE_SGD_CASH_ACCOUNT =>
>     tierLevelFut.map { level =>
>       deriveRecommendationFromIncomeTier(level, RecommendedRecurringMonthlyAmountSgdCashBasedOnIncomeLevelMap)
>     }
> 
>   case TradingAccountType.SINGAPORE_CPF_OA_ACCOUNT =>
>     for {
>       myInfoFinancialData <- myInfoFinancialDataFut
>       response <- deriveRecommendationFromMyInfo(myInfoFinancialData) match {
>         case Some(recommendation) =>
>           Future.successful(recommendation)
>         case None =>
>           tierLevelFut.map { level =>
>             deriveRecommendationFromIncomeTier(level, RecommendedRecurringMonthlyAmountCpfBasedOnIncomeLevelMap)
>           }
>       }
>     } yield response
> 
>   case _ =>
>     Future.successful(RecommendedInvestmentDto.noRecommendation())
> }
> ```
> 
> ‌
> 
> No need to split the helper methods too fine, especially when they are not used in more than one place
> 
> * `getCustomerIncomeTierLevel` can do both customer lookup and perform mapping to TierLevel
> * `getMyInfoFinancialData` can do myinfo lookup, if found then return, else only then do onboarding lookup and perform mapping
> 
> ‌

**Conditions and limits:**

- SGD uses only income-tier lookup; CPF tries MyInfo first, falling back to income tier only if needed; unsupported account returns noRecommendation. Customer/onboarding lookup should also be lazy.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:783 · comment 530404623 · PR 9739 · 2024-08-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManager.scala`

**Evidence:** anon-2.jsonl:783 · comment 530404623 · PR 9739 · 2024-08-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManager.scala`

**Explicit source context (pr_title):**

> Feat/EN-3683 sg create a new api to get recommended investment amount

## A2-0784 — SgRecommendedInvestmentManager: Can we change to this style instead

**Source stance:** suggestion

**Context:**

> PR 9739 (Feat/EN-3683 sg create a new api to get recommended investment amount), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManager.scala; original row 784.

**Concern stated in the source:** Can we change to this style instead

```
(myInfoFinancialData.updatedAt, myInfoFinancialData.cpfBalances.flatMap(_.oa), myInfoFinancialData.cpfContributions) match {
  case (Some(updatedAt), Some(cpfOaBalance), Some(cpfContributions)) =>
    ...
  case _ =>
    None
}
```

A bit dangerous to extract `cpfOaBalance` via extractor if we mess up refactoring, cuz all the fields there are `Option[Decimal]`

**Source-preserving request, proposal, or question:**

> Can we change to this style instead
> 
> ```
> (myInfoFinancialData.updatedAt, myInfoFinancialData.cpfBalances.flatMap(_.oa), myInfoFinancialData.cpfContributions) match {
>   case (Some(updatedAt), Some(cpfOaBalance), Some(cpfContributions)) =>
>     ...
>   case _ =>
>     None
> }
> ```
> 
> A bit dangerous to extract `cpfOaBalance` via extractor if we mess up refactoring, cuz all the fields there are `Option[Decimal]`

**Conditions and limits:**

- Tuple matching is proposed because many Option[Decimal] extractor fields make refactoring mixups easy.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:784 · comment 530398441 · PR 9739 · 2024-08-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManager.scala`

**Evidence:** anon-2.jsonl:784 · comment 530398441 · PR 9739 · 2024-08-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgRecommendedInvestmentManager.scala`

**Explicit source context (pr_title):**

> Feat/EN-3683 sg create a new api to get recommended investment amount

## A2-0807 — TimeSeriesServiceClient: Can use `ServiceExceptionFactory.NoopFactory` if a service doesn’t have any need for custom exception

**Source stance:** suggestion

**Context:**

> PR 9440 ([LAGOM-97] (timeseries) Lagom client removal for timeseries), timeseries-api/src/main/scala/com/endowus/silver/timeseries/api/TimeSeriesServiceClient.scala; original row 807.

**Concern stated in the source:** Can use `ServiceExceptionFactory.NoopFactory` if a service doesn’t have any need for custom exception

**Source-preserving request, proposal, or question:**

> Can use `ServiceExceptionFactory.NoopFactory` if a service doesn’t have any need for custom exception

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:807 · comment 516344053 · PR 9440 · 2024-07-02

Source path: `timeseries-api/src/main/scala/com/endowus/silver/timeseries/api/TimeSeriesServiceClient.scala`

**Evidence:** anon-2.jsonl:807 · comment 516344053 · PR 9440 · 2024-07-02

Source path: `timeseries-api/src/main/scala/com/endowus/silver/timeseries/api/TimeSeriesServiceClient.scala`

**Explicit source context (pr_title):**

> [LAGOM-97] (timeseries) Lagom client removal for timeseries

## A2-0813 — BrokerOrderTopicSubscriber: Lagom is using below by default

**Source stance:** suggestion

**Context:**

> PR 9440 ([LAGOM-97] (timeseries) Lagom client removal for timeseries), timeseries-impl/src/main/scala/com/endowus/silver/timeseries/impl/subscribers/BrokerOrderTopicSubscriber.scala; original row 813.

**Concern stated in the source:** Lagom is using below by default

```
lagom.broker.kafka {
  client {
    default {
      # Exponential backoff for failures
      failure-exponential-backoff {
        # minimum (initial) duration until processor is started again
        # after failure
        min = 3s

        # the exponential back-off is capped to this duration
        max = 30s

        # additional random delay is based on this factor
        random-factor = 0.2
      }
    }
  }
}
```

‌

**Source-preserving request, proposal, or question:**

> Lagom is using below by default
> 
> ```
> lagom.broker.kafka {
>   client {
>     default {
>       # Exponential backoff for failures
>       failure-exponential-backoff {
>         # minimum (initial) duration until processor is started again
>         # after failure
>         min = 3s
> 
>         # the exponential back-off is capped to this duration
>         max = 30s
> 
>         # additional random delay is based on this factor
>         random-factor = 0.2
>       }
>     }
>   }
> }
> ```
> 
> ‌

**Conditions and limits:**

- The quoted Lagom default is exponential-backoff min=3s, max=30s, random-factor=0.2.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:813 · comment 516353645 · PR 9440 · 2024-07-02

Source path: `timeseries-impl/src/main/scala/com/endowus/silver/timeseries/impl/subscribers/BrokerOrderTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:813 · comment 516353645 · PR 9440 · 2024-07-02

Source path: `timeseries-impl/src/main/scala/com/endowus/silver/timeseries/impl/subscribers/BrokerOrderTopicSubscriber.scala`

**Explicit source context (pr_title):**

> [LAGOM-97] (timeseries) Lagom client removal for timeseries

## A2-0820 — ServiceClientExceptionSerializerTest: Shouldn’t it be `implicit val system: ActorSystem`

**Source stance:** suggestion

**Context:**

> PR 9440 ([LAGOM-97] (timeseries) Lagom client removal for timeseries), akka-client-commons/src/test/scala/ServiceClientExceptionSerializerTest.scala; original row 820.

**Concern stated in the source:** Shouldn’t it be `implicit val system: ActorSystem`

‌

**Source-preserving request, proposal, or question:**

> Shouldn’t it be `implicit val system: ActorSystem`
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:820 · comment 525234003 · PR 9440 · 2024-07-26

Source path: `akka-client-commons/src/test/scala/ServiceClientExceptionSerializerTest.scala`

**Evidence:** anon-2.jsonl:820 · comment 525234003 · PR 9440 · 2024-07-26

Source path: `akka-client-commons/src/test/scala/ServiceClientExceptionSerializerTest.scala`

**Explicit source context (pr_title):**

> [LAGOM-97] (timeseries) Lagom client removal for timeseries

## A2-0821 — ProductPortfolioRepository: Maybe we can keep this method generic, but only handle for CoreEnhanced for now…

**Source stance:** suggestion

**Context:**

> PR 9605 ([INV-3236] feat(advisory): create advisory endpoints for goal create), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala; original row 821.

**Concern stated in the source:** Maybe we can keep this method generic, but only handle for CoreEnhanced for now…

```
def findProductPortfolio(
  advisoryTag: AdvisoryTag,
  riskTarget: ModelPortfolioRiskTarget,
  tradingAccountType: TradingAccountType
): Future[ProductPortfolio] = {
  findAllActiveForAdvisoryTag(advisoryTag)
    .filter(p => filterForTradingAccountType(advisoryTag, tradingAccountType, p))
    .filter(p => filterForRiskTarget(advisoryTag, riskTarget, p))
    .runWith(Sink.headOption)
    .flatMap({
      case Some(productPortfolio) => Future.successful(productPortfolio)
      case None =>
        Future
          .failed(BadRequest(s"Unable to find $advisoryTag portfolio for trading account $tradingAccountType with risk target of $riskTarget"))
    })
}

private def filterForRiskTarget(advisoryTag: AdvisoryTag, riskTarget: ModelPortfolioRiskTarget, p: ProductPortfolio): Boolean = {
  advisoryTag match {
    case AdvisoryTag.CORE_ENHANCED =>
      ProductPortfolio.extractCoreEnhancedMetaData(p).exists(_.riskTarget == riskTarget)
    case _ => false
  }
}
```

‌

I want to keep the method signature as close to the lookup by targetStockRatio one so it’s easier to switch later for Flagship/Esg/Factors/FlagshipDpm

**Source-preserving request, proposal, or question:**

> Maybe we can keep this method generic, but only handle for CoreEnhanced for now…
> 
> ```
> def findProductPortfolio(
>   advisoryTag: AdvisoryTag,
>   riskTarget: ModelPortfolioRiskTarget,
>   tradingAccountType: TradingAccountType
> ): Future[ProductPortfolio] = {
>   findAllActiveForAdvisoryTag(advisoryTag)
>     .filter(p => filterForTradingAccountType(advisoryTag, tradingAccountType, p))
>     .filter(p => filterForRiskTarget(advisoryTag, riskTarget, p))
>     .runWith(Sink.headOption)
>     .flatMap({
>       case Some(productPortfolio) => Future.successful(productPortfolio)
>       case None =>
>         Future
>           .failed(BadRequest(s"Unable to find $advisoryTag portfolio for trading account $tradingAccountType with risk target of $riskTarget"))
>     })
> }
> 
> private def filterForRiskTarget(advisoryTag: AdvisoryTag, riskTarget: ModelPortfolioRiskTarget, p: ProductPortfolio): Boolean = {
>   advisoryTag match {
>     case AdvisoryTag.CORE_ENHANCED =>
>       ProductPortfolio.extractCoreEnhancedMetaData(p).exists(_.riskTarget == riskTarget)
>     case _ => false
>   }
> }
> ```
> 
> ‌
> 
> I want to keep the method signature as close to the lookup by targetStockRatio one so it’s easier to switch later for Flagship/Esg/Factors/FlagshipDpm

**Conditions and limits:**

- Initial proposed generic signature handles only CoreEnhanced and otherwise returns false; row 837 proposes completing other productlines via ProductPortfolio.riskTarget.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:821 · comment 523845974 · PR 9605 · 2024-07-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala`

**Evidence:** anon-2.jsonl:821 · comment 523845974 · PR 9605 · 2024-07-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala`

**Explicit source context (pr_title):**

> [INV-3236] feat(advisory): create advisory endpoints for goal create

## A2-0858 — InstrumentMarketDataEntity: If it’s None, `exists` will return false and we won’t fail

**Source stance:** explanation

**Context:**

> PR 9671 ([INV-3355] feat(marketdata): Allow empty price in DailyPerformance API. Populate instrument ccy if not exists), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/InstrumentMarketDataEntity.scala; original row 858.

**Concern stated in the source:** If it’s None, `exists` will return false and we won’t fail

**Source-preserving request, proposal, or question:**

> If it’s None, `exists` will return false and we won’t fail

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:858 · comment 525764413 · PR 9671 · 2024-07-29

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/InstrumentMarketDataEntity.scala`

**Evidence:** anon-2.jsonl:858 · comment 525764413 · PR 9671 · 2024-07-29

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/InstrumentMarketDataEntity.scala`

**Explicit source context (pr_title):**

> [INV-3355] feat(marketdata): Allow empty price in DailyPerformance API. Populate instrument ccy if not exists

## A2-0859 — InstrumentMarketDataEntity: As in is this marketdata update original \(and not result of fx conversion\)

**Source stance:** open-question

**Context:**

> PR 9671 ([INV-3355] feat(marketdata): Allow empty price in DailyPerformance API. Populate instrument ccy if not exists), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/InstrumentMarketDataEntity.scala; original row 859.

**Source-preserving request, proposal, or question:**

> As in is this marketdata update original \(and not result of fx conversion\)

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:859 · comment 525764992 · PR 9671 · 2024-07-29

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/InstrumentMarketDataEntity.scala`

**Evidence:** anon-2.jsonl:859 · comment 525764992 · PR 9671 · 2024-07-29

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/InstrumentMarketDataEntity.scala`

**Explicit source context (pr_title):**

> [INV-3355] feat(marketdata): Allow empty price in DailyPerformance API. Populate instrument ccy if not exists

## A2-0860 — NonAltsFeeManager: Can you help to refactor this bit a little, to make it clearer

**Source stance:** suggestion

**Context:**

> PR 9668 (Fix/EN-3777 cash only fee charge), charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/NonAltsFeeManager.scala; original row 860.

**Concern stated in the source:** Can you help to refactor this bit a little, to make it clearer

* we simply validate request.cashOnlyFee flag must be enabled if required
* after validated, it’s safe to use the flag in the request directly, i.e. if required then it’s already set, if not required then it may or may not set, up to caller

```
isCashOnlyFeeRequired <- isCashOnlyFeeRequired(planId, planProfile.tradingAccountType)(isSellBlockedPlan)
_ = if (isCashOnlyFeeRequired && !request.cashOnlyFee.contains(true)) {
  throw BadRequest(s"CashOnlyFee is required for plan: $planId")
}
...
maybeFeeChargeRequest <- chargePlanIfEligible(
  ...
  cashOnlyFee = request.cashOnlyFee
)
```

‌

**Source-preserving request, proposal, or question:**

> Can you help to refactor this bit a little, to make it clearer
> 
> * we simply validate request.cashOnlyFee flag must be enabled if required
> * after validated, it’s safe to use the flag in the request directly, i.e. if required then it’s already set, if not required then it may or may not set, up to caller
> 
> ```
> isCashOnlyFeeRequired <- isCashOnlyFeeRequired(planId, planProfile.tradingAccountType)(isSellBlockedPlan)
> _ = if (isCashOnlyFeeRequired && !request.cashOnlyFee.contains(true)) {
>   throw BadRequest(s"CashOnlyFee is required for plan: $planId")
> }
> ...
> maybeFeeChargeRequest <- chargePlanIfEligible(
>   ...
>   cashOnlyFee = request.cashOnlyFee
> )
> ```
> 
> ‌

**Conditions and limits:**

- Validate cashOnlyFee is enabled when required, then honor the request flag even when not required.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:860 · comment 525738620 · PR 9668 · 2024-07-29

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/NonAltsFeeManager.scala`

**Evidence:** anon-2.jsonl:860 · comment 525738620 · PR 9668 · 2024-07-29

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/NonAltsFeeManager.scala`

**Explicit source context (pr_title):**

> Fix/EN-3777 cash only fee charge

## A2-0863 — OverrideRedemptionCashReservationsCmdHandler: Should be safe to just use `RedemptionRequestStatus.terminalStatuses`… FAILED should block as well

**Source stance:** suggestion

**Context:**

> PR 9653 ([INV-3350] feat(redemption): Faciliate handling of invalid redemption requests in complete status), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/handlers/OverrideRedemptionCashReservationsCmdHandler.scala; original row 863.

**Concern stated in the source:** Should be safe to just use `RedemptionRequestStatus.terminalStatuses`… FAILED should block as well

**Source-preserving request, proposal, or question:**

> Should be safe to just use `RedemptionRequestStatus.terminalStatuses`… FAILED should block as well

**Conditions and limits:**

- FAILED is included among terminal redemption statuses that should block this operation.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:863 · comment 524940917 · PR 9653 · 2024-07-25

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/handlers/OverrideRedemptionCashReservationsCmdHandler.scala`

**Evidence:** anon-2.jsonl:863 · comment 524940917 · PR 9653 · 2024-07-25

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/handlers/OverrideRedemptionCashReservationsCmdHandler.scala`

**Explicit source context (pr_title):**

> [INV-3350] feat(redemption): Faciliate handling of invalid redemption requests in complete status

## A2-0882 — EmailProviderData: All of these, in theory, would need to be optional. Cuz there might be existing message in the kafka topic without the fields, and communication svc starts ex...

**Source stance:** suggestion

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), communication-api/src/main/scala/com/endowus/silver/communication/api/v2/email/EmailProviderData.scala; original row 882.

**Concern stated in the source:** All of these, in theory, would need to be optional. Cuz there might be existing message in the kafka topic without the fields, and communication svc starts expecting new field to be required.

We will not release during the printing, but POps might still print adhoc statements every now and then. I think let’s play safe and make `statementType` optional.

**Source-preserving request, proposal, or question:**

> All of these, in theory, would need to be optional. Cuz there might be existing message in the kafka topic without the fields, and communication svc starts expecting new field to be required.
> 
> We will not release during the printing, but POps might still print adhoc statements every now and then. I think let’s play safe and make `statementType` optional.

**Conditions and limits:**

- Kafka may still contain messages without statementType even outside normal printing release windows because POps runs adhoc printing; source requests optionality.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:882 · comment 507791386 · PR 9240 · 2024-06-03

Source path: `communication-api/src/main/scala/com/endowus/silver/communication/api/v2/email/EmailProviderData.scala`

**Evidence:** anon-2.jsonl:882 · comment 507791386 · PR 9240 · 2024-06-03

Source path: `communication-api/src/main/scala/com/endowus/silver/communication/api/v2/email/EmailProviderData.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0883 — StatementDataGenerator: Let’s filter for dpmGoals outside, regardless of `ignoreTimeForDebug`

**Source stance:** suggestion

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/StatementDataGenerator.scala; original row 883.

**Concern stated in the source:** Let’s filter for dpmGoals outside, regardless of `ignoreTimeForDebug`

**Source-preserving request, proposal, or question:**

> Let’s filter for dpmGoals outside, regardless of `ignoreTimeForDebug`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:883 · comment 507805408 · PR 9240 · 2024-06-03

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/StatementDataGenerator.scala`

**Evidence:** anon-2.jsonl:883 · comment 507805408 · PR 9240 · 2024-06-03

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/StatementDataGenerator.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0884 — StatementEmailProducer: Let’s name these `DpmSemiAnnualReport*` or `DiscretionarySemiAnnualReport`

**Source stance:** suggestion

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-impl/src/main/scala/com/endowus/silver/report/impl/producers/StatementEmailProducer.scala; original row 884.

**Source-preserving request, proposal, or question:**

> Let’s name these `DpmSemiAnnualReport*` or `DiscretionarySemiAnnualReport`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:884 · comment 507803742 · PR 9240 · 2024-06-03

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/producers/StatementEmailProducer.scala`

**Evidence:** anon-2.jsonl:884 · comment 507803742 · PR 9240 · 2024-06-03

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/producers/StatementEmailProducer.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0887 — StatementEmailProducer: Can help to rename this typo `MonthlyStatemnetGenerated`

**Source stance:** suggestion

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-impl/src/main/scala/com/endowus/silver/report/impl/producers/StatementEmailProducer.scala; original row 887.

**Source-preserving request, proposal, or question:**

> Can help to rename this typo `MonthlyStatemnetGenerated`

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:887 · comment 507803434 · PR 9240 · 2024-06-03

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/producers/StatementEmailProducer.scala`

**Evidence:** anon-2.jsonl:887 · comment 507803434 · PR 9240 · 2024-06-03

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/producers/StatementEmailProducer.scala`

**Explicit source context (hunk):**

>      val shortFormMonth = Translator.translate(preferredLocale, yearMonth.getMonth)
> +    val shortFormStartMonth = Translator.translate(preferredLocale, startDateOfStatement.getMonth)
> +    val shortFormEndMonth = Translator.translate(preferredLocale, endDateOfStatement.getMonth)
>      val ctaUrl = uri"${localConfig.getSilverWebAppBaseUrl}/account/monthly-statements"
> +
>      val (emailTemplateType, data) = if (isReprint) {
> -      (

**Evidence:** anon-2.jsonl:887 · comment 507803434 · PR 9240 · 2024-06-03

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/producers/StatementEmailProducer.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0889 — HkServiceLogicImpl: Looking at `StatementDataGenerator.createStatementDataAndGeneratePdf`, looks like it’s better to use `statementPeriod = END_OF_MONTH` and `monthPeriod = Some...

**Source stance:** suggestion

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-impl/src/main/scala/com/endowus/silver/report/impl/logic/service/impl/HkServiceLogicImpl.scala; original row 889.

**Concern stated in the source:** Looking at `StatementDataGenerator.createStatementDataAndGeneratePdf`, looks like it’s better to use `statementPeriod = END_OF_MONTH` and `monthPeriod = Some(6)`, and only specify `startDateOfStatement`

‌

**Source-preserving request, proposal, or question:**

> Looking at `StatementDataGenerator.createStatementDataAndGeneratePdf`, looks like it’s better to use `statementPeriod = END_OF_MONTH` and `monthPeriod = Some(6)`, and only specify `startDateOfStatement`
> 
> ‌

**Conditions and limits:**

- Use statementPeriod=END_OF_MONTH, monthPeriod=Some(6), and specify only startDateOfStatement.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:889 · comment 507802852 · PR 9240 · 2024-06-03

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/logic/service/impl/HkServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:889 · comment 507802852 · PR 9240 · 2024-06-03

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/logic/service/impl/HkServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0892 — BaseServiceLogicImpl: I extracted `IncludeExcludeUtils`. Can see example for rebate / charge svc. If make sense, maybe we can refactor to use that as well

**Source stance:** suggestion

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-impl/src/main/scala/com/endowus/silver/report/impl/logic/service/impl/BaseServiceLogicImpl.scala; original row 892.

**Source-preserving request, proposal, or question:**

> I extracted `IncludeExcludeUtils`. Can see example for rebate / charge svc. If make sense, maybe we can refactor to use that as well

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:892 · comment 507796716 · PR 9240 · 2024-06-03

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:892 · comment 507796716 · PR 9240 · 2024-06-03

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0894 — StatementGenerationScheduler: Maybe getYear - 1 is cheaper?

**Source stance:** open-question

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-impl/src/main/scala/com/endowus/silver/report/impl/scheduler/StatementGenerationScheduler.scala; original row 894.

**Source-preserving request, proposal, or question:**

> Maybe getYear - 1 is cheaper?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:894 · comment 507826195 · PR 9240 · 2024-06-03

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/scheduler/StatementGenerationScheduler.scala`

**Evidence:** anon-2.jsonl:894 · comment 507826195 · PR 9240 · 2024-06-03

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/scheduler/StatementGenerationScheduler.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0895 — StatementGenerationScheduler: Should be July?

**Source stance:** open-question

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-impl/src/main/scala/com/endowus/silver/report/impl/scheduler/StatementGenerationScheduler.scala; original row 895.

**Source-preserving request, proposal, or question:**

> Should be July?

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- Scheduler hunk uses January or July for HK semi-annual reports. The comment is a correction/question, not a complete scheduling specification.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:895 · comment 507824726 · PR 9240 · 2024-06-03

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/scheduler/StatementGenerationScheduler.scala`

**Evidence:** anon-2.jsonl:895 · comment 507824726 · PR 9240 · 2024-06-03

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/scheduler/StatementGenerationScheduler.scala`

**Explicit source context (hunk):**

> +    val isJanuary = today.getMonth == Month.JANUARY
> +    val isJuly = today.getMonth == Month.JULY
> +    (isJanuary || isJuly) && region == SilverRegion.Hk
> +  }
> +
> +  private def generateMonthlyStatement(): Future[Done] = {
> +    val env = localConfig.getSilverEnvironment

**Evidence:** anon-2.jsonl:895 · comment 507824726 · PR 9240 · 2024-06-03

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/scheduler/StatementGenerationScheduler.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0896 — HkServiceLogicImpl: Looks like this is not needed, as `endDateOfStatement` will be resolved from `yearMonth`

**Source stance:** explanation

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-impl/src/main/scala/com/endowus/silver/report/impl/logic/service/impl/HkServiceLogicImpl.scala; original row 896.

**Concern stated in the source:** Looks like this is not needed, as `endDateOfStatement` will be resolved from `yearMonth`

**Source-preserving request, proposal, or question:**

> Looks like this is not needed, as `endDateOfStatement` will be resolved from `yearMonth`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:896 · comment 511583082 · PR 9240 · 2024-06-18

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/logic/service/impl/HkServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:896 · comment 511583082 · PR 9240 · 2024-06-18

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/logic/service/impl/HkServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0898 — StatementGenerationScheduler: Should we take in `today: LocalDate`?

**Source stance:** open-question

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-impl/src/main/scala/com/endowus/silver/report/impl/scheduler/StatementGenerationScheduler.scala; original row 898.

**Source-preserving request, proposal, or question:**

> Should we take in `today: LocalDate`?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:898 · comment 511606684 · PR 9240 · 2024-06-18

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/scheduler/StatementGenerationScheduler.scala`

**Evidence:** anon-2.jsonl:898 · comment 511606684 · PR 9240 · 2024-06-18

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/scheduler/StatementGenerationScheduler.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0901 — StatementGenerationScheduler: Nit: `shouldGenerateDpmSemiAnnualReport`

**Source stance:** suggestion

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-impl/src/main/scala/com/endowus/silver/report/impl/scheduler/StatementGenerationScheduler.scala; original row 901.

**Source-preserving request, proposal, or question:**

> Nit: `shouldGenerateDpmSemiAnnualReport`

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:901 · comment 511604858 · PR 9240 · 2024-06-18

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/scheduler/StatementGenerationScheduler.scala`

**Evidence:** anon-2.jsonl:901 · comment 511604858 · PR 9240 · 2024-06-18

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/scheduler/StatementGenerationScheduler.scala`

**Explicit source context (hunk):**

>    }
> +
> +  private def shouldGenerateDpmSemiAnnualReport(today: LocalDate, region: SilverRegion): Boolean = {
> +    val isJanuary = today.getMonth == Month.JANUARY
> +    val isJuly = today.getMonth == Month.JULY
> +    (isJanuary || isJuly) && region == SilverRegion.Hk
> +  }

**Evidence:** anon-2.jsonl:901 · comment 511604858 · PR 9240 · 2024-06-18

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/scheduler/StatementGenerationScheduler.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0903 — StatementGenerationScheduler: Nit: `generateMonthlyStatement`

**Source stance:** suggestion

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-impl/src/main/scala/com/endowus/silver/report/impl/scheduler/StatementGenerationScheduler.scala; original row 903.

**Source-preserving request, proposal, or question:**

> Nit: `generateMonthlyStatement`

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:903 · comment 511604933 · PR 9240 · 2024-06-18

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/scheduler/StatementGenerationScheduler.scala`

**Evidence:** anon-2.jsonl:903 · comment 511604933 · PR 9240 · 2024-06-18

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/scheduler/StatementGenerationScheduler.scala`

**Explicit source context (hunk):**

> +  }
> +
> +  private def generateMonthlyStatement(): Future[Done] = {
> +    val env = localConfig.getSilverEnvironment
> +    env match {
> +      case SilverEnvironment.PROD =>
> +        val statementMonthToGenerate = dateTimeProvider.currentMonth.minusMonths(1)

**Evidence:** anon-2.jsonl:903 · comment 511604933 · PR 9240 · 2024-06-18

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/scheduler/StatementGenerationScheduler.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0906 — allInvestmentGoalsPage: You can have both

**Source stance:** suggestion

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-impl/src/main/resources/templates/hk/allInvestmentGoalsPage.html; original row 906.

**Source-preserving request, proposal, or question:**

> You can have both
> 
> ```
> case class PageData(
>   ...,
>   statementType: StatementTypeEnum
> ) {
>   lazy val isDpmSemiAnnualReport: Boolean = statementType == StatementTypeEnum.DPM_SEMI_ANNUAL_REPORT
> }
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:906 · comment 512145588 · PR 9240 · 2024-06-20

Source path: `report-impl/src/main/resources/templates/hk/allInvestmentGoalsPage.html`

**Evidence:** anon-2.jsonl:906 · comment 512145588 · PR 9240 · 2024-06-20

Source path: `report-impl/src/main/resources/templates/hk/allInvestmentGoalsPage.html`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0907 — StatementDataGenerator: Maybe rename this val to `isApplicableForStatementType`

**Source stance:** suggestion

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/StatementDataGenerator.scala; original row 907.

**Source-preserving request, proposal, or question:**

> Maybe rename this val to `isApplicableForStatementType`

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:907 · comment 512147040 · PR 9240 · 2024-06-20

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/StatementDataGenerator.scala`

**Evidence:** anon-2.jsonl:907 · comment 512147040 · PR 9240 · 2024-06-20

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/StatementDataGenerator.scala`

**Explicit source context (hunk):**

> -      response <- if (!customerStatusIsValidForGeneration) {
> -        Future.successful(
> -          CreateCustomerStatementResponse(
> -            status = StatementStatusEnum.CANCELLED_NO_AVAILABLE_DATA,
> -            reason = Some(s"Customer's status [${customerInfo.status}] is not valid to create Statement!! CustomerId[${request.customerId}]!!")
> -          )
> +        goalIdsToDisplay = getGoalIdsToDisplay(startDateOfStatement, goalsToCalculate)

**Evidence:** anon-2.jsonl:907 · comment 512147040 · PR 9240 · 2024-06-20

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/StatementDataGenerator.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0910 — StatementPageData: Can you remind me again why this condition is not just `startOfNonDiscretionaryGoalIndex > 0` ? Shouldn’t the condition be same as one in `showGoalOnLeftOfCov...

**Source stance:** open-question

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-impl/src/main/scala/com/endowus/silver/report/impl/pdfGenerator/models/StatementPageData.scala; original row 910.

**Concern stated in the source:** Can you remind me again why this condition is not just `startOfNonDiscretionaryGoalIndex > 0` ? Shouldn’t the condition be same as one in `showGoalOnLeftOfCoverPagePureGoalAtRowIndex` ?

**Source-preserving request, proposal, or question:**

> Can you remind me again why this condition is not just `startOfNonDiscretionaryGoalIndex > 0` ? Shouldn’t the condition be same as one in `showGoalOnLeftOfCoverPagePureGoalAtRowIndex` ?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:910 · comment 512900031 · PR 9240 · 2024-06-24

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/pdfGenerator/models/StatementPageData.scala`

**Evidence:** anon-2.jsonl:910 · comment 512900031 · PR 9240 · 2024-06-24

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/pdfGenerator/models/StatementPageData.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0912 — StatementPageData: Both this and the one below should check against `MaxGoalRowsCanFitOnLeftSectionOfCoverPagePureGoal` \(even though left and right here ref the same const\)?

**Source stance:** open-question

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-impl/src/main/scala/com/endowus/silver/report/impl/pdfGenerator/models/StatementPageData.scala; original row 912.

**Concern stated in the source:** Both this and the one below should check against `MaxGoalRowsCanFitOnLeftSectionOfCoverPagePureGoal` \(even though left and right here ref the same const\)?

**Source-preserving request, proposal, or question:**

> Both this and the one below should check against `MaxGoalRowsCanFitOnLeftSectionOfCoverPagePureGoal` \(even though left and right here ref the same const\)?

**Conditions and limits:**

- Both referenced checks should use MaxGoalRowsCanFitOnLeftSectionOfCoverPagePureGoal even if left/right currently share a numeric value.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:912 · comment 512900208 · PR 9240 · 2024-06-24

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/pdfGenerator/models/StatementPageData.scala`

**Evidence:** anon-2.jsonl:912 · comment 512900208 · PR 9240 · 2024-06-24

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/pdfGenerator/models/StatementPageData.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0913 — StatementPageData: Maybe we can put some common method so it’s easier to follow

**Source stance:** suggestion

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-impl/src/main/scala/com/endowus/silver/report/impl/pdfGenerator/models/StatementPageData.scala; original row 913.

**Concern stated in the source:** Maybe we can put some common method so it’s easier to follow

```
private def canFitUnderstandingYourStatementAndDisclaimerOnLeftOfCoverPage(maxGoalRowsCanFitLeftSection: Int, totalNumberOfGoals: Int): Boolean =
  totalNumberOfGoals <= maxGoalRowsCanFitLeftSection - NumberOfRowsForUnderstandingYourStatementAndDisclaimer
  
def showUnderstandingYourStatementAndDisclaimerOnLeftOfCoverPage(totalNumberOfGoals: Int): Boolean =
  canFitUnderstandingYourStatementAndDisclaimerOnLeftOfCoverPage(MaxGoalRowsCanFitOnLeftSectionOfCoverPage, totalNumberOfGoals)
  
def showUnderstandingYourStatementAndDisclaimerOnRightOfCoverPage(totalNumberOfGoals: Int): Boolean =
  !canFitUnderstandingYourStatementAndDisclaimerOnLeftOfCoverPage(MaxGoalRowsCanFitOnLeftSectionOfCoverPage, totalNumberOfGoals)
```

\(not sure if we want to put “Right” methods here, cuz it seems we normally use `th:unless` in template\)

**Source-preserving request, proposal, or question:**

> Maybe we can put some common method so it’s easier to follow
> 
> ```
> private def canFitUnderstandingYourStatementAndDisclaimerOnLeftOfCoverPage(maxGoalRowsCanFitLeftSection: Int, totalNumberOfGoals: Int): Boolean =
>   totalNumberOfGoals <= maxGoalRowsCanFitLeftSection - NumberOfRowsForUnderstandingYourStatementAndDisclaimer
>   
> def showUnderstandingYourStatementAndDisclaimerOnLeftOfCoverPage(totalNumberOfGoals: Int): Boolean =
>   canFitUnderstandingYourStatementAndDisclaimerOnLeftOfCoverPage(MaxGoalRowsCanFitOnLeftSectionOfCoverPage, totalNumberOfGoals)
>   
> def showUnderstandingYourStatementAndDisclaimerOnRightOfCoverPage(totalNumberOfGoals: Int): Boolean =
>   !canFitUnderstandingYourStatementAndDisclaimerOnLeftOfCoverPage(MaxGoalRowsCanFitOnLeftSectionOfCoverPage, totalNumberOfGoals)
> ```
> 
> \(not sure if we want to put “Right” methods here, cuz it seems we normally use `th:unless` in template\)

**Conditions and limits:**

- Right-section helper is optional because templates normally use th:unless; preserve that open design detail.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:913 · comment 512900503 · PR 9240 · 2024-06-24

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/pdfGenerator/models/StatementPageData.scala`

**Evidence:** anon-2.jsonl:913 · comment 512900503 · PR 9240 · 2024-06-24

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/pdfGenerator/models/StatementPageData.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0914 — StatementPageData: Also this has an implicit assumption that we only calls this method in DPM semi-annual report, which doesn’t have non-DPM heading and hence no need to if such...

**Source stance:** suggestion

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-impl/src/main/scala/com/endowus/silver/report/impl/pdfGenerator/models/StatementPageData.scala; original row 914.

**Concern stated in the source:** Also this has an implicit assumption that we only calls this method in DPM semi-annual report, which doesn’t have non-DPM heading and hence no need to if such heading was printed or not \(similar to `showCashBalance*` methods below\).

Maybe put a comment, or find way to adjust the logic so we don’t depend on it

**Source-preserving request, proposal, or question:**

> Also this has an implicit assumption that we only calls this method in DPM semi-annual report, which doesn’t have non-DPM heading and hence no need to if such heading was printed or not \(similar to `showCashBalance*` methods below\).
> 
> Maybe put a comment, or find way to adjust the logic so we don’t depend on it

**Conditions and limits:**

- The helper assumes DPM semi-annual report only, with no non-DPM heading; document or remove that dependency.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:914 · comment 512900720 · PR 9240 · 2024-06-24

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/pdfGenerator/models/StatementPageData.scala`

**Evidence:** anon-2.jsonl:914 · comment 512900720 · PR 9240 · 2024-06-24

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/pdfGenerator/models/StatementPageData.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0915 — StatementPageData: Let’s add comment here too

**Source stance:** suggestion

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-impl/src/main/scala/com/endowus/silver/report/impl/pdfGenerator/models/StatementPageData.scala; original row 915.

**Concern stated in the source:** Let’s add comment here too

```
showDiscretionaryHeadingOnLeftOfCoverPageAtRowIndex
// Only show `Discretionary` heading if it's a first row, and at least one DPM goal exist
// - if cover page has mixed DPM and non-DPM goals, startOfNonDiscretionaryGoalIndex is > 0
// - if cover page has only DPM goals, startOfNonDiscretionaryGoalIndex is -1
```

Should we also extract methods \(together with comments\) for these?

```
showNonDiscretionaryHeadingOnLeftOfCoverPageAtRowIndex
showNonDiscretionaryHeadingOnLeftOfCoverPageAtLastRow
showNonDiscretionaryHeadingOnRightOfCoverPageAtRowIndex
showNonDiscretionaryHeadingOnRightOfCoverPageAtLastRow
```

‌

**Source-preserving request, proposal, or question:**

> Let’s add comment here too
> 
> ```
> showDiscretionaryHeadingOnLeftOfCoverPageAtRowIndex
> // Only show `Discretionary` heading if it's a first row, and at least one DPM goal exist
> // - if cover page has mixed DPM and non-DPM goals, startOfNonDiscretionaryGoalIndex is > 0
> // - if cover page has only DPM goals, startOfNonDiscretionaryGoalIndex is -1
> ```
> 
> Should we also extract methods \(together with comments\) for these?
> 
> ```
> showNonDiscretionaryHeadingOnLeftOfCoverPageAtRowIndex
> showNonDiscretionaryHeadingOnLeftOfCoverPageAtLastRow
> showNonDiscretionaryHeadingOnRightOfCoverPageAtRowIndex
> showNonDiscretionaryHeadingOnRightOfCoverPageAtLastRow
> ```
> 
> ‌

**Conditions and limits:**

- Discretionary heading requires first row and any DPM goal: mixed goals have startOfNonDiscretionaryGoalIndex>0; DPM-only has -1. Extraction of non-DPM heading variants is proposed.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:915 · comment 512899729 · PR 9240 · 2024-06-24

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/pdfGenerator/models/StatementPageData.scala`

**Evidence:** anon-2.jsonl:915 · comment 512899729 · PR 9240 · 2024-06-24

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/pdfGenerator/models/StatementPageData.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0916 — StatementPageData: Let’s put some comment explaining this a bit, e.g. `reserve 3 rows for [...] as compared to CoverPagePureGoal`

**Source stance:** suggestion

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-impl/src/main/scala/com/endowus/silver/report/impl/pdfGenerator/models/StatementPageData.scala; original row 916.

**Concern stated in the source:** Let’s put some comment explaining this a bit, e.g. `reserve 3 rows for [...] as compared to CoverPagePureGoal`

**Source-preserving request, proposal, or question:**

> Let’s put some comment explaining this a bit, e.g. `reserve 3 rows for [...] as compared to CoverPagePureGoal`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:916 · comment 512898362 · PR 9240 · 2024-06-24

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/pdfGenerator/models/StatementPageData.scala`

**Evidence:** anon-2.jsonl:916 · comment 512898362 · PR 9240 · 2024-06-24

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/pdfGenerator/models/StatementPageData.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0917 — ReportService: The term for this \(understood by product and clients\) is actually `semi-annual report` \(as opposed to `monthly statement`\) hence this name everywhere

**Source stance:** explanation

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-api/src/main/scala/com/endowus/silver/report/api/ReportService.scala; original row 917.

**Concern stated in the source:** The term for this \(understood by product and clients\) is actually `semi-annual report` \(as opposed to `monthly statement`\) hence this name everywhere

**Source-preserving request, proposal, or question:**

> The term for this \(understood by product and clients\) is actually `semi-annual report` \(as opposed to `monthly statement`\) hence this name everywhere

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:917 · comment 518703079 · PR 9240 · 2024-07-08

Source path: `report-api/src/main/scala/com/endowus/silver/report/api/ReportService.scala`

**Evidence:** anon-2.jsonl:917 · comment 518703079 · PR 9240 · 2024-07-08

Source path: `report-api/src/main/scala/com/endowus/silver/report/api/ReportService.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0918 — StatementDataGenerator: Actually no need a default `case _` as well cuz it should already give MatchError by default.

**Source stance:** suggestion

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/StatementDataGenerator.scala; original row 918.

**Concern stated in the source:** Actually no need a default `case _` as well cuz it should already give MatchError by default.

And Intellij can help us to indicate non-exhaustive cases warning

**Source-preserving request, proposal, or question:**

> Actually no need a default `case _` as well cuz it should already give MatchError by default.
> 
> And Intellij can help us to indicate non-exhaustive cases warning

**Conditions and limits:**

- Comment says default exhaustive-match failure is MatchError; retain as source-specific suggestion rather than a general error-handling prescription.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:918 · comment 518703203 · PR 9240 · 2024-07-08

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/StatementDataGenerator.scala`

**Evidence:** anon-2.jsonl:918 · comment 518703203 · PR 9240 · 2024-07-08

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/StatementDataGenerator.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0919 — ReportService: [person] I don’t really follow this comment…

**Source stance:** explanation

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-api/src/main/scala/com/endowus/silver/report/api/ReportService.scala; original row 919.

**Concern stated in the source:** [person] I don’t really follow this comment…

* `createDiscretionaryGoalsSemiAnnualReports` is named “report” because it’s actually for DPM semi-annual reports
* `createMonthlyStatementsV2` is named “statement” because it’s actually for monthly statements
* report svc is named “report” because it’s intended to cover all reporting domain?

‌

**Source-preserving request, proposal, or question:**

> [person] I don’t really follow this comment…
> 
> * `createDiscretionaryGoalsSemiAnnualReports` is named “report” because it’s actually for DPM semi-annual reports
> * `createMonthlyStatementsV2` is named “statement” because it’s actually for monthly statements
> * report svc is named “report” because it’s intended to cover all reporting domain?
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:919 · comment 518703934 · PR 9240 · 2024-07-08

Source path: `report-api/src/main/scala/com/endowus/silver/report/api/ReportService.scala`

> I don’t really follow this comment…
> 
> * `createDiscretionaryGoalsSemiAnnualReports` is named “report” because it’s actually for DPM semi-annual reports
> * `createMonthlyStatementsV2` is named “statement” because it’s actually for monthly statements
> * report svc is named “report” because it’s intended to cover all reporting domain?
> 
> ‌

**Evidence:** anon-2.jsonl:919 · comment 518703934 · PR 9240 · 2024-07-08

Source path: `report-api/src/main/scala/com/endowus/silver/report/api/ReportService.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0922 — StatementPageData: Yea the condition is negation, applicable for all of these pages as well I think. But it was like this in the templates and we simply moved them out \+ added ...

**Source stance:** explanation

**Context:**

> PR 9240 ([INV-3011] feat(report): Generate semi annual report), report-impl/src/main/scala/com/endowus/silver/report/impl/pdfGenerator/models/StatementPageData.scala; original row 922.

**Concern stated in the source:** Yea the condition is negation, applicable for all of these pages as well I think. But it was like this in the templates and we simply moved them out \+ added explanation.

**Source-preserving request, proposal, or question:**

> Yea the condition is negation, applicable for all of these pages as well I think. But it was like this in the templates and we simply moved them out \+ added explanation.

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:922 · comment 519134760 · PR 9240 · 2024-07-09

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/pdfGenerator/models/StatementPageData.scala`

**Evidence:** anon-2.jsonl:922 · comment 519134760 · PR 9240 · 2024-07-09

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/pdfGenerator/models/StatementPageData.scala`

**Explicit source context (pr_title):**

> [INV-3011] feat(report): Generate semi annual report

## A2-0924 — FeeManager: As discussed, let’s try to refactor and move this decision to outer level \(similar to fee estimation query\), cuz we already have all the planProfiles and customerI...

**Source stance:** suggestion

**Context:**

> PR 9546 ([EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeManager.scala; original row 924.

**Concern stated in the source:** As discussed, let’s try to refactor and move this decision to outer level \(similar to fee estimation query\), cuz we already have all the planProfiles and customerId there

**Source-preserving request, proposal, or question:**

> As discussed, let’s try to refactor and move this decision to outer level \(similar to fee estimation query\), cuz we already have all the planProfiles and customerId there

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:924 · comment 520050194 · PR 9546 · 2024-07-11

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeManager.scala`

**Evidence:** anon-2.jsonl:924 · comment 520050194 · PR 9546 · 2024-07-11

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeManager.scala`

**Explicit source context (pr_title):**

> [EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles

## A2-0929 — package: We won’t be sending this as separate payload anywhere between the actors, so shouldn’t need extend `PlayJsonSerializable`

**Source stance:** explanation

**Context:**

> PR 9546 ([EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/state/package.scala; original row 929.

**Concern stated in the source:** We won’t be sending this as separate payload anywhere between the actors, so shouldn’t need extend `PlayJsonSerializable`

**Source-preserving request, proposal, or question:**

> We won’t be sending this as separate payload anywhere between the actors, so shouldn’t need extend `PlayJsonSerializable`

**Conditions and limits:**

- PlayJsonSerializable is unnecessary only because this object is not sent separately between actors.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:929 · comment 520040192 · PR 9546 · 2024-07-11

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/state/package.scala`

**Evidence:** anon-2.jsonl:929 · comment 520040192 · PR 9546 · 2024-07-11

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/state/package.scala`

**Explicit source context (pr_title):**

> [EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles

## A2-0930 — package: Should we use the above isDiy instead? We do not support RF semi-liquid alts yet \(I don’t know if we will one day\), until then, and anyway we are only targeting the n...

**Source stance:** open-question

**Context:**

> PR 9546 ([EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/state/package.scala; original row 930.

**Concern stated in the source:** Should we use the above isDiy instead? We do not support RF semi-liquid alts yet \(I don’t know if we will one day\), until then, and anyway we are only targeting the non-Alts FS plans in this requirement

**Source-preserving request, proposal, or question:**

> Should we use the above isDiy instead? We do not support RF semi-liquid alts yet \(I don’t know if we will one day\), until then, and anyway we are only targeting the non-Alts FS plans in this requirement

**Conditions and limits:**

- RF semi-liquid alts are unsupported at that time; current requirement targets non-Alts FundSmart only.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:930 · comment 520039775 · PR 9546 · 2024-07-11

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/state/package.scala`

**Evidence:** anon-2.jsonl:930 · comment 520039775 · PR 9546 · 2024-07-11

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/state/package.scala`

**Explicit source context (pr_title):**

> [EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles

## A2-0932 — InitiateFeeChargeCmdHandler: Maybe we can rearrange this logic a little

**Source stance:** suggestion

**Context:**

> PR 9546 ([EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/InitiateFeeChargeCmdHandler.scala; original row 932.

**Concern stated in the source:** Maybe we can rearrange this logic a little

```
1. if isFullRedemptionFeeChargeAlreadyRequested block: validate if duplicated full redemption fee charge
2. if noFeeChargeRequired block: always waive
3. pattern match on skip details to generate charge request or skip
```

‌

**Source-preserving request, proposal, or question:**

> Maybe we can rearrange this logic a little
> 
> ```
> 1. if isFullRedemptionFeeChargeAlreadyRequested block: validate if duplicated full redemption fee charge
> 2. if noFeeChargeRequired block: always waive
> 3. pattern match on skip details to generate charge request or skip
> ```
> 
> ‌

**Conditions and limits:**

- Preserve ordering: duplicate full-redemption charge check, noFeeChargeRequired waiver, then skip-details charge-or-skip match.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:932 · comment 520046307 · PR 9546 · 2024-07-11

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/InitiateFeeChargeCmdHandler.scala`

**Evidence:** anon-2.jsonl:932 · comment 520046307 · PR 9546 · 2024-07-11

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/InitiateFeeChargeCmdHandler.scala`

**Explicit source context (pr_title):**

> [EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles

## A2-0934 — commands: nit: let’s name this field here and above cmd with same name

**Source stance:** suggestion

**Context:**

> PR 9546 ([EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/commands/commands.scala; original row 934.

**Source-preserving request, proposal, or question:**

> nit: let’s name this field here and above cmd with same name

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:934 · comment 520381308 · PR 9546 · 2024-07-12

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/commands/commands.scala`

**Evidence:** anon-2.jsonl:934 · comment 520381308 · PR 9546 · 2024-07-12

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/commands/commands.scala`

**Explicit source context (hunk):**

> -    initiatingFullRedemptionSettlementDate: LocalDate
> +    initiatingFullRedemptionSettlementDate: LocalDate,
> +    maybePlanFeeChargeSkipRequest: Option[PlanFeeChargeSkipRequest]
>    ) extends FeeManagerCmd
>        with ReplyType[FullRedemptionFeeChargeRequests]
>  

**Evidence:** anon-2.jsonl:934 · comment 520381308 · PR 9546 · 2024-07-12

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/commands/commands.scala`

**Explicit source context (pr_title):**

> [EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles

## A2-0939 — InitiateFeeChargeCmdHandler: Not cleanest code branches, but if we reach here, we already validated `!noFeeChargeRequired`. This is why existing code also calls `maybeAccumulate...

**Source stance:** explanation

**Context:**

> PR 9546 ([EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/InitiateFeeChargeCmdHandler.scala; original row 939.

**Concern stated in the source:** Not cleanest code branches, but if we reach here, we already validated `!noFeeChargeRequired`. This is why existing code also calls `maybeAccumulatedFee.get` directly

**Source-preserving request, proposal, or question:**

> Not cleanest code branches, but if we reach here, we already validated `!noFeeChargeRequired`. This is why existing code also calls `maybeAccumulatedFee.get` directly

**Conditions and limits:**

- .get is accepted here only after !noFeeChargeRequired validation.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:939 · comment 520382469 · PR 9546 · 2024-07-12

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/InitiateFeeChargeCmdHandler.scala`

**Evidence:** anon-2.jsonl:939 · comment 520382469 · PR 9546 · 2024-07-12

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/InitiateFeeChargeCmdHandler.scala`

**Explicit source context (pr_title):**

> [EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles

## A2-0952 — BaseRedemptionCommunicationV2Projection: Can import `TraversableOnceUtils` and use it like this

**Source stance:** suggestion

**Context:**

> PR 9473 (Feat/INV-2450/sg hk retail redemption initiated email v2), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala; original row 952.

**Source-preserving request, proposal, or question:**

> Can import `TraversableOnceUtils` and use it like this
> 
> ```
> instruments
>   .flatMap(_.redemptionDetails.flatMap(_.dealingFrequency))
>   .maxByOption(identity)(DealingFrequencyOrdering)
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:952 · comment 516549655 · PR 9473 · 2024-07-02

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Evidence:** anon-2.jsonl:952 · comment 516549655 · PR 9473 · 2024-07-02

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/processors/BaseRedemptionCommunicationV2Projection.scala`

**Explicit source context (pr_title):**

> Feat/INV-2450/sg hk retail redemption initiated email v2

## A2-0970 — NonAltsFeeManager: There’s a small performance boost here cuz [person] queries tradable-goals by customerId first, and we only care about checking TAA if a plan does not exist i...

**Source stance:** suggestion

**Context:**

> PR 9467 (Resolve INV-3214: Changes to charge cash only fee for fixed maturity product plans.), charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/NonAltsFeeManager.scala; original row 970.

**Concern stated in the source:** There’s a small performance boost here cuz [person] queries tradable-goals by customerId first, and we only care about checking TAA if a plan does not exist in the list. `chargePlanIfEligible` OTOH is already at plan level.

I suppose we can refactor a bit more to reuse this code.

* this customer method checks using `getTradableCustomerGoals`
* then pass whether `isCashOnlyFee` may require overridden or not into `chargePlanIfEligible`
* and `chargePlanIfEligible` will fetch TAA if needed

‌

**Source-preserving request, proposal, or question:**

> There’s a small performance boost here cuz [person] queries tradable-goals by customerId first, and we only care about checking TAA if a plan does not exist in the list. `chargePlanIfEligible` OTOH is already at plan level.
> 
> I suppose we can refactor a bit more to reuse this code.
> 
> * this customer method checks using `getTradableCustomerGoals`
> * then pass whether `isCashOnlyFee` may require overridden or not into `chargePlanIfEligible`
> * and `chargePlanIfEligible` will fetch TAA if needed
> 
> ‌

**Conditions and limits:**

- Customer-level path first checks getTradableCustomerGoals; plan-level path fetches TAA only as needed to override isCashOnlyFee.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:970 · comment 516099105 · PR 9467 · 2024-07-01

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/NonAltsFeeManager.scala`

> There’s a small performance boost here cuz

**Evidence:** anon-2.jsonl:970 · comment 516099105 · PR 9467 · 2024-07-01

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/NonAltsFeeManager.scala`

> queries tradable-goals by customerId first, and we only care about checking TAA if a plan does not exist in the list. `chargePlanIfEligible` OTOH is already at plan level.
> 
> I suppose we can refactor a bit more to reuse this code.
> 
> * this customer method checks using `getTradableCustomerGoals`
> * then pass whether `isCashOnlyFee` may require overridden or not into `chargePlanIfEligible`
> * and `chargePlanIfEligible` will fetch TAA if needed
> 
> ‌

**Evidence:** anon-2.jsonl:970 · comment 516099105 · PR 9467 · 2024-07-01

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/NonAltsFeeManager.scala`

**Explicit source context (pr_title):**

> Resolve INV-3214: Changes to charge cash only fee for fixed maturity product plans.

## A2-0993 — NotifyRebalanceTradeSettlementAmendedCmdHandler: Probably check w trading team but if amendment comes after buy started, the buy amount is already determined

**Source stance:** open-question

**Context:**

> PR 9365 (Feat/INV-3015 rebalance trade settlement amended), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala; original row 993.

**Concern stated in the source:** Probably check w trading team but if amendment comes after buy started, the buy amount is already determined

**Source-preserving request, proposal, or question:**

> Probably check w trading team but if amendment comes after buy started, the buy amount is already determined

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:993 · comment 511513716 · PR 9365 · 2024-06-18

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Evidence:** anon-2.jsonl:993 · comment 511513716 · PR 9365 · 2024-06-18

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3015 rebalance trade settlement amended

## A2-0994 — NotifyRebalanceTradeSettlementAmendedCmdHandler: We need to flip this amount

**Source stance:** observed-defect

**Context:**

> PR 9365 (Feat/INV-3015 rebalance trade settlement amended), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala; original row 994.

**Source-preserving request, proposal, or question:**

> We need to flip this amount

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- The hunk shows totalSoldAmount=Some(cmd.settledAmount); exact amount sign/direction change is not specified by the short comment.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:994 · comment 511564881 · PR 9365 · 2024-06-18

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Evidence:** anon-2.jsonl:994 · comment 511564881 · PR 9365 · 2024-06-18

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Explicit source context (hunk):**

> +         request.copy(
> +          status = request.status, //Status should be the same
> +          lastStatusChangeAt = cmd.settledAt,
> +          sellOrders = cmd.settledOrders,
> +          buyOrders = request.buyOrders,
> +          totalSoldAmount = Some(cmd.settledAmount),
> +          totalPurchasedAmount = request.totalPurchasedAmount,

**Evidence:** anon-2.jsonl:994 · comment 511564881 · PR 9365 · 2024-06-18

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3015 rebalance trade settlement amended

## A2-0995 — NotifyRebalanceTradeSettlementAmendedCmdHandler: Don’t we need more brackets to group these conditions?

**Source stance:** suggestion

**Context:**

> PR 9365 (Feat/INV-3015 rebalance trade settlement amended), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala; original row 995.

**Concern stated in the source:** Don’t we need more brackets to group these conditions?

```
if ((SELL && sellStatus) || (BUY && buyStatuses))
```

‌

**Source-preserving request, proposal, or question:**

> Don’t we need more brackets to group these conditions?
> 
> ```
> if ((SELL && sellStatus) || (BUY && buyStatuses))
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:995 · comment 511513961 · PR 9365 · 2024-06-18

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Evidence:** anon-2.jsonl:995 · comment 511513961 · PR 9365 · 2024-06-18

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3015 rebalance trade settlement amended

## A2-0996 — package: Rename to `NotifyRebalanceTradeSettlementDetailsAmendedCmd`… do the same for event and kafka msg

**Source stance:** suggestion

**Context:**

> PR 9365 (Feat/INV-3015 rebalance trade settlement amended), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/ces/commands/package.scala; original row 996.

**Source-preserving request, proposal, or question:**

> Rename to `NotifyRebalanceTradeSettlementDetailsAmendedCmd`… do the same for event and kafka msg

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:996 · comment 513297484 · PR 9365 · 2024-06-26

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/ces/commands/package.scala`

**Evidence:** anon-2.jsonl:996 · comment 513297484 · PR 9365 · 2024-06-26

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/ces/commands/package.scala`

**Explicit source context (pr_title):**

> Feat/INV-3015 rebalance trade settlement amended

## A2-0997 — NotifyRebalanceTradeSettlementAmendedCmdHandler: This is very dangerous and potentially lead to wonky data state if not done properly by POps. In fact, if you check the entrypoi...

**Source stance:** suggestion

**Context:**

> PR 9365 (Feat/INV-3015 rebalance trade settlement amended), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala; original row 997.

**Concern stated in the source:** This is very dangerous and potentially lead to wonky data state if not done properly by POps. In fact, if you check the entrypoint for `TradeSettlementDetailsAmendedMsg` from trading svc, it comes from `AmendSettledOrderCmd` / `AmendSettledOrderCmdHandler` which doesn’t really update corresponding cash reservation of the order \(applicable for sell\)… and `handleCashReservationForTradeSettlement` in `PlanTraderProjection` doesn’t handle all cases…

**Source-preserving request, proposal, or question:**

> This is very dangerous and potentially lead to wonky data state if not done properly by POps. In fact, if you check the entrypoint for `TradeSettlementDetailsAmendedMsg` from trading svc, it comes from `AmendSettledOrderCmd` / `AmendSettledOrderCmdHandler` which doesn’t really update corresponding cash reservation of the order \(applicable for sell\)… and `handleCashReservationForTradeSettlement` in `PlanTraderProjection` doesn’t handle all cases…

**Conditions and limits:**

- AmendSettledOrderCmd does not update sell-order cash reservations, and PlanTraderProjection does not handle every cash-reservation amendment case.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:997 · comment 513320777 · PR 9365 · 2024-06-26

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Evidence:** anon-2.jsonl:997 · comment 513320777 · PR 9365 · 2024-06-26

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3015 rebalance trade settlement amended

## A2-1001 — NotifyRebalanceTradeSettlementAmendedCmdHandler: As discussed on Slack thread w trading \+ POps, we won’t touch cash reservations, this means buy trade is not affected by amendm...

**Source stance:** explanation

**Context:**

> PR 9365 (Feat/INV-3015 rebalance trade settlement amended), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala; original row 1001.

**Concern stated in the source:** As discussed on Slack thread w trading \+ POps, we won’t touch cash reservations, this means buy trade is not affected by amendment on sell trade. So we allow all these statuses.

**Source-preserving request, proposal, or question:**

> As discussed on Slack thread w trading \+ POps, we won’t touch cash reservations, this means buy trade is not affected by amendment on sell trade. So we allow all these statuses.

**Conditions and limits:**

- Historical agreement: leave cash reservations untouched, so amending sell settlement does not affect buy amount; allow the discussed statuses.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1001 · comment 514084648 · PR 9365 · 2024-06-27

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Evidence:** anon-2.jsonl:1001 · comment 514084648 · PR 9365 · 2024-06-27

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3015 rebalance trade settlement amended

## A2-1002 — NotifyRebalanceTradeSettlementAmendedCmdHandler: If buy trade has not started, and we amend totalSoldAmount but keeping cashReservation intact, we might run into additional cash...

**Source stance:** suggestion

**Context:**

> PR 9365 (Feat/INV-3015 rebalance trade settlement amended), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala; original row 1002.

**Concern stated in the source:** If buy trade has not started, and we amend totalSoldAmount but keeping cashReservation intact, we might run into additional cash reservation for diff amount if we amend up.

So let’s log error and skip this `SELL_TRADE_SETTLED_AWAITING_BUY_PROCESS_TO_BEGIN`

**Source-preserving request, proposal, or question:**

> If buy trade has not started, and we amend totalSoldAmount but keeping cashReservation intact, we might run into additional cash reservation for diff amount if we amend up.
> 
> So let’s log error and skip this `SELL_TRADE_SETTLED_AWAITING_BUY_PROCESS_TO_BEGIN`

**Conditions and limits:**

- Exception to broad status allowance: SELL_TRADE_SETTLED_AWAITING_BUY_PROCESS_TO_BEGIN may create extra diff reservation on an upward amendment; log error and skip.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1002 · comment 514086416 · PR 9365 · 2024-06-27

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Evidence:** anon-2.jsonl:1002 · comment 514086416 · PR 9365 · 2024-06-27

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3015 rebalance trade settlement amended

## A2-1003 — NotifyRebalanceTradeSettlementAmendedCmdHandler: This `cashReservations` is from sell trade, to be used by subsequent buy trade.

**Source stance:** suggestion

**Context:**

> PR 9365 (Feat/INV-3015 rebalance trade settlement amended), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala; original row 1003.

**Concern stated in the source:** This `cashReservations` is from sell trade, to be used by subsequent buy trade.

So we expect this to not changed \(as per current agreement\) even if settledAmount change.

```
cashReservations = if (request.cashReservations != cmd.cashReservations) {
  logger.error(...)
  request.cashReservations
} else {
  request.cashReservations
}
```

‌

**Source-preserving request, proposal, or question:**

> This `cashReservations` is from sell trade, to be used by subsequent buy trade.
> 
> So we expect this to not changed \(as per current agreement\) even if settledAmount change.
> 
> ```
> cashReservations = if (request.cashReservations != cmd.cashReservations) {
>   logger.error(...)
>   request.cashReservations
> } else {
>   request.cashReservations
> }
> ```
> 
> ‌

**Conditions and limits:**

- Preserve existing sell cashReservations even when settledAmount differs, and log only if command cashReservations differ.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1003 · comment 514087743 · PR 9365 · 2024-06-27

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Evidence:** anon-2.jsonl:1003 · comment 514087743 · PR 9365 · 2024-06-27

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3015 rebalance trade settlement amended

## A2-1004 — NotifyRebalanceTradeSettlementAmendedCmdHandler: check if diff, log here as well

**Source stance:** suggestion

**Context:**

> PR 9365 (Feat/INV-3015 rebalance trade settlement amended), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala; original row 1004.

**Source-preserving request, proposal, or question:**

> check if diff, log here as well

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- The comment requests difference-check logging in settlement amendment; rows 1002–1003 explain the cash-reservation context.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1004 · comment 514088207 · PR 9365 · 2024-06-27

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Evidence:** anon-2.jsonl:1004 · comment 514088207 · PR 9365 · 2024-06-27

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Explicit source context (hunk):**

> +          status = request.status, //Status should be the same
> +          lastStatusChangeAt = cmd.settledAt,
> +          sellOrders = cmd.settledOrders,
> +          buyOrders = request.buyOrders,
> +          totalSoldAmount = Some(cmd.settledAmount),
> +          totalPurchasedAmount = request.totalPurchasedAmount,
> +          cashReservations = request.cashReservations

**Evidence:** anon-2.jsonl:1004 · comment 514088207 · PR 9365 · 2024-06-27

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3015 rebalance trade settlement amended

## A2-1005 — NotifyRebalanceTradeSettlementAmendedCmdHandler: No need to check here

**Source stance:** suggestion

**Context:**

> PR 9365 (Feat/INV-3015 rebalance trade settlement amended), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala; original row 1005.

**Source-preserving request, proposal, or question:**

> No need to check here

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1005 · comment 514090072 · PR 9365 · 2024-06-27

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Evidence:** anon-2.jsonl:1005 · comment 514090072 · PR 9365 · 2024-06-27

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Explicit source context (hunk):**

> +          cashReservations = request.cashReservations
> +        )
> +      case BuySell.BUY =>
> +        request.copy(
> +          status = request.status, //Status should be the same
> +          lastStatusChangeAt = cmd.settledAt,
> +          sellOrders = request.sellOrders,

**Evidence:** anon-2.jsonl:1005 · comment 514090072 · PR 9365 · 2024-06-27

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/NotifyRebalanceTradeSettlementAmendedCmdHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3015 rebalance trade settlement amended

## A2-1006 — RedemptionRequestTopicSubscriberV3: Not sure if we need all these validation in transaction svc. Maybe just dump directly with status = `SETTLEMENT_CONFIRMED`.

**Source stance:** suggestion

**Context:**

> PR 9388 (Feat/INV-3183 redemption amend settlement), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala; original row 1006.

**Concern stated in the source:** Not sure if we need all these validation in transaction svc. Maybe just dump directly with status = `SETTLEMENT_CONFIRMED`.

State validation should happen upstream, not here I think

**Source-preserving request, proposal, or question:**

> Not sure if we need all these validation in transaction svc. Maybe just dump directly with status = `SETTLEMENT_CONFIRMED`.
> 
> State validation should happen upstream, not here I think

**Conditions and limits:**

- Upstream state validation and direct SETTLEMENT_CONFIRMED transaction update is proposed, not established safe behavior.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1006 · comment 512144974 · PR 9388 · 2024-06-20

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1006 · comment 512144974 · PR 9388 · 2024-06-20

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RedemptionRequestTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> Feat/INV-3183 redemption amend settlement

## A2-1009 — package: Name should be `AmendSettlementCmd`. Update for cmd handler too

**Source stance:** suggestion

**Context:**

> PR 9388 (Feat/INV-3183 redemption amend settlement), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/ces/commands/package.scala; original row 1009.

**Source-preserving request, proposal, or question:**

> Name should be `AmendSettlementCmd`. Update for cmd handler too

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1009 · comment 512143421 · PR 9388 · 2024-06-20

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/ces/commands/package.scala`

**Evidence:** anon-2.jsonl:1009 · comment 512143421 · PR 9388 · 2024-06-20

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/ces/commands/package.scala`

**Explicit source context (pr_title):**

> Feat/INV-3183 redemption amend settlement

## A2-1010 — SettlementAmendedCmdHandler: So this flag `chargeFeeForFullRedemption` is not used? How does this flow work if we amend for full redemption? Probably a question for trading team...

**Source stance:** open-question

**Context:**

> PR 9388 (Feat/INV-3183 redemption amend settlement), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/handlers/SettlementAmendedCmdHandler.scala; original row 1010.

**Concern stated in the source:** So this flag `chargeFeeForFullRedemption` is not used? How does this flow work if we amend for full redemption? Probably a question for trading team and POps…

**Source-preserving request, proposal, or question:**

> So this flag `chargeFeeForFullRedemption` is not used? How does this flow work if we amend for full redemption? Probably a question for trading team and POps…

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1010 · comment 512144082 · PR 9388 · 2024-06-20

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/handlers/SettlementAmendedCmdHandler.scala`

**Evidence:** anon-2.jsonl:1010 · comment 512144082 · PR 9388 · 2024-06-20

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/handlers/SettlementAmendedCmdHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3183 redemption amend settlement

## A2-1011 — SettlementAmendedCmdHandler: Ok this one is not safe. On redemption trade side, cash reservations \(if any\) correspond to each individual orders, however if full redemption fee...

**Source stance:** suggestion

**Context:**

> PR 9388 (Feat/INV-3183 redemption amend settlement), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/handlers/SettlementAmendedCmdHandler.scala; original row 1011.

**Concern stated in the source:** Ok this one is not safe. On redemption trade side, cash reservations \(if any\) correspond to each individual orders, however if full redemption fee charge is involved, they will be merged and split to fund the fee amount.

Examples:

```
Normal redemption of 600 from 3 orders
{
  "settlementConfirmation": {
    "cashReservations": [100, 200, 300]
  },
  "cashReservations": [100, 200, 300]
}

Full redemption of 600 from 3 orders, with charge 10
{
  "settlementConfirmation": {
    "cashReservations": [100, 200, 300]
  },
  "cashReservations": [590]
}
```

‌

Amendment comes for full redemption comes, outer `cashReservations` needs to be updated/resplit from the settlement cash reservations

```
Full redemption of 600 -> 650 from 3 orders, with charge 10
{
  "settlementConfirmation": {
    "cashReservations": [100 -> 150, 200, 300]
  },
  "cashReservations": [640]
}
```

‌

**Source-preserving request, proposal, or question:**

> Ok this one is not safe. On redemption trade side, cash reservations \(if any\) correspond to each individual orders, however if full redemption fee charge is involved, they will be merged and split to fund the fee amount.
> 
> Examples:
> 
> ```
> Normal redemption of 600 from 3 orders
> {
>   "settlementConfirmation": {
>     "cashReservations": [100, 200, 300]
>   },
>   "cashReservations": [100, 200, 300]
> }
> 
> Full redemption of 600 from 3 orders, with charge 10
> {
>   "settlementConfirmation": {
>     "cashReservations": [100, 200, 300]
>   },
>   "cashReservations": [590]
> }
> ```
> 
> ‌
> 
> Amendment comes for full redemption comes, outer `cashReservations` needs to be updated/resplit from the settlement cash reservations
> 
> ```
> Full redemption of 600 -> 650 from 3 orders, with charge 10
> {
>   "settlementConfirmation": {
>     "cashReservations": [100 -> 150, 200, 300]
>   },
>   "cashReservations": [640]
> }
> ```
> 
> ‌

**Conditions and limits:**

- Specific counterexample: normal settlement [100,200,300]→outer [100,200,300]; full-redemption fee 10 produces [590]; amending first order 100→150 requires outer [640]. Later rows 1013–1015 retain reservations under an agreement that trading will not change them.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1011 · comment 513296334 · PR 9388 · 2024-06-25

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/handlers/SettlementAmendedCmdHandler.scala`

**Evidence:** anon-2.jsonl:1011 · comment 513296334 · PR 9388 · 2024-06-25

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/handlers/SettlementAmendedCmdHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3183 redemption amend settlement

## A2-1013 — SettlementAmendedCmdHandler: Only log this error if current `request.settlementConfirmation.cashReservations` is different from `cmd.cashReservations`… currently trading side wo...

**Source stance:** suggestion

**Context:**

> PR 9388 (Feat/INV-3183 redemption amend settlement), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/handlers/SettlementAmendedCmdHandler.scala; original row 1013.

**Concern stated in the source:** Only log this error if current `request.settlementConfirmation.cashReservations` is different from `cmd.cashReservations`… currently trading side won’t update anything in this `cmd.cashReservations`, and discussed on Slack thread, nothing to check further for this on redemption side

**Source-preserving request, proposal, or question:**

> Only log this error if current `request.settlementConfirmation.cashReservations` is different from `cmd.cashReservations`… currently trading side won’t update anything in this `cmd.cashReservations`, and discussed on Slack thread, nothing to check further for this on redemption side

**Conditions and limits:**

- The proposed logging condition compares current settlementConfirmation.cashReservations to command cashReservations; settled-amount divergence is expected.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1013 · comment 514077006 · PR 9388 · 2024-06-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/handlers/SettlementAmendedCmdHandler.scala`

**Evidence:** anon-2.jsonl:1013 · comment 514077006 · PR 9388 · 2024-06-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/handlers/SettlementAmendedCmdHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3183 redemption amend settlement

## A2-1014 — SettlementAmendedCmdHandler: The settled amount surely is going to be diverged \(exactly the point of the amendment\). We want to log if the cash reservations also changes \(exp...

**Source stance:** suggestion

**Context:**

> PR 9388 (Feat/INV-3183 redemption amend settlement), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/handlers/SettlementAmendedCmdHandler.scala; original row 1014.

**Concern stated in the source:** The settled amount surely is going to be diverged \(exactly the point of the amendment\). We want to log if the cash reservations also changes \(expectation right now is that it should not change\)

**Source-preserving request, proposal, or question:**

> The settled amount surely is going to be diverged \(exactly the point of the amendment\). We want to log if the cash reservations also changes \(expectation right now is that it should not change\)

**Conditions and limits:**

- This clarifies that settledAmount is expected to diverge; only unexpected cash-reservation changes should alert.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1014 · comment 514079559 · PR 9388 · 2024-06-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/handlers/SettlementAmendedCmdHandler.scala`

**Evidence:** anon-2.jsonl:1014 · comment 514079559 · PR 9388 · 2024-06-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/handlers/SettlementAmendedCmdHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3183 redemption amend settlement

## A2-1015 — SettlementAmendedCmdHandler: ```

**Source stance:** suggestion

**Context:**

> PR 9388 (Feat/INV-3183 redemption amend settlement), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/handlers/SettlementAmendedCmdHandler.scala; original row 1015.

**Concern stated in the source:** ```
cashReservations = if (cmd.cashReservations != request.settlementConfirmation.get.cashReservations) {
  logger.error(...)
  request.cashReservations
} else {
  request.cashReservations
}
```

‌

**Source-preserving request, proposal, or question:**

> ```
> cashReservations = if (cmd.cashReservations != request.settlementConfirmation.get.cashReservations) {
>   logger.error(...)
>   request.cashReservations
> } else {
>   request.cashReservations
> }
> ```
> 
> ‌

**Conditions and limits:**

- Code proposal preserves request.cashReservations in both branches and logs mismatch against request.settlementConfirmation.get.cashReservations.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1015 · comment 514082843 · PR 9388 · 2024-06-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/handlers/SettlementAmendedCmdHandler.scala`

**Evidence:** anon-2.jsonl:1015 · comment 514082843 · PR 9388 · 2024-06-27

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/handlers/SettlementAmendedCmdHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3183 redemption amend settlement

## A2-1035 — CustomerAdvisoryProfileEntity: Yea, luckily we haven’t launched DPM, so no customers currently have valid DPM status and in VC grace period. So we can afford to leave with this ...

**Source stance:** explanation

**Context:**

> PR 9392 (Feat/INV-3186 CRA age), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileEntity.scala; original row 1035.

**Concern stated in the source:** Yea, luckily we haven’t launched DPM, so no customers currently have valid DPM status and in VC grace period. So we can afford to leave with this until they exit grace period \(either by force or retake :laughing: \)

**Source-preserving request, proposal, or question:**

> Yea, luckily we haven’t launched DPM, so no customers currently have valid DPM status and in VC grace period. So we can afford to leave with this until they exit grace period \(either by force or retake :laughing: \)

**Conditions and limits:**

- Temporary VC-grace handling is tolerated only because DPM has not launched and no customers occupy that state.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1035 · comment 512174219 · PR 9392 · 2024-06-20

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileEntity.scala`

**Evidence:** anon-2.jsonl:1035 · comment 512174219 · PR 9392 · 2024-06-20

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileEntity.scala`

**Explicit source context (pr_title):**

> Feat/INV-3186 CRA age

## A2-1050 — GoalBasedStatementInfoDbDto: I’m not sure if we need all these new fields in `*DbDto`. As I understand, these DTO are persisted and used to check if a statement is reprint or not.

**Source stance:** explanation

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-impl/src/main/scala/com/endowus/silver/report/impl/statement/db/goalBased/model/GoalBasedStatementInfoDbDto.scala; original row 1050.

**Concern stated in the source:** I’m not sure if we need all these new fields in `*DbDto`. As I understand, these DTO are persisted and used to check if a statement is reprint or not.

Generally, we do not change isDiscretionary flag of a goal - even if we do, we probably can force-reprint if needed, rather than storing these fields?

--

Even if we don’t change these DTO, the page content would already changed due to new format. It’s a more generic question for report svc, how do we version the statement design to avoid mass reprint / support ability to print an old month using old format, etc…

**Source-preserving request, proposal, or question:**

> I’m not sure if we need all these new fields in `*DbDto`. As I understand, these DTO are persisted and used to check if a statement is reprint or not.
> 
> Generally, we do not change isDiscretionary flag of a goal - even if we do, we probably can force-reprint if needed, rather than storing these fields?
> 
> --
> 
> Even if we don’t change these DTO, the page content would already changed due to new format. It’s a more generic question for report svc, how do we version the statement design to avoid mass reprint / support ability to print an old month using old format, etc…

**Conditions and limits:**

- Persisted *DbDto fields drive reprint detection. isDiscretionary rarely changes and force-reprint may suffice; broader old-format/versioning versus mass-reprint question is unresolved.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1050 · comment 502458481 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/db/goalBased/model/GoalBasedStatementInfoDbDto.scala`

**Evidence:** anon-2.jsonl:1050 · comment 502458481 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/db/goalBased/model/GoalBasedStatementInfoDbDto.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1051 — StatementPageDataDto: Still feel that `numberOfDiscretionaryGoals` and `startOfNonDPMGoalIndex` are duplicating each other. I feel we should be able to make it work with just on...

**Source stance:** suggestion

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-api/src/main/scala/com/endowus/silver/report/api/commons/goalBasedStatement/models/StatementPageDataDto.scala; original row 1051.

**Concern stated in the source:** Still feel that `numberOfDiscretionaryGoals` and `startOfNonDPMGoalIndex` are duplicating each other. I feel we should be able to make it work with just one variable

**Source-preserving request, proposal, or question:**

> Still feel that `numberOfDiscretionaryGoals` and `startOfNonDPMGoalIndex` are duplicating each other. I feel we should be able to make it work with just one variable

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1051 · comment 502455582 · PR 9052 · 2024-05-21

Source path: `report-api/src/main/scala/com/endowus/silver/report/api/commons/goalBasedStatement/models/StatementPageDataDto.scala`

**Evidence:** anon-2.jsonl:1051 · comment 502455582 · PR 9052 · 2024-05-21

Source path: `report-api/src/main/scala/com/endowus/silver/report/api/commons/goalBasedStatement/models/StatementPageDataDto.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1052 — GoalBasedStatementDataGenerator: Use the `empty`?

**Source stance:** suggestion

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/GoalBasedStatementDataGenerator.scala; original row 1052.

**Source-preserving request, proposal, or question:**

> Use the `empty`?

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1052 · comment 502461376 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/GoalBasedStatementDataGenerator.scala`

**Evidence:** anon-2.jsonl:1052 · comment 502461376 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/GoalBasedStatementDataGenerator.scala`

**Explicit source context (hunk):**

>          (PlanRowItem(detailInPlanCcy, detailInDisplayCcy), planPerm)
>        }
>  
> -      // TBD: Continue to display no activity goals on all investments page. Hence not using 'goalsInfoForDisplayWithSomeActivity'
> -      val goalDetails: List[GoalRowDetails] = rawData.goalsInfoForDisplay.map {
> -        case (goalId, goalName, planInfo) =>

**Evidence:** anon-2.jsonl:1052 · comment 502461376 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/GoalBasedStatementDataGenerator.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1053 — GoalBasedStatementDataGenerator: Let’s reverse the goalDetails here before returning, so it’s easier to follow… a bit out of context when we reverse when assigning to `AllInvest...

**Source stance:** suggestion

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/GoalBasedStatementDataGenerator.scala; original row 1053.

**Concern stated in the source:** Let’s reverse the goalDetails here before returning, so it’s easier to follow… a bit out of context when we reverse when assigning to `AllInvestmentGoalsPageData.goalDetails` later

**Source-preserving request, proposal, or question:**

> Let’s reverse the goalDetails here before returning, so it’s easier to follow… a bit out of context when we reverse when assigning to `AllInvestmentGoalsPageData.goalDetails` later

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1053 · comment 502462046 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/GoalBasedStatementDataGenerator.scala`

**Evidence:** anon-2.jsonl:1053 · comment 502462046 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/GoalBasedStatementDataGenerator.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1054 — PageDataGenerator: Similar here… “SG AllInvestmentGoals templates do not distinguish DPM and non-DPM goals, hence treating all goals as non-DPM”

**Source stance:** suggestion

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/PageDataGenerator.scala; original row 1054.

**Concern stated in the source:** Similar here… “SG AllInvestmentGoals templates do not distinguish DPM and non-DPM goals, hence treating all goals as non-DPM”

**Source-preserving request, proposal, or question:**

> Similar here… “SG AllInvestmentGoals templates do not distinguish DPM and non-DPM goals, hence treating all goals as non-DPM”

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1054 · comment 502463913 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/PageDataGenerator.scala`

**Evidence:** anon-2.jsonl:1054 · comment 502463913 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/PageDataGenerator.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1055 — StatementPageData: Let’s use named var, e.g. `startingBalance = startingBalance + other.startingBalance`. A bit easier to read, and safer to refactor later

**Source stance:** suggestion

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-impl/src/main/scala/com/endowus/silver/report/impl/pdfGenerator/models/StatementPageData.scala; original row 1055.

**Concern stated in the source:** Let’s use named var, e.g. `startingBalance = startingBalance + other.startingBalance`. A bit easier to read, and safer to refactor later

**Source-preserving request, proposal, or question:**

> Let’s use named var, e.g. `startingBalance = startingBalance + other.startingBalance`. A bit easier to read, and safer to refactor later

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1055 · comment 502456618 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/pdfGenerator/models/StatementPageData.scala`

**Evidence:** anon-2.jsonl:1055 · comment 502456618 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/pdfGenerator/models/StatementPageData.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1056 — package: Should be compatible cuz this is not persisted \(only the `*DbDto` are persisted\).

**Source stance:** suggestion

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-api/src/main/scala/com/endowus/silver/report/api/commons/statement/package.scala; original row 1056.

**Concern stated in the source:** Should be compatible cuz this is not persisted \(only the `*DbDto` are persisted\).

I see some lookup done by traversing this list. If it’s safe to refactor, should we just change to

```
goalIdsToDisplay: List[UUID], // ordering is maintained here
goalInfoByGoalId: Map[UUID, GoalInfoToDisplay] // lookup only
```

‌

**Source-preserving request, proposal, or question:**

> Should be compatible cuz this is not persisted \(only the `*DbDto` are persisted\).
> 
> I see some lookup done by traversing this list. If it’s safe to refactor, should we just change to
> 
> ```
> goalIdsToDisplay: List[UUID], // ordering is maintained here
> goalInfoByGoalId: Map[UUID, GoalInfoToDisplay] // lookup only
> ```
> 
> ‌

**Conditions and limits:**

- List+Map is a proposed lookup/order refactor, but row 1064 later accepts leaving it a List after usage review. Only *DbDto are persisted.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1056 · comment 502456452 · PR 9052 · 2024-05-21

Source path: `report-api/src/main/scala/com/endowus/silver/report/api/commons/statement/package.scala`

**Evidence:** anon-2.jsonl:1056 · comment 502456452 · PR 9052 · 2024-05-21

Source path: `report-api/src/main/scala/com/endowus/silver/report/api/commons/statement/package.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1057 — GoalBasedStatementDataGenerator: Maybe give a bit more context.. “SG CoverPage templates do not distinguish DPM and non-DPM goals, hence treating all goals as non-DPM”

**Source stance:** suggestion

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/GoalBasedStatementDataGenerator.scala; original row 1057.

**Concern stated in the source:** Maybe give a bit more context.. “SG CoverPage templates do not distinguish DPM and non-DPM goals, hence treating all goals as non-DPM”

‌

**Source-preserving request, proposal, or question:**

> Maybe give a bit more context.. “SG CoverPage templates do not distinguish DPM and non-DPM goals, hence treating all goals as non-DPM”
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1057 · comment 502463332 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/GoalBasedStatementDataGenerator.scala`

**Evidence:** anon-2.jsonl:1057 · comment 502463332 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/GoalBasedStatementDataGenerator.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1058 — GoalBasedStatementDataGenerator: Maybe put a comment here to explain this is just dummy value as base input. We have this thing just because we reuse the same case class for inp...

**Source stance:** suggestion

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/GoalBasedStatementDataGenerator.scala; original row 1058.

**Concern stated in the source:** Maybe put a comment here to explain this is just dummy value as base input. We have this thing just because we reuse the same case class for input and response

**Source-preserving request, proposal, or question:**

> Maybe put a comment here to explain this is just dummy value as base input. We have this thing just because we reuse the same case class for input and response

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1058 · comment 502462630 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/GoalBasedStatementDataGenerator.scala`

**Evidence:** anon-2.jsonl:1058 · comment 502462630 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/GoalBasedStatementDataGenerator.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1059 — PageDataGenerator: Actually we have too many region pattern matching in this method. Maybe consolidate it a bit

**Source stance:** suggestion

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/PageDataGenerator.scala; original row 1059.

**Concern stated in the source:** Actually we have too many region pattern matching in this method. Maybe consolidate it a bit

```
def headTailMapper(...)

def generate(goals: List[GoalRowDetails], isDPM: Boolean, maxRowsInFirstPage: Int, firstPageTemplate: String, subsequentPageTemplate: String): List[(AllInvestmentGoalsPageData, String)] = ...

region match {
  case SilverRegion.Sg =>
    // SG AllInvestmentGoals templates do not distinguish DPM and non-DPM goals, hence treating all goals as non-DPM
    generate(
      goals = pageData.goalDetails.asScala.toList,
      isDPM = false,
      maxRowsInFirstPage = maxRowsPerAllInvestmentsPage,
      firstPageTemplate = "allInvestmentGoalsPage",
      subsequentPageTemplate = "allInvestmentGoalsPureGoalsPage"
    )
  case SilverRegion.Hk =>
    // HK AllInvestmentGoals templates have special empty page
    if (pageData.goalDetails.isEmpty) {
      List((pageData.copy(goalDetails = pageData.goalDetails), "allInvestmentGoalsPageWithoutGoal"))
    } else {
      val allInvestmentDPMPageData = generate(
        goals = pageData.goalDetails.asScala.toList.filter(_.isDiscretionary),
        isDPM = true,
        maxRowsInFirstPage = maxRowsPerAllInvestmentsPageForFirstDPMPage,
        firstPageTemplate = "allInvestmentGoalsPage",
        subsequentPageTemplate = "allInvestmentGoalsPureGoalsPage"
      )
      val allInvestmentNonDPMPageData = generate(
        goals = pageData.goalDetails.asScala.toList.filterNot(_.isDiscretionary),
        isDPM = false,
        maxRowsInFirstPage = maxRowsPerAllInvestmentsPage,
        firstPageTemplate = "allInvestmentNonDPMGoalsPage",
        subsequentPageTemplate = "allInvestmentGoalsPureGoalsPage"
      )
      allInvestmentDPMPageData ++ allInvestmentNonDPMPageData
    }
  case _ => throw new Exception(s"AllInvestmentGoalsPageData generator behaviour not configured for region $region.")
}
```

‌

**Source-preserving request, proposal, or question:**

> Actually we have too many region pattern matching in this method. Maybe consolidate it a bit
> 
> ```
> def headTailMapper(...)
> 
> def generate(goals: List[GoalRowDetails], isDPM: Boolean, maxRowsInFirstPage: Int, firstPageTemplate: String, subsequentPageTemplate: String): List[(AllInvestmentGoalsPageData, String)] = ...
> 
> region match {
>   case SilverRegion.Sg =>
>     // SG AllInvestmentGoals templates do not distinguish DPM and non-DPM goals, hence treating all goals as non-DPM
>     generate(
>       goals = pageData.goalDetails.asScala.toList,
>       isDPM = false,
>       maxRowsInFirstPage = maxRowsPerAllInvestmentsPage,
>       firstPageTemplate = "allInvestmentGoalsPage",
>       subsequentPageTemplate = "allInvestmentGoalsPureGoalsPage"
>     )
>   case SilverRegion.Hk =>
>     // HK AllInvestmentGoals templates have special empty page
>     if (pageData.goalDetails.isEmpty) {
>       List((pageData.copy(goalDetails = pageData.goalDetails), "allInvestmentGoalsPageWithoutGoal"))
>     } else {
>       val allInvestmentDPMPageData = generate(
>         goals = pageData.goalDetails.asScala.toList.filter(_.isDiscretionary),
>         isDPM = true,
>         maxRowsInFirstPage = maxRowsPerAllInvestmentsPageForFirstDPMPage,
>         firstPageTemplate = "allInvestmentGoalsPage",
>         subsequentPageTemplate = "allInvestmentGoalsPureGoalsPage"
>       )
>       val allInvestmentNonDPMPageData = generate(
>         goals = pageData.goalDetails.asScala.toList.filterNot(_.isDiscretionary),
>         isDPM = false,
>         maxRowsInFirstPage = maxRowsPerAllInvestmentsPage,
>         firstPageTemplate = "allInvestmentNonDPMGoalsPage",
>         subsequentPageTemplate = "allInvestmentGoalsPureGoalsPage"
>       )
>       allInvestmentDPMPageData ++ allInvestmentNonDPMPageData
>     }
>   case _ => throw new Exception(s"AllInvestmentGoalsPageData generator behaviour not configured for region $region.")
> }
> ```
> 
> ‌

**Conditions and limits:**

- Preserve SG all-non-DPM template handling versus HK DPM/non-DPM splitting and special empty page; the entire example is a proposal.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1059 · comment 502467840 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/PageDataGenerator.scala`

**Evidence:** anon-2.jsonl:1059 · comment 502467840 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/PageDataGenerator.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1060 — StatementPageDataDto: Let’s rename it to `totalNumberOfDiscretionaryGoals` then

**Source stance:** suggestion

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-api/src/main/scala/com/endowus/silver/report/api/commons/goalBasedStatement/models/StatementPageDataDto.scala; original row 1060.

**Source-preserving request, proposal, or question:**

> Let’s rename it to `totalNumberOfDiscretionaryGoals` then

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1060 · comment 502493476 · PR 9052 · 2024-05-21

Source path: `report-api/src/main/scala/com/endowus/silver/report/api/commons/goalBasedStatement/models/StatementPageDataDto.scala`

**Evidence:** anon-2.jsonl:1060 · comment 502493476 · PR 9052 · 2024-05-21

Source path: `report-api/src/main/scala/com/endowus/silver/report/api/commons/goalBasedStatement/models/StatementPageDataDto.scala`

**Explicit source context (hunk):**

> +  showDisclaimer: Boolean = false,
> +  startOfNonDiscretionaryGoalIndex: Int = -1
>  ) extends StatementPageDataDto
>  
>  object CoverPageDataDto {

**Evidence:** anon-2.jsonl:1060 · comment 502493476 · PR 9052 · 2024-05-21

Source path: `report-api/src/main/scala/com/endowus/silver/report/api/commons/goalBasedStatement/models/StatementPageDataDto.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1061 — GoalBasedStatementInfoDbDto: Yea so I think adding these new fields to `*DbDto` can cause confusion for existing data if we don’t retrospectively update them.

**Source stance:** explanation

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-impl/src/main/scala/com/endowus/silver/report/impl/statement/db/goalBased/model/GoalBasedStatementInfoDbDto.scala; original row 1061.

**Concern stated in the source:** Yea so I think adding these new fields to `*DbDto` can cause confusion for existing data if we don’t retrospectively update them.

Based on my understanding, it seems these new fields are not needed anyway. The new design will anyway cause it to be reprinted cuz we have the new page split for AllInvestmentGoals pages \+ the ordering for other goal pages. Other than that, once new design is printed, these isDpm flags are no longer useful, cuz goal cannot change its dpm flag.

**Source-preserving request, proposal, or question:**

> Yea so I think adding these new fields to `*DbDto` can cause confusion for existing data if we don’t retrospectively update them.
> 
> Based on my understanding, it seems these new fields are not needed anyway. The new design will anyway cause it to be reprinted cuz we have the new page split for AllInvestmentGoals pages \+ the ordering for other goal pages. Other than that, once new design is printed, these isDpm flags are no longer useful, cuz goal cannot change its dpm flag.

**Conditions and limits:**

- New format already forces reprinting through page splitting/order changes; mutable persisted isDpm fields are considered unnecessary and confusing without retrospective data updates.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1061 · comment 502499163 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/db/goalBased/model/GoalBasedStatementInfoDbDto.scala`

**Evidence:** anon-2.jsonl:1061 · comment 502499163 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/db/goalBased/model/GoalBasedStatementInfoDbDto.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1062 — StatementPdfGeneratorTest: I suppose this assertion at best can only verify the html templates don’t throw error, and that some pdf file is generated.

**Source stance:** suggestion

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-impl/src/test/scala/com/endowus/silver/report/impl/pdfGenerator/statementPdfGenerator/StatementPdfGeneratorTest.scala; original row 1062.

**Concern stated in the source:** I suppose this assertion at best can only verify the html templates don’t throw error, and that some pdf file is generated.

IDK how we can effectively assert the result of the template \(since it has logic\). But at least, let’s validate the result of `PageDataGenerator`, e.g. for CoverPage, let’s also also check number of pageData returned, for each of them, validate the dynamic fields `goalNames` / `startOfNonDPMGoalIndex` / `showDisclaimer` as well as the corresponding templateName.

Then we do the same for AllInvestmentGoals page. For the rest, I’m ok with not touching as we know we don’t change them much other than just additional isDpm flag

**Source-preserving request, proposal, or question:**

> I suppose this assertion at best can only verify the html templates don’t throw error, and that some pdf file is generated.
> 
> IDK how we can effectively assert the result of the template \(since it has logic\). But at least, let’s validate the result of `PageDataGenerator`, e.g. for CoverPage, let’s also also check number of pageData returned, for each of them, validate the dynamic fields `goalNames` / `startOfNonDPMGoalIndex` / `showDisclaimer` as well as the corresponding templateName.
> 
> Then we do the same for AllInvestmentGoals page. For the rest, I’m ok with not touching as we know we don’t change them much other than just additional isDpm flag

**Conditions and limits:**

- Successful HTML/PDF rendering only verifies no template throw; PageDataGenerator tests must assert page count, goalNames/startOfNonDPMGoalIndex/showDisclaimer and template names.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1062 · comment 503069656 · PR 9052 · 2024-05-22

Source path: `report-impl/src/test/scala/com/endowus/silver/report/impl/pdfGenerator/statementPdfGenerator/StatementPdfGeneratorTest.scala`

**Evidence:** anon-2.jsonl:1062 · comment 503069656 · PR 9052 · 2024-05-22

Source path: `report-impl/src/test/scala/com/endowus/silver/report/impl/pdfGenerator/statementPdfGenerator/StatementPdfGeneratorTest.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1063 — PageDataGenerator: Can we change this method to additionally return `maxNoOfRowCanFitOnCurrentPage`? I find it a bit funky to check the template name again below. Maybe sth like...

**Source stance:** suggestion

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/PageDataGenerator.scala; original row 1063.

**Concern stated in the source:** Can we change this method to additionally return `maxNoOfRowCanFitOnCurrentPage`? I find it a bit funky to check the template name again below. Maybe sth like this?

```
private def getTemplateWithShowDisclaimer(startIndex: Int, endIndex: Int, rowsToAccountForExtraHeading: Int): (Boolean, String, Int) = {
  startIndex match {
    case 0 =>
      val maxRowsInFirstPage = MaxRowsCanFitAfterAllInvestmentAaaGoalsHeadingAreAccounted - rowsToAccountForExtraHeading
      (false, "coverPageWithoutCashBalanceGlossaryDisclaimer", maxRowsInFirstPage)
    case _ =>
      val maxRowsInSubsequentPage = MaxRowsCanFitOnCoverPage - rowsToAccountForExtraHeading
      val canFitWithEndingSection = (endIndex - startIndex) <= (maxRowsInSubsequentPage - CashBalUnderstandingStatementDisclaimer)
      (canFitWithEndingSection, "coverPagePureGoal", MaxRowsCanFitOnCoverPage - rowsToAccountForExtraHeading)
  }
}
```

‌

Then here we just need

```
val (showDisclaimer, templateName, maxNoOfRowCanFitOnCurrentPage) = getTemplateWithShowDisclaimer(startIndex, endIndex, rowsToAccountForExtraHeading)
```

‌

**Source-preserving request, proposal, or question:**

> Can we change this method to additionally return `maxNoOfRowCanFitOnCurrentPage`? I find it a bit funky to check the template name again below. Maybe sth like this?
> 
> ```
> private def getTemplateWithShowDisclaimer(startIndex: Int, endIndex: Int, rowsToAccountForExtraHeading: Int): (Boolean, String, Int) = {
>   startIndex match {
>     case 0 =>
>       val maxRowsInFirstPage = MaxRowsCanFitAfterAllInvestmentAaaGoalsHeadingAreAccounted - rowsToAccountForExtraHeading
>       (false, "coverPageWithoutCashBalanceGlossaryDisclaimer", maxRowsInFirstPage)
>     case _ =>
>       val maxRowsInSubsequentPage = MaxRowsCanFitOnCoverPage - rowsToAccountForExtraHeading
>       val canFitWithEndingSection = (endIndex - startIndex) <= (maxRowsInSubsequentPage - CashBalUnderstandingStatementDisclaimer)
>       (canFitWithEndingSection, "coverPagePureGoal", MaxRowsCanFitOnCoverPage - rowsToAccountForExtraHeading)
>   }
> }
> ```
> 
> ‌
> 
> Then here we just need
> 
> ```
> val (showDisclaimer, templateName, maxNoOfRowCanFitOnCurrentPage) = getTemplateWithShowDisclaimer(startIndex, endIndex, rowsToAccountForExtraHeading)
> ```
> 
> ‌

**Conditions and limits:**

- Return (showDisclaimer, templateName, maxNoOfRowCanFitOnCurrentPage) directly so callers do not reverse-engineer row limits from template names.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1063 · comment 503063922 · PR 9052 · 2024-05-22

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/PageDataGenerator.scala`

**Evidence:** anon-2.jsonl:1063 · comment 503063922 · PR 9052 · 2024-05-22

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/PageDataGenerator.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1064 — package: [person] after checking the usage of this class again, I’m convinced that

**Source stance:** explanation

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-api/src/main/scala/com/endowus/silver/report/api/commons/statement/package.scala; original row 1064.

**Concern stated in the source:** [person] after checking the usage of this class again, I’m convinced that

* it’s not used for public DTO - let’s move to report-impl instead, otherwise it can be confusing to see `*RawData` case class in report-api. I think these can just stay in `GoalBasedStatementDataGenerator`
* it’s not used at all for serdes, not even in test - so we don’t need the format at all

‌

I checked the lookup usage of this `goalsInfoForDisplay`. Not too bad so I guess we can leave it as a List still. But let’s move both `GoalBasedStatementRawData` and `GoalInfoToDisplay` to impl so that it’s less confusing on usage scope

**Source-preserving request, proposal, or question:**

> [person] after checking the usage of this class again, I’m convinced that
> 
> * it’s not used for public DTO - let’s move to report-impl instead, otherwise it can be confusing to see `*RawData` case class in report-api. I think these can just stay in `GoalBasedStatementDataGenerator`
> * it’s not used at all for serdes, not even in test - so we don’t need the format at all
> 
> ‌
> 
> I checked the lookup usage of this `goalsInfoForDisplay`. Not too bad so I guess we can leave it as a List still. But let’s move both `GoalBasedStatementRawData` and `GoalInfoToDisplay` to impl so that it’s less confusing on usage scope

**Conditions and limits:**

- After inspection, raw-data classes are neither public DTOs nor serialized; move GoalBasedStatementRawData/GoalInfoToDisplay into report-impl and remove format. List lookup is accepted, revising row 1056.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1064 · comment 503067120 · PR 9052 · 2024-05-22

Source path: `report-api/src/main/scala/com/endowus/silver/report/api/commons/statement/package.scala`

> after checking the usage of this class again, I’m convinced that
> 
> * it’s not used for public DTO - let’s move to report-impl instead, otherwise it can be confusing to see `*RawData` case class in report-api. I think these can just stay in `GoalBasedStatementDataGenerator`
> * it’s not used at all for serdes, not even in test - so we don’t need the format at all
> 
> ‌
> 
> I checked the lookup usage of this `goalsInfoForDisplay`. Not too bad so I guess we can leave it as a List still. But let’s move both `GoalBasedStatementRawData` and `GoalInfoToDisplay` to impl so that it’s less confusing on usage scope

**Evidence:** anon-2.jsonl:1064 · comment 503067120 · PR 9052 · 2024-05-22

Source path: `report-api/src/main/scala/com/endowus/silver/report/api/commons/statement/package.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1065 — PageDataGenerator: Maybe just use named var here

**Source stance:** suggestion

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/PageDataGenerator.scala; original row 1065.

**Concern stated in the source:** Maybe just use named var here

```
isLastGoalLessCoverPageNeeded = isLastGeneratedPageWithGoalNames && !showDisclaimer
```

Re-assigning same `val isLastGoalLessCoverPageNeeded` as method input parameter can be confusing

**Source-preserving request, proposal, or question:**

> Maybe just use named var here
> 
> ```
> isLastGoalLessCoverPageNeeded = isLastGeneratedPageWithGoalNames && !showDisclaimer
> ```
> 
> Re-assigning same `val isLastGoalLessCoverPageNeeded` as method input parameter can be confusing

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1065 · comment 503065310 · PR 9052 · 2024-05-22

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/PageDataGenerator.scala`

**Evidence:** anon-2.jsonl:1065 · comment 503065310 · PR 9052 · 2024-05-22

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/goalBasedStatement/PageDataGenerator.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1066 — GoalBasedStatementInfoDbDto: Let’s add these fields into the list of data-loss fields in the comment in `GoalBasedStatementPageDataDbDto`, together with explanation, e.g. isDpm ...

**Source stance:** suggestion

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-impl/src/main/scala/com/endowus/silver/report/impl/statement/db/goalBased/model/GoalBasedStatementInfoDbDto.scala; original row 1066.

**Concern stated in the source:** Let’s add these fields into the list of data-loss fields in the comment in `GoalBasedStatementPageDataDbDto`, together with explanation, e.g. isDpm flag is immutable for a goal \+ dpm/non-dpm total are just convenient summary data for display

**Source-preserving request, proposal, or question:**

> Let’s add these fields into the list of data-loss fields in the comment in `GoalBasedStatementPageDataDbDto`, together with explanation, e.g. isDpm flag is immutable for a goal \+ dpm/non-dpm total are just convenient summary data for display

**Conditions and limits:**

- Document intentional data-loss fields: immutable per-goal isDpm and derived DPM/non-DPM display counts.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1066 · comment 503071608 · PR 9052 · 2024-05-22

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/db/goalBased/model/GoalBasedStatementInfoDbDto.scala`

**Evidence:** anon-2.jsonl:1066 · comment 503071608 · PR 9052 · 2024-05-22

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/db/goalBased/model/GoalBasedStatementInfoDbDto.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1067 — StatementPageDataDto: After your change to remove the usage of `totalNumberOfDiscretionaryGoals` inside template, we now can remove this field from the CoverPageData completely ...

**Source stance:** explanation

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-api/src/main/scala/com/endowus/silver/report/api/commons/goalBasedStatement/models/StatementPageDataDto.scala; original row 1067.

**Concern stated in the source:** After your change to remove the usage of `totalNumberOfDiscretionaryGoals` inside template, we now can remove this field from the CoverPageData completely :thumbsup: sorry for many back and forth on this, I added the commit for this :pray:

**Source-preserving request, proposal, or question:**

> After your change to remove the usage of `totalNumberOfDiscretionaryGoals` inside template, we now can remove this field from the CoverPageData completely :thumbsup: sorry for many back and forth on this, I added the commit for this :pray:

**Conditions and limits:**

- Reported final cleanup removes totalNumberOfDiscretionaryGoals from CoverPageData once template stops using it.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1067 · comment 504029426 · PR 9052 · 2024-05-27

Source path: `report-api/src/main/scala/com/endowus/silver/report/api/commons/goalBasedStatement/models/StatementPageDataDto.scala`

**Evidence:** anon-2.jsonl:1067 · comment 504029426 · PR 9052 · 2024-05-27

Source path: `report-api/src/main/scala/com/endowus/silver/report/api/commons/goalBasedStatement/models/StatementPageDataDto.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1071 — InvestmentCommunicationV2EventProcessor: So invalid bank account state \(e.g. 2 bank accounts\) will throw can cause this processor to get stuck here. How do we go about resolvi...

**Source stance:** open-question

**Context:**

> PR 9267 (TT-4231 autofund upcoming recur inv has problem comm), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentCommunicationV2EventProcessor.scala; original row 1071.

**Concern stated in the source:** So invalid bank account state \(e.g. 2 bank accounts\) will throw can cause this processor to get stuck here. How do we go about resolving such data issue?

**Source-preserving request, proposal, or question:**

> So invalid bank account state \(e.g. 2 bank accounts\) will throw can cause this processor to get stuck here. How do we go about resolving such data issue?

**Conditions and limits:**

- Two-bank-account invalid data may throw and stall the processor; recovery remains an open question.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1071 · comment 508959895 · PR 9267 · 2024-06-07

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:1071 · comment 508959895 · PR 9267 · 2024-06-07

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentCommunicationV2EventProcessor.scala`

**Explicit source context (pr_title):**

> TT-4231 autofund upcoming recur inv has problem comm

## A2-1080 — DpmStatusLogic: [person] [person] this kind of validation in logic \+ blind update in entity is actually not safe against race condition / concurrent modification. Specialized c...

**Source stance:** explanation

**Context:**

> PR 9314 ([INV-3127] feat(compliance): Add edge endpoint to query DPM status with cross validation against DPM eligibility in case of EC), compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/DpmStatusLogic.scala; original row 1080.

**Concern stated in the source:** [person] [person] this kind of validation in logic \+ blind update in entity is actually not safe against race condition / concurrent modification. Specialized cmd\+events or proper versioning \(optimistic locking\) can help solve this, but I’ll leave that out as another improvement

**Source-preserving request, proposal, or question:**

> [person] [person] this kind of validation in logic \+ blind update in entity is actually not safe against race condition / concurrent modification. Specialized cmd\+events or proper versioning \(optimistic locking\) can help solve this, but I’ll leave that out as another improvement

**Conditions and limits:**

- Logic-layer validation plus blind entity update is unsafe for concurrent modification; specialized commands/events or optimistic locking are proposed as later improvement.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1080 · comment 508719218 · PR 9314 · 2024-06-06

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/DpmStatusLogic.scala`

> this kind of validation in logic \+ blind update in entity is actually not safe against race condition / concurrent modification. Specialized cmd\+events or proper versioning \(optimistic locking\) can help solve this, but I’ll leave that out as another improvement

**Evidence:** anon-2.jsonl:1080 · comment 508719218 · PR 9314 · 2024-06-06

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/DpmStatusLogic.scala`

**Explicit source context (pr_title):**

> [INV-3127] feat(compliance): Add edge endpoint to query DPM status with cross validation against DPM eligibility in case of EC

## A2-1081 — ReportApplication: Just some notes here, yall are right about the trade-offs but manual start is not that bad, depending on use cases.

**Source stance:** suggestion

**Context:**

> PR 9306 (Feat/EN-3405 use tasktopicsubscriber in report for manual start/stop), report-impl/src/main/scala/com/endowus/silver/report/impl/ReportApplication.scala; original row 1081.

**Concern stated in the source:** Just some notes here, yall are right about the trade-offs but manual start is not that bad, depending on use cases.

In case of report, the svc itself is responsible for triggering of the topic producer side. So we can potentially just call start \(via distributed pubsub\) in the same trigger endpoint, i.e. `createMonthlyStatementsV2` first will trigger start, only then produce the message.

* the start is idempotent so if already started, it won’t cause any harm
* the distributed pubsub is at-most once tho, so it could still happen that maybe one of instance does not start… but I suppose this could be checked easily via logs or metrics.

‌

We can also make this pause/resume status persisted, and check upon startup :thumbsup: 

‌

**Source-preserving request, proposal, or question:**

> Just some notes here, yall are right about the trade-offs but manual start is not that bad, depending on use cases.
> 
> In case of report, the svc itself is responsible for triggering of the topic producer side. So we can potentially just call start \(via distributed pubsub\) in the same trigger endpoint, i.e. `createMonthlyStatementsV2` first will trigger start, only then produce the message.
> 
> * the start is idempotent so if already started, it won’t cause any harm
> * the distributed pubsub is at-most once tho, so it could still happen that maybe one of instance does not start… but I suppose this could be checked easily via logs or metrics.
> 
> ‌
> 
> We can also make this pause/resume status persisted, and check upon startup :thumbsup: 
> 
> ‌

**Conditions and limits:**

- Report may start TaskTopicSubscriber idempotently before producing in createMonthlyStatementsV2. Distributed pubsub is at-most-once and may miss an instance; logs/metrics can detect it. Persisted pause/resume is another option.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1081 · comment 508950934 · PR 9306 · 2024-06-07

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/ReportApplication.scala`

**Evidence:** anon-2.jsonl:1081 · comment 508950934 · PR 9306 · 2024-06-07

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/ReportApplication.scala`

**Explicit source context (pr_title):**

> Feat/EN-3405 use tasktopicsubscriber in report for manual start/stop

## A2-1108 — DetectUpcomingRecurringInvestmentCmdHandler: Remind me how does notification for upcoming-recurring-txn work? It seems we only have amount, without fundingCcy in this event. How...

**Source stance:** open-question

**Context:**

> PR 9091 ([EN-3271] Add autofx recurring support in investment), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/DetectUpcomingRecurringInvestmentCmdHandler.scala; original row 1108.

**Concern stated in the source:** Remind me how does notification for upcoming-recurring-txn work? It seems we only have amount, without fundingCcy in this event. How does it decide if autofx or not?

**Source-preserving request, proposal, or question:**

> Remind me how does notification for upcoming-recurring-txn work? It seems we only have amount, without fundingCcy in this event. How does it decide if autofx or not?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1108 · comment 500269403 · PR 9091 · 2024-05-13

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/DetectUpcomingRecurringInvestmentCmdHandler.scala`

**Evidence:** anon-2.jsonl:1108 · comment 500269403 · PR 9091 · 2024-05-13

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/DetectUpcomingRecurringInvestmentCmdHandler.scala`

**Explicit source context (pr_title):**

> [EN-3271] Add autofx recurring support in investment

## A2-1109 — MakeRecurringInvestmentCmdHandler: We should throw if fxRate is missing for autofx?

**Source stance:** open-question

**Context:**

> PR 9091 ([EN-3271] Add autofx recurring support in investment), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/MakeRecurringInvestmentCmdHandler.scala; original row 1109.

**Concern stated in the source:** We should throw if fxRate is missing for autofx?

**Source-preserving request, proposal, or question:**

> We should throw if fxRate is missing for autofx?

**Conditions and limits:**

- Missing autofx fxRate throwing is a question, not established behavior.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1109 · comment 500232107 · PR 9091 · 2024-05-13

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/MakeRecurringInvestmentCmdHandler.scala`

**Evidence:** anon-2.jsonl:1109 · comment 500232107 · PR 9091 · 2024-05-13

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/MakeRecurringInvestmentCmdHandler.scala`

**Explicit source context (pr_title):**

> [EN-3271] Add autofx recurring support in investment

## A2-1114 — MakeRecurringInvestmentCmdHandler: Need to reply with exception, cannot just throw like this

**Source stance:** explanation

**Context:**

> PR 9091 ([EN-3271] Add autofx recurring support in investment), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/MakeRecurringInvestmentCmdHandler.scala; original row 1114.

**Concern stated in the source:** Need to reply with exception, cannot just throw like this

**Source-preserving request, proposal, or question:**

> Need to reply with exception, cannot just throw like this

**Conditions and limits:**

- Actor command handling needs an exception reply rather than a direct throw.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1114 · comment 501647025 · PR 9091 · 2024-05-17

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/MakeRecurringInvestmentCmdHandler.scala`

**Evidence:** anon-2.jsonl:1114 · comment 501647025 · PR 9091 · 2024-05-17

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/MakeRecurringInvestmentCmdHandler.scala`

**Explicit source context (pr_title):**

> [EN-3271] Add autofx recurring support in investment

## A2-1115 — MakeRecurringInvestmentCmdHandler: It doesn’t matter so let’s relax this and simple ignore indicativeFxRate even if it’s provided? at most let’s just log warn?

**Source stance:** suggestion

**Context:**

> PR 9091 ([EN-3271] Add autofx recurring support in investment), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/MakeRecurringInvestmentCmdHandler.scala; original row 1115.

**Concern stated in the source:** It doesn’t matter so let’s relax this and simple ignore indicativeFxRate even if it’s provided? at most let’s just log warn?

**Source-preserving request, proposal, or question:**

> It doesn’t matter so let’s relax this and simple ignore indicativeFxRate even if it’s provided? at most let’s just log warn?

**Conditions and limits:**

- For an unused indicativeFxRate on this path, ignoring even supplied values with at most warning is proposed.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1115 · comment 501647350 · PR 9091 · 2024-05-17

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/MakeRecurringInvestmentCmdHandler.scala`

**Evidence:** anon-2.jsonl:1115 · comment 501647350 · PR 9091 · 2024-05-17

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/MakeRecurringInvestmentCmdHandler.scala`

**Explicit source context (pr_title):**

> [EN-3271] Add autofx recurring support in investment

## A2-1119 — MakeRecurringInvestmentCmdHandler: Should this use `resolvedFundingInstructions` too?

**Source stance:** open-question

**Context:**

> PR 9091 ([EN-3271] Add autofx recurring support in investment), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/MakeRecurringInvestmentCmdHandler.scala; original row 1119.

**Concern stated in the source:** Should this use `resolvedFundingInstructions` too?

**Source-preserving request, proposal, or question:**

> Should this use `resolvedFundingInstructions` too?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1119 · comment 505583000 · PR 9091 · 2024-05-29

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/MakeRecurringInvestmentCmdHandler.scala`

**Evidence:** anon-2.jsonl:1119 · comment 505583000 · PR 9091 · 2024-05-29

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/MakeRecurringInvestmentCmdHandler.scala`

**Explicit source context (pr_title):**

> [EN-3271] Add autofx recurring support in investment

## A2-1122 — RecurringInvestmentProcessor: This one is just used for tradability \+ compliance check. We don’t pass this amount to cmd, only the fxRate

**Source stance:** explanation

**Context:**

> PR 9091 ([EN-3271] Add autofx recurring support in investment), investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala; original row 1122.

**Concern stated in the source:** This one is just used for tradability \+ compliance check. We don’t pass this amount to cmd, only the fxRate

**Source-preserving request, proposal, or question:**

> This one is just used for tradability \+ compliance check. We don’t pass this amount to cmd, only the fxRate

**Conditions and limits:**

- This adjusted amount is only for tradability/compliance checks; command receives fxRate, not amount.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1122 · comment 505668648 · PR 9091 · 2024-05-29

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Evidence:** anon-2.jsonl:1122 · comment 505668648 · PR 9091 · 2024-05-29

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/schedulers/RecurringInvestmentProcessor.scala`

**Explicit source context (pr_title):**

> [EN-3271] Add autofx recurring support in investment

## A2-1125 — DetectUpcomingRecurringInvestmentCmdHandler: Then we don’t need `indicativeFxRate` in this detect cmd either

**Source stance:** suggestion

**Context:**

> PR 9102 ([EN-3248] Autofx upcoming recurring comms), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/DetectUpcomingRecurringInvestmentCmdHandler.scala; original row 1125.

**Source-preserving request, proposal, or question:**

> Then we don’t need `indicativeFxRate` in this detect cmd either

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1125 · comment 500279433 · PR 9102 · 2024-05-13

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/DetectUpcomingRecurringInvestmentCmdHandler.scala`

**Evidence:** anon-2.jsonl:1125 · comment 500279433 · PR 9102 · 2024-05-13

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/DetectUpcomingRecurringInvestmentCmdHandler.scala`

**Explicit source context (hunk):**

> +        scheduledInvestmentAmount = recurringSchedule.investmentAmount,
> +        fundingInstructions = recurringSchedule.fundingInstructions
>        )
>        Effect.persist(evt).thenAck(cmd.replyTo)
>      }

**Evidence:** anon-2.jsonl:1125 · comment 500279433 · PR 9102 · 2024-05-13

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/DetectUpcomingRecurringInvestmentCmdHandler.scala`

**Explicit source context (pr_title):**

> [EN-3248] Autofx upcoming recurring comms

## A2-1126 — DetectUpcomingRecurringInvestmentCmdHandler: Does this amount needs to be “correct” amount here? Maybe just make it as deprecated, and only use if old events

**Source stance:** suggestion

**Context:**

> PR 9102 ([EN-3248] Autofx upcoming recurring comms), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/DetectUpcomingRecurringInvestmentCmdHandler.scala; original row 1126.

**Concern stated in the source:** Does this amount needs to be “correct” amount here? Maybe just make it as deprecated, and only use if old events

```
case class UpcomingRecurringTransactionDetectedEvt(
  ...
  @deprecated scheduledInvestmentAmount: BigDecimal,
  fundingInstructions: Option[PlanFundingInstructions]
) {

  def resolvedScheduledInvestmentAmount: BigDecimal = {
    fundingInstructions match {
      case Some(specifiedAccount) => ...
      case Some(planAccount) => ...
      case None => scheduledInvestmentAmount
    }
  }

}
```

‌

**Source-preserving request, proposal, or question:**

> Does this amount needs to be “correct” amount here? Maybe just make it as deprecated, and only use if old events
> 
> ```
> case class UpcomingRecurringTransactionDetectedEvt(
>   ...
>   @deprecated scheduledInvestmentAmount: BigDecimal,
>   fundingInstructions: Option[PlanFundingInstructions]
> ) {
> 
>   def resolvedScheduledInvestmentAmount: BigDecimal = {
>     fundingInstructions match {
>       case Some(specifiedAccount) => ...
>       case Some(planAccount) => ...
>       case None => scheduledInvestmentAmount
>     }
>   }
> 
> }
> ```
> 
> ‌

**Conditions and limits:**

- FundingInstructions is optional for old events; deprecated scheduledInvestmentAmount is fallback only when absent. New variants should derive currency-correct amount.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1126 · comment 500278057 · PR 9102 · 2024-05-13

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/DetectUpcomingRecurringInvestmentCmdHandler.scala`

**Evidence:** anon-2.jsonl:1126 · comment 500278057 · PR 9102 · 2024-05-13

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/DetectUpcomingRecurringInvestmentCmdHandler.scala`

**Explicit source context (pr_title):**

> [EN-3248] Autofx upcoming recurring comms

## A2-1162 — SuggestAllocationTargetUpdateCmdHandler: Are we sure this is what we want for Factors in SG? Cuz it’s still Advisory there currently? Let’s check w PM?

**Source stance:** open-question

**Context:**

> PR 9167 (Feat/INV-2796 auto accept dpc), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/SuggestAllocationTargetUpdateCmdHandler.scala; original row 1162.

**Concern stated in the source:** Are we sure this is what we want for Factors in SG? Cuz it’s still Advisory there currently? Let’s check w PM?

**Source-preserving request, proposal, or question:**

> Are we sure this is what we want for Factors in SG? Cuz it’s still Advisory there currently? Let’s check w PM?

**Conditions and limits:**

- SG Factors is still Advisory at that time; desired automatic DPC acceptance needs PM confirmation.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1162 · comment 501684084 · PR 9167 · 2024-05-17

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/SuggestAllocationTargetUpdateCmdHandler.scala`

**Evidence:** anon-2.jsonl:1162 · comment 501684084 · PR 9167 · 2024-05-17

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/SuggestAllocationTargetUpdateCmdHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-2796 auto accept dpc

## A2-1173 — ChargeApplication: Shouldn’t have any issue to spawn a simple actor, but yeah if that throws, it will block init of everything else, and cause the HttpServerStartUp onMemberUp t...

**Source stance:** explanation

**Context:**

> PR 9178 ([INV-3074] Manual start/stop for TaskTopicSubscriber), charge-impl/src/main/scala/com/endowus/silver/charge/impl/ChargeApplication.scala; original row 1173.

**Concern stated in the source:** Shouldn’t have any issue to spawn a simple actor, but yeah if that throws, it will block init of everything else, and cause the HttpServerStartUp onMemberUp to fail

**Source-preserving request, proposal, or question:**

> Shouldn’t have any issue to spawn a simple actor, but yeah if that throws, it will block init of everything else, and cause the HttpServerStartUp onMemberUp to fail

**Conditions and limits:**

- Spawning failure can block subsequent initialization and HttpServerStartUp onMemberUp.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1173 · comment 502172495 · PR 9178 · 2024-05-20

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/ChargeApplication.scala`

**Evidence:** anon-2.jsonl:1173 · comment 502172495 · PR 9178 · 2024-05-20

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/ChargeApplication.scala`

**Explicit source context (pr_title):**

> [INV-3074] Manual start/stop for TaskTopicSubscriber

## A2-1175 — ClusterStartup: So I guess the only reason for `ClusterStartup` to own the termination bit is because `onMemberUp` itself might not have access to the actorSystem

**Source stance:** open-question

**Context:**

> PR 9179 ([DYNAMIC-1046] feat(advisory): Add scaladoc for ClusterStartup. Change to single critical onMemberUp action for default apply method), akka-silver-commons/src/main/scala/com/endowus/silver/commons/startup/ClusterStartup.scala; original row 1175.

**Concern stated in the source:** So I guess the only reason for `ClusterStartup` to own the termination bit is because `onMemberUp` itself might not have access to the actorSystem

**Source-preserving request, proposal, or question:**

> So I guess the only reason for `ClusterStartup` to own the termination bit is because `onMemberUp` itself might not have access to the actorSystem

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1175 · comment 501614646 · PR 9179 · 2024-05-17

Source path: `akka-silver-commons/src/main/scala/com/endowus/silver/commons/startup/ClusterStartup.scala`

**Evidence:** anon-2.jsonl:1175 · comment 501614646 · PR 9179 · 2024-05-17

Source path: `akka-silver-commons/src/main/scala/com/endowus/silver/commons/startup/ClusterStartup.scala`

**Explicit source context (pr_title):**

> [DYNAMIC-1046] feat(advisory): Add scaladoc for ClusterStartup. Change to single critical onMemberUp action for default apply method

## A2-1191 — EmailDataFactory: Let’s just return for planCcy? A bit weird to see None here \(I know it’s existing code\)

**Source stance:** suggestion

**Context:**

> PR 9153 (TT-4228 Autofund one time investment and alts investment setup comms), investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala; original row 1191.

**Concern stated in the source:** Let’s just return for planCcy? A bit weird to see None here \(I know it’s existing code\)

**Source-preserving request, proposal, or question:**

> Let’s just return for planCcy? A bit weird to see None here \(I know it’s existing code\)

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1191 · comment 502188775 · PR 9153 · 2024-05-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala`

**Evidence:** anon-2.jsonl:1191 · comment 502188775 · PR 9153 · 2024-05-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala`

**Explicit source context (pr_title):**

> TT-4228 Autofund one time investment and alts investment setup comms

## A2-1192 — EmailDataFactory: Is this flag a bit confusing for CPF/SRS?

**Source stance:** open-question

**Context:**

> PR 9153 (TT-4228 Autofund one time investment and alts investment setup comms), investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala; original row 1192.

**Source-preserving request, proposal, or question:**

> Is this flag a bit confusing for CPF/SRS?

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1192 · comment 502188827 · PR 9153 · 2024-05-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala`

**Evidence:** anon-2.jsonl:1192 · comment 502188827 · PR 9153 · 2024-05-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala`

**Explicit source context (hunk):**

>      OneTimeInvestmentCreatedData(
>        VIRTUAL_ACCOUNT_NUMBER = virtualAccountNumber,
>        ACCOUNT_TYPE = tradingAccountType.toString,
>        ACCOUNT_NAME = TradingAccountType.tradingAccountToUserFriendlyNameMap(tradingAccountType),
>        GOAL_NAME = goalName,
> -      CURRENCY_CODE = CurrencyUtils.getCurrencySymbol(investmentRequestCcy),
> -      CURRENCY_UNIT = investmentRequestCcy.toString,

**Evidence:** anon-2.jsonl:1192 · comment 502188827 · PR 9153 · 2024-05-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala`

**Explicit source context (pr_title):**

> TT-4228 Autofund one time investment and alts investment setup comms

## A2-1193 — EmailDataFactory: It seems this piece of code didnt exist for Alts flow before, because we assumed autofx is not applicable for Alts.

**Source stance:** suggestion

**Context:**

> PR 9153 (TT-4228 Autofund one time investment and alts investment setup comms), investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala; original row 1193.

**Concern stated in the source:** It seems this piece of code didnt exist for Alts flow before, because we assumed autofx is not applicable for Alts.

However, I see this code is generic enough we can extract into another helper \(returning a case class\) and reuse for both places.

**Source-preserving request, proposal, or question:**

> It seems this piece of code didnt exist for Alts flow before, because we assumed autofx is not applicable for Alts.
> 
> However, I see this code is generic enough we can extract into another helper \(returning a case class\) and reuse for both places.

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1193 · comment 502189642 · PR 9153 · 2024-05-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala`

**Evidence:** anon-2.jsonl:1193 · comment 502189642 · PR 9153 · 2024-05-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala`

**Explicit source context (pr_title):**

> TT-4228 Autofund one time investment and alts investment setup comms

## A2-1196 — EmailDataFactory: Should we change these fields to use data from `fiDetails`?

**Source stance:** open-question

**Context:**

> PR 9153 (TT-4228 Autofund one time investment and alts investment setup comms), investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala; original row 1196.

**Source-preserving request, proposal, or question:**

> Should we change these fields to use data from `fiDetails`?
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1196 · comment 502297417 · PR 9153 · 2024-05-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala`

**Evidence:** anon-2.jsonl:1196 · comment 502297417 · PR 9153 · 2024-05-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala`

**Explicit source context (pr_title):**

> TT-4228 Autofund one time investment and alts investment setup comms

## A2-1204 — HttpServerStartup: Should we make `route` and `rejectionHandler` available in the base Endpoints? Then we provide overloading constructors, so service doesn’t need to think too ...

**Source stance:** suggestion

**Context:**

> PR 9049 (DYNAMIC-1046: Terminate service if onMemberUp fails (ready for review)), akka-http-commons/src/main/scala/com/endowus/silver/server/akka/http/HttpServerStartup.scala; original row 1204.

**Concern stated in the source:** Should we make `route` and `rejectionHandler` available in the base Endpoints? Then we provide overloading constructors, so service doesn’t need to think too much if their use case is standard, but still have an easy way to give additional routes if needed \(e.g. OpenApi route\)

```
class HttpServerStartup private(actorSystem: ActorSystem[_], endpoints: BaseEndpointResultCompat, routes: Route) {
  implicit val executionContext: ExecutionContext = actorSystem.executionContext
  implicit val rejectionHandler: RejectionHandler = endpoints.rejectionHandler
  
  def start(): Future[Unit] = {
    ...
  }
}

object HttpServerStartup {
  def apply(actorSystem: ActorSystem[_], endpoints: BaseEndpointResultCompat, additionalRoutes: Route*): HttpServerStartup = {
    val routes = ... // concat endpoints.routes and additionalRoutes
    new HttpServerStartup(actorSystem, endpoints, routes)
  }
}
```

‌

**Source-preserving request, proposal, or question:**

> Should we make `route` and `rejectionHandler` available in the base Endpoints? Then we provide overloading constructors, so service doesn’t need to think too much if their use case is standard, but still have an easy way to give additional routes if needed \(e.g. OpenApi route\)
> 
> ```
> class HttpServerStartup private(actorSystem: ActorSystem[_], endpoints: BaseEndpointResultCompat, routes: Route) {
>   implicit val executionContext: ExecutionContext = actorSystem.executionContext
>   implicit val rejectionHandler: RejectionHandler = endpoints.rejectionHandler
>   
>   def start(): Future[Unit] = {
>     ...
>   }
> }
> 
> object HttpServerStartup {
>   def apply(actorSystem: ActorSystem[_], endpoints: BaseEndpointResultCompat, additionalRoutes: Route*): HttpServerStartup = {
>     val routes = ... // concat endpoints.routes and additionalRoutes
>     new HttpServerStartup(actorSystem, endpoints, routes)
>   }
> }
> ```
> 
> ‌

**Conditions and limits:**

- Base endpoints can expose routes/rejectionHandler and constructors add extra routes such as OpenApi; this is proposed API design.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1204 · comment 499728704 · PR 9049 · 2024-05-10

Source path: `akka-http-commons/src/main/scala/com/endowus/silver/server/akka/http/HttpServerStartup.scala`

**Evidence:** anon-2.jsonl:1204 · comment 499728704 · PR 9049 · 2024-05-10

Source path: `akka-http-commons/src/main/scala/com/endowus/silver/server/akka/http/HttpServerStartup.scala`

**Explicit source context (pr_title):**

> DYNAMIC-1046: Terminate service if onMemberUp fails (ready for review)

## A2-1205 — Startup: How about we decouple cluster startup from onMemberUp callback \(potentially can provide 0 or more than 1 callbacks\)

**Source stance:** suggestion

**Context:**

> PR 9049 (DYNAMIC-1046: Terminate service if onMemberUp fails (ready for review)), akka-silver-commons/src/main/scala/com/endowus/silver/commons/startup/Startup.scala; original row 1205.

**Concern stated in the source:** How about we decouple cluster startup from onMemberUp callback \(potentially can provide 0 or more than 1 callbacks\)

We can follow akka Cluster approach, essentially just wrap it with additional akka management etc. and handle error in callback to terminate system

```
class AkkaClusterStartup(system: ActorSystem[_]) {
  AkkaManagement(system).start()
  AppConfigExtension(system.classicSystem).start()
  ClusterBootstrap(system).start()

  private val cluster = Cluster(system)

  def registerOnMemberUp[T](onMemberUp: => T): Unit = {
    cluster.registerOnMemberUp {
      Try(onMemberUp).recover {
        case e: Exception =>
          logger.error(s"System ${system.name} terminating, akka cluster registered OnMemberUp failed: ${e.getMessage}", e)
          system.terminate()
      }
    }
  }
}

object AkkaClusterStartup {

  def apply(system: ActorSystem[_], onMemberUpCallbacks: (=> Unit)*): AkkaClusterStartup = {
    val clusterStartup = new AkkaClusterStartup(system)
    onMemberUpCallbacks.foreach(cluster.registerOnMemberUp)
    clusterStartup
  }

}
```

‌

**Source-preserving request, proposal, or question:**

> How about we decouple cluster startup from onMemberUp callback \(potentially can provide 0 or more than 1 callbacks\)
> 
> We can follow akka Cluster approach, essentially just wrap it with additional akka management etc. and handle error in callback to terminate system
> 
> ```
> class AkkaClusterStartup(system: ActorSystem[_]) {
>   AkkaManagement(system).start()
>   AppConfigExtension(system.classicSystem).start()
>   ClusterBootstrap(system).start()
> 
>   private val cluster = Cluster(system)
> 
>   def registerOnMemberUp[T](onMemberUp: => T): Unit = {
>     cluster.registerOnMemberUp {
>       Try(onMemberUp).recover {
>         case e: Exception =>
>           logger.error(s"System ${system.name} terminating, akka cluster registered OnMemberUp failed: ${e.getMessage}", e)
>           system.terminate()
>       }
>     }
>   }
> }
> 
> object AkkaClusterStartup {
> 
>   def apply(system: ActorSystem[_], onMemberUpCallbacks: (=> Unit)*): AkkaClusterStartup = {
>     val clusterStartup = new AkkaClusterStartup(system)
>     onMemberUpCallbacks.foreach(cluster.registerOnMemberUp)
>     clusterStartup
>   }
> 
> }
> ```
> 
> ‌

**Conditions and limits:**

- Proposed decoupled AkkaClusterStartup supports zero/multiple onMemberUp callbacks and terminates system on callback exception. Reproduce illustrative source without claiming the snippet compiles unchanged.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1205 · comment 499730341 · PR 9049 · 2024-05-10

Source path: `akka-silver-commons/src/main/scala/com/endowus/silver/commons/startup/Startup.scala`

**Evidence:** anon-2.jsonl:1205 · comment 499730341 · PR 9049 · 2024-05-10

Source path: `akka-silver-commons/src/main/scala/com/endowus/silver/commons/startup/Startup.scala`

**Explicit source context (pr_title):**

> DYNAMIC-1046: Terminate service if onMemberUp fails (ready for review)

## A2-1234 — InvestmentRequestTopicSubscriberV3: Should we also use `UpdateFundingInstructionsCmd` here?

**Source stance:** open-question

**Context:**

> PR 8959 (TT-4222 pass retry date time to investment and transaction svc), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala; original row 1234.

**Source-preserving request, proposal, or question:**

> Should we also use `UpdateFundingInstructionsCmd` here?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1234 · comment 499195387 · PR 8959 · 2024-05-08

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1234 · comment 499195387 · PR 8959 · 2024-05-08

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> TT-4222 pass retry date time to investment and transaction svc

## A2-1236 — InvestmentRequestTopicSubscriberV3: Looks like we need separate cmd to update fxConversionRequestId / deposit transactionId without changing status?

**Source stance:** open-question

**Context:**

> PR 8923 (TT-4220 pass deposit tx id to investment and transaction), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala; original row 1236.

**Concern stated in the source:** Looks like we need separate cmd to update fxConversionRequestId / deposit transactionId without changing status?

Maybe make it a bit more generic to update `FundingInstructions` instead?

**Source-preserving request, proposal, or question:**

> Looks like we need separate cmd to update fxConversionRequestId / deposit transactionId without changing status?
> 
> Maybe make it a bit more generic to update `FundingInstructions` instead?

**Conditions and limits:**

- Separate funding-instructions update command should change fxConversionRequestId/depositTransactionId without changing status.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1236 · comment 498410939 · PR 8923 · 2024-05-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1236 · comment 498410939 · PR 8923 · 2024-05-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> TT-4220 pass deposit tx id to investment and transaction

## A2-1244 — BrokerCashTransactionTopicSubscriberV3: What will happen to normal deposit? They will flow straight from broker → transaction, without any records in TradingAccountEntity right?...

**Source stance:** open-question

**Context:**

> PR 8998 (TT-4221 add depositDetails in transaction), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/BrokerCashTransactionTopicSubscriberV3.scala; original row 1244.

**Concern stated in the source:** What will happen to normal deposit? They will flow straight from broker → transaction, without any records in TradingAccountEntity right? So this cmd won’t work?

**Source-preserving request, proposal, or question:**

> What will happen to normal deposit? They will flow straight from broker → transaction, without any records in TradingAccountEntity right? So this cmd won’t work?

**Conditions and limits:**

- Normal broker→transaction deposit lacks TradingAccountEntity records, so applicability of the command is unresolved.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1244 · comment 498392655 · PR 8998 · 2024-05-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/BrokerCashTransactionTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1244 · comment 498392655 · PR 8998 · 2024-05-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/BrokerCashTransactionTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> TT-4221 add depositDetails in transaction

## A2-1248 — TransactionTypes: Same here. Individual transaction should be serdes via the sealed trait `Transaction` by default. You can ref this inside the object so that we ensure it’s onl...

**Source stance:** suggestion

**Context:**

> PR 8998 (TT-4221 add depositDetails in transaction), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/TransactionTypes.scala; original row 1248.

**Concern stated in the source:** Same here. Individual transaction should be serdes via the sealed trait `Transaction` by default. You can ref this inside the object so that we ensure it’s only used there

```
object UpdateDepositTransactionCmd {
  implicit private val depositTransaction: Format[DepositTransaction] = DepositTransaction.format
  implicit def format(implicit system: ActorSystem[_]): Format[UpdateDepositTransactionCmd] = Json.format
}
```

‌

**Source-preserving request, proposal, or question:**

> Same here. Individual transaction should be serdes via the sealed trait `Transaction` by default. You can ref this inside the object so that we ensure it’s only used there
> 
> ```
> object UpdateDepositTransactionCmd {
>   implicit private val depositTransaction: Format[DepositTransaction] = DepositTransaction.format
>   implicit def format(implicit system: ActorSystem[_]): Format[UpdateDepositTransactionCmd] = Json.format
> }
> ```
> 
> ‌

**Conditions and limits:**

- Transactions normally serialize through sealed Transaction; DepositTransaction format should be private local implicit inside UpdateDepositTransactionCmd.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1248 · comment 499180515 · PR 8998 · 2024-05-08

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/TransactionTypes.scala`

**Evidence:** anon-2.jsonl:1248 · comment 499180515 · PR 8998 · 2024-05-08

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/TransactionTypes.scala`

**Explicit source context (pr_title):**

> TT-4221 add depositDetails in transaction

## A2-1249 — TransactionV3Entity: I think it’s safer to assume we only want to copy over tradeDetails from existing to new value, than to assume we only need to take new statusDetails only f...

**Source stance:** suggestion

**Context:**

> PR 8998 (TT-4221 add depositDetails in transaction), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/TransactionV3Entity.scala; original row 1249.

**Concern stated in the source:** I think it’s safer to assume we only want to copy over tradeDetails from existing to new value, than to assume we only need to take new statusDetails only from new value.  
  
How about we keep this logic just simple as below, no need to think about various status sequences. After all, it’s still an upsert cmd

```
val updatedTransaction = cmd.depositTransaction.copy(
  tradeDetails = cmd.depositTransaction.tradeDetails.orElse(existingTx.tradeDetails)
)
Effect.persist(TransactionUpdatedEvt(updatedTransaction)).thenAck(cmd.replyTo)
```

‌

**Source-preserving request, proposal, or question:**

> I think it’s safer to assume we only want to copy over tradeDetails from existing to new value, than to assume we only need to take new statusDetails only from new value.  
>   
> How about we keep this logic just simple as below, no need to think about various status sequences. After all, it’s still an upsert cmd
> 
> ```
> val updatedTransaction = cmd.depositTransaction.copy(
>   tradeDetails = cmd.depositTransaction.tradeDetails.orElse(existingTx.tradeDetails)
> )
> Effect.persist(TransactionUpdatedEvt(updatedTransaction)).thenAck(cmd.replyTo)
> ```
> 
> ‌

**Conditions and limits:**

- Upsert takes the complete new depositTransaction and only preserves existing tradeDetails when new tradeDetails are absent; avoid reconstructing all fields from status-order assumptions.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1249 · comment 499184615 · PR 8998 · 2024-05-08

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/TransactionV3Entity.scala`

**Evidence:** anon-2.jsonl:1249 · comment 499184615 · PR 8998 · 2024-05-08

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/TransactionV3Entity.scala`

**Explicit source context (pr_title):**

> TT-4221 add depositDetails in transaction

## A2-1257 — HkGoalCreatePortfolioSummaryBehaviour: Shouldn’t this be calculated from `request.riskTolerance` instead? Also should we refactor and use the `ProductLineAndIntentHelper` ? Then...

**Source stance:** open-question

**Context:**

> PR 8933 (Feat/INV-2808/flagship dpm goal create endpoints), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/hk/HkGoalCreatePortfolioSummaryBehaviour.scala; original row 1257.

**Concern stated in the source:** Shouldn’t this be calculated from `request.riskTolerance` instead? Also should we refactor and use the `ProductLineAndIntentHelper` ? Then once productlineAndIntent is provided, we can refactor again to make this common between flapshipDpm and fundSmart too

**Source-preserving request, proposal, or question:**

> Shouldn’t this be calculated from `request.riskTolerance` instead? Also should we refactor and use the `ProductLineAndIntentHelper` ? Then once productlineAndIntent is provided, we can refactor again to make this common between flapshipDpm and fundSmart too

**Conditions and limits:**

- riskTolerance-based resolution and ProductLineAndIntentHelper reuse are proposed; a later productlineAndIntent refactor can unify FlagshipDpm/FundSmart.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1257 · comment 494559514 · PR 8933 · 2024-04-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/hk/HkGoalCreatePortfolioSummaryBehaviour.scala`

**Evidence:** anon-2.jsonl:1257 · comment 494559514 · PR 8933 · 2024-04-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/hk/HkGoalCreatePortfolioSummaryBehaviour.scala`

**Explicit source context (pr_title):**

> Feat/INV-2808/flagship dpm goal create endpoints

## A2-1306 — CustomerStateUpdatedLogic: Maybe make them follow same style right?

**Source stance:** suggestion

**Context:**

> PR 9039 (Feat/INV-3007 react to cra downgrade dpm), compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/CustomerStateUpdatedLogic.scala; original row 1306.

**Concern stated in the source:** Maybe make them follow same style right?

either

```
case CraValidationOutput.CraCat3 =>
  Future.successful(true)
case CraValidationOutput.CraCat2 if isGoalDiscretionary(goal) =>
  Future.successful(true)
case CraValidationOutput.CraCat2 if allocationHelper.isComplexPortfolio(targetAllocation) =>
  Future.successful(true)
case _ =>
  Future.successful(false)
```

or

```
case CraValidationOutput.CraCat3 =>
  Future.successful(true)
case CraValidationOutput.CraCat2 =>
  Future.successful(isGoalDiscretionary(goal) || allocationHelper.isComplexPortfolio(targetAllocation))
case _ =>
  Future.successful(false)
```

‌

**Source-preserving request, proposal, or question:**

> Maybe make them follow same style right?
> 
> either
> 
> ```
> case CraValidationOutput.CraCat3 =>
>   Future.successful(true)
> case CraValidationOutput.CraCat2 if isGoalDiscretionary(goal) =>
>   Future.successful(true)
> case CraValidationOutput.CraCat2 if allocationHelper.isComplexPortfolio(targetAllocation) =>
>   Future.successful(true)
> case _ =>
>   Future.successful(false)
> ```
> 
> or
> 
> ```
> case CraValidationOutput.CraCat3 =>
>   Future.successful(true)
> case CraValidationOutput.CraCat2 =>
>   Future.successful(isGoalDiscretionary(goal) || allocationHelper.isComplexPortfolio(targetAllocation))
> case _ =>
>   Future.successful(false)
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1306 · comment 498417714 · PR 9039 · 2024-05-06

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/CustomerStateUpdatedLogic.scala`

**Evidence:** anon-2.jsonl:1306 · comment 498417714 · PR 9039 · 2024-05-06

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/CustomerStateUpdatedLogic.scala`

**Explicit source context (pr_title):**

> Feat/INV-3007 react to cra downgrade dpm

## A2-1307 — Wrongly deleted fee-redemption recovery: first order stays deleted, second assumption restores, confirmations complete

**Source stance:** reported-verification

**Context:**

> PR 9060 ([INV-3021] fix(charge)(redemption)(transaction): Recover wrongly deleted fee redemption trade. To revert after data is fixed), no inline path; original row 1307.

**Source-preserving request, proposal, or question:**

> ## Test setup
> 
> Trading: `SUBMITTED_EXTERNALLY`
> 
> ‌
> 
> Redemption: `TRADE_SUBMITTED_EXTERNALLY_PENDING_SETTLEMENT`
> 
> ‌
> 
> Charge: `WITHDRAWAL_IN_PROGRESS`
> 
> ‌
> 
> Transaction: `SUBMITTED_EXTERNALLY_AND_PENDING_SETTLEMENT`
> 
> ‌
> 
> ## Reproduce
> 
> ‌
> 
> Trading: `DELETED`
> 
> ‌
> 
> Redemption: `DELETED` with `deletedAt`
> 
> ‌
> 
> Charge: `DELETED`
> 
> ‌
> 
> Transaction: `DELETED`
> 
> ‌
> 
> ## Assume first order
> 
> ‌
> 
> Trading: still `DELETED`. One order has `settlementAssumption` without deletedAt
> 
> ‌
> 
> Redemption: still `DELETED` with `deletedAt`. One order has settlement assumed details without `deletedAt`
> 
> ‌
> 
> Transaction now skip the invalid `RedemptionRequestOrderSettlementAssumedMsg` message instead getting stuck
> 
> ![](<url>
> ‌
> 
> ## Assume second order
> 
> ‌
> 
> Trading: recover to `SETTLEMENT_ASSUMED_WAITING_FOR_CONFIRMATION`
> 
> ‌
> 
> Redemption: recover to `TRADE_SETTLEMENT_ASSUMED_PENDING_CONFIRMATION` without `deletedAt`
> 
> ‌
> 
> Transaction: recover to `SETTLEMENT_ASSUMED_AND_PENDING_FINAL_CONFIRMATION` without `deletedAt`
> 
> ‌
> 
> ## Confirm both orders
> 
> Trading: successfully reach `COMPLETED` with updated `finalStatusConfirmedAt`, and without `deletedAt`
> 
> ‌
> 
> Redemption: successfully reach `COMPLETED` with `completedAt`
> 
> ‌
> 
> Charge: successfully reach `FEE_CHARGE_COMPLETED`
> 
> ‌
> 
> Transaction: successfully reach `SETTLEMENT_CONFIRMED`
> 
> ‌

**Conditions and limits:**

- Reported staged test only; do not generalize this temporary recovery PR into a permanent production workflow. Large repeated state JSON was inspected selectively for statuses, amount/order split and recovery fields; incidental IDs/accounts/timestamps are excluded.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ## Test setup
> 
> Trading: `SUBMITTED_EXTERNALLY`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Redemption: `TRADE_SUBMITTED_EXTERNALLY_PENDING_SETTLEMENT`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Charge: `WITHDRAWAL_IN_PROGRESS`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Transaction: `SUBMITTED_EXTERNALLY_AND_PENDING_SETTLEMENT`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> ## Reproduce

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Trading: `DELETED`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Redemption: `DELETED` with `deletedAt`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Charge: `DELETED`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Transaction: `DELETED`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> ## Assume first order

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Trading: still `DELETED`. One order has `settlementAssumption` without deletedAt

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Redemption: still `DELETED` with `deletedAt`. One order has settlement assumed details without `deletedAt`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Transaction now skip the invalid `RedemptionRequestOrderSettlementAssumedMsg` message instead getting stuck
> 
> ![](<url>
> ‌
> 
> ## Assume second order

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Trading: recover to `SETTLEMENT_ASSUMED_WAITING_FOR_CONFIRMATION`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Redemption: recover to `TRADE_SETTLEMENT_ASSUMED_PENDING_CONFIRMATION` without `deletedAt`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Transaction: recover to `SETTLEMENT_ASSUMED_AND_PENDING_FINAL_CONFIRMATION` without `deletedAt`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> ## Confirm both orders
> 
> Trading: successfully reach `COMPLETED` with updated `finalStatusConfirmedAt`, and without `deletedAt`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Redemption: successfully reach `COMPLETED` with `completedAt`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Charge: successfully reach `FEE_CHARGE_COMPLETED`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌
> 
> Transaction: successfully reach `SETTLEMENT_CONFIRMED`

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> ‌

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> "forceDelete": true

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> "forceSettle": true

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> "requestedAmount": 13.19

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> "requestedAmount": 6.59

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

> "requestedAmount": 6.6

**Evidence:** anon-2.jsonl:1307 · comment 497938405 · PR 9060 · 2024-05-03

**Explicit source context (pr_title):**

> [INV-3021] fix(charge)(redemption)(transaction): Recover wrongly deleted fee redemption trade. To revert after data is fixed

## A2-1310 — D56 abort rejected withdrawal dividend: 187.44 switches to cash balance; 12.56 reinvestment remains unchanged

**Source stance:** reported-verification

**Context:**

> PR 9037 ([INV-3016] feat(dividend)(timeseries)(transaction): Support aborting dividend stuck in WithdrawalRequested), no inline path; original row 1310.

**Source-preserving request, proposal, or question:**

> Tested in d56
> 
> ‌
> 
> Setup dividend \+ rejected withdrawal
> 
> * withdrawal with amount 187.44 is rejected
> * dividend has distribution withdrawal pref, amount = 187.44, stuck in Processing
> * another dividend with same distribution has distribution reinvested pref, amount = 12.56, in Processing \(not affected\)
> 
> ![](<url>
> dividend svc logs error as expected when received `WithdrawalRequestRejectedMsg` from trading svc
> 
> ‌
> 
> Trigger abort endpoint
> 
> Results:
> 
> * withdrawal with amount 187.44 is still rejected \(in tact\)
> * previously stuck dividend now has distribution cash balance pref, amount = 187.44, and is completed
> * the other dividend with same distribution is not affected
> 
> ![](<url>
> timeseries svc processes the new event and update distribution pref correctly
> 
> ‌
> 
> Inspection reports DividendWithdrawalRequestAbortedEvt with overridingDistributionPreference=DistributeCashBalance, and final Distributed state.

**Conditions and limits:**

- Reported D56 test affects only 187.44 withdrawal dividend; 12.56 reinvestment dividend in same distribution is a negative/control case. Incidental entity/account identifiers omitted.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

> Tested in d56
> 
> ‌
> 
> Setup dividend \+ rejected withdrawal
> 
> * withdrawal with amount 187.44 is rejected
> * dividend has distribution withdrawal pref, amount = 187.44, stuck in Processing
> * another dividend with same distribution has distribution reinvested pref, amount = 12.56, in Processing \(not affected\)
> 
> ![](<url>
> dividend svc logs error as expected when received `WithdrawalRequestRejectedMsg` from trading svc
> 
> ‌
> 
> Trigger abort endpoint

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

> Results:
> 
> * withdrawal with amount 187.44 is still rejected \(in tact\)
> * previously stuck dividend now has distribution cash balance pref, amount = 187.44, and is completed
> * the other dividend with same distribution is not affected
> 
> ![](<url>
> timeseries svc processes the new event and update distribution pref correctly
> 
> ‌

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

> "eventName": "DividendWithdrawalRequestAbortedEvt"

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

> "overridingDistributionPreference": "DistributeCashBalance"

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

> "distributionPreference": "DistributeCashBalance"

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

> "_type": "com.endowus.silver.dividend.impl.entities.dividend.ces.Distributed"

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

**Explicit source context (pr_title):**

> [INV-3016] feat(dividend)(timeseries)(transaction): Support aborting dividend stuck in WithdrawalRequested

## A2-1311 — DividendTopicSubscriberV3: Added comment for the AbortCmd… from transaction pov, it doesnt need to know about the possible cases of pref here. In future, we might support for ca...

**Source stance:** explanation

**Context:**

> PR 9037 ([INV-3016] feat(dividend)(timeseries)(transaction): Support aborting dividend stuck in WithdrawalRequested), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala; original row 1311.

**Concern stated in the source:** Added comment for the AbortCmd… from transaction pov, it doesnt need to know about the possible cases of pref here. In future, we might support for cases if required

**Source-preserving request, proposal, or question:**

> Added comment for the AbortCmd… from transaction pov, it doesnt need to know about the possible cases of pref here. In future, we might support for cases if required

**Conditions and limits:**

- AbortCmd is outside normal dividend workflow; transaction need not know all possible distribution preferences unless future cases require it.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1311 · comment 497612570 · PR 9037 · 2024-05-02

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1311 · comment 497612570 · PR 9037 · 2024-05-02

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/DividendTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> [INV-3016] feat(dividend)(timeseries)(transaction): Support aborting dividend stuck in WithdrawalRequested

## A2-1332 — EdgeWarningAndRestrictionQueryLogic: Should we make this a method of `PlanStateValidationResult` instead? Merge the goalIds from the 3 impacted plan sets, no need to check again...

**Source stance:** open-question

**Context:**

> PR 8964 (Feat/INV-2795 warning blocks dpm), compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/EdgeWarningAndRestrictionQueryLogic.scala; original row 1332.

**Concern stated in the source:** Should we make this a method of `PlanStateValidationResult` instead? Merge the goalIds from the 3 impacted plan sets, no need to check against `customerGoals` ?

**Source-preserving request, proposal, or question:**

> Should we make this a method of `PlanStateValidationResult` instead? Merge the goalIds from the 3 impacted plan sets, no need to check against `customerGoals` ?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1332 · comment 494960710 · PR 8964 · 2024-04-23

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/EdgeWarningAndRestrictionQueryLogic.scala`

**Evidence:** anon-2.jsonl:1332 · comment 494960710 · PR 8964 · 2024-04-23

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/EdgeWarningAndRestrictionQueryLogic.scala`

**Explicit source context (pr_title):**

> Feat/INV-2795 warning blocks dpm

## A2-1345 — package: Many fields of same type next to each other makes this very easy to mess sth up during refactoring if we are not careful. Let’s just use this syntax instead

**Source stance:** suggestion

**Context:**

> PR 8692 ([EN-3026] Add funding instructions to add goal flow), advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/invest/package.scala; original row 1345.

**Concern stated in the source:** Many fields of same type next to each other makes this very easy to mess sth up during refactoring if we are not careful. Let’s just use this syntax instead

```
case r: SpecifiedAccountFundingInstructionsRequest => r.indicativeFxAmount
```

‌

**Source-preserving request, proposal, or question:**

> Many fields of same type next to each other makes this very easy to mess sth up during refactoring if we are not careful. Let’s just use this syntax instead
> 
> ```
> case r: SpecifiedAccountFundingInstructionsRequest => r.indicativeFxAmount
> ```
> 
> ‌

**Conditions and limits:**

- Type-pattern access to r.indicativeFxAmount avoids positional mistakes among many same-typed fields.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1345 · comment 484820008 · PR 8692 · 2024-03-25

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/invest/package.scala`

**Evidence:** anon-2.jsonl:1345 · comment 484820008 · PR 8692 · 2024-03-25

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/invest/package.scala`

**Explicit source context (pr_title):**

> [EN-3026] Add funding instructions to add goal flow

## A2-1402 — EmailDataFactory: Can remove “SG”

**Source stance:** suggestion

**Context:**

> PR 8632 (Feat/INV-2451/hk alts emails), investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala; original row 1402.

**Source-preserving request, proposal, or question:**

> Can remove “SG”

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1402 · comment 480880349 · PR 8632 · 2024-03-12

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala`

**Evidence:** anon-2.jsonl:1402 · comment 480880349 · PR 8632 · 2024-03-12

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala`

**Explicit source context (hunk):**

>          }
>          OrderEmailViewItem(
> -          confirmedDate = order.confirmedDate.map(date => FormatterUtils.dateFormatterDayFullMonthYear.format(date)), // SG Trade date
> -          confirmedPriceDate = order.confirmedPriceDate.map(date => FormatterUtils.dateFormatterInNumber.format(date)), // Nav Date
> +          confirmedDate = order.confirmedDate.map(date => Translator.translate(locale = preferredLocale, localDate = date, englishFormatter = FormatterUtils.dateFormatterDayFullMonthYear)), // Trade date
> +          confirmedPriceDate = order.confirmedPriceDate.map(date => Translator.translate(locale = preferredLocale, localDate = date, englishFormatter = FormatterUtils.dateFormatterInNumber)), // Nav Date
>            instrumentId = order.instrumentId,

**Evidence:** anon-2.jsonl:1402 · comment 480880349 · PR 8632 · 2024-03-12

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala`

**Explicit source context (pr_title):**

> Feat/INV-2451/hk alts emails

## A2-1439 — BaseServiceLogicImpl: Yes all the usage of this API mostly just check if plan exists.. and in general, if you query by not entity-id, you should expect EC regardless

**Source stance:** explanation

**Context:**

> PR 8906 ([INV-2906] feat(goal): Use Plan readside table for getPlansByCustomerId), goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala; original row 1439.

**Concern stated in the source:** Yes all the usage of this API mostly just check if plan exists.. and in general, if you query by not entity-id, you should expect EC regardless

**Source-preserving request, proposal, or question:**

> Yes all the usage of this API mostly just check if plan exists.. and in general, if you query by not entity-id, you should expect EC regardless

**Conditions and limits:**

- Non-entity-id plan lookup should be expected eventually consistent; consumers mostly check existence.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1439 · comment 491283491 · PR 8906 · 2024-04-12

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:1439 · comment 491283491 · PR 8906 · 2024-04-12

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-2906] feat(goal): Use Plan readside table for getPlansByCustomerId

## A2-1446 — package: Actually no need to split also right? This PR we will only release goal svc, all consumer of goal svc will still use old endpoints.

**Source stance:** suggestion

**Context:**

> PR 8568 ([EN-3050] Add initial funding instructions to plan models), goal-api/src/main/scala/com/endowus/silver/goal/api/requests/package.scala; original row 1446.

**Concern stated in the source:** Actually no need to split also right? This PR we will only release goal svc, all consumer of goal svc will still use old endpoints.

During release window, such request can hit either old or new goal instance

* old instance: continue working with V2, create cmd with amount but without fundingInstructions
* new instance: convert V2 to V3 request, create cmd with both amount and fundingInstructions

This cmd then again can hit either old or new goal instance

* old instance: create plan with amount but without fundingInstructions \(old behaviour\)
* new instance: create plan with both amount and fundingInstructions \(new behaviour\)

‌

**Source-preserving request, proposal, or question:**

> Actually no need to split also right? This PR we will only release goal svc, all consumer of goal svc will still use old endpoints.
> 
> During release window, such request can hit either old or new goal instance
> 
> * old instance: continue working with V2, create cmd with amount but without fundingInstructions
> * new instance: convert V2 to V3 request, create cmd with both amount and fundingInstructions
> 
> This cmd then again can hit either old or new goal instance
> 
> * old instance: create plan with amount but without fundingInstructions \(old behaviour\)
> * new instance: create plan with both amount and fundingInstructions \(new behaviour\)
> 
> ‌

**Conditions and limits:**

- Goal-only rollout keeps old consumer endpoints. Old/new HTTP instances may construct old/new commands and actor instances may independently persist amount-only or amount+instructions; preserve the full four-way rollout reasoning.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1446 · comment 483381270 · PR 8568 · 2024-03-20

Source path: `goal-api/src/main/scala/com/endowus/silver/goal/api/requests/package.scala`

**Evidence:** anon-2.jsonl:1446 · comment 483381270 · PR 8568 · 2024-03-20

Source path: `goal-api/src/main/scala/com/endowus/silver/goal/api/requests/package.scala`

**Explicit source context (pr_title):**

> [EN-3050] Add initial funding instructions to plan models

## A2-1461 — BaseTradingServiceLogicImpl: Should we also add internal endpoints to trigger this `UpdateCashReservationFxConversionRequestIdCmd` and `NotifyFxFundedTradeFxConversionRequestedC...

**Source stance:** open-question

**Context:**

> PR 8671 (TT-4025 Retry failed FX conversion request for auto FX trades), trading-impl/src/main/scala/com/endowus/silver/trading/impl/logic/service/BaseTradingServiceLogicImpl.scala; original row 1461.

**Concern stated in the source:** Should we also add internal endpoints to trigger this `UpdateCashReservationFxConversionRequestIdCmd` and `NotifyFxFundedTradeFxConversionRequestedCmd` in case this fut chain is interrupted mid way, e.g. deployment?

**Source-preserving request, proposal, or question:**

> Should we also add internal endpoints to trigger this `UpdateCashReservationFxConversionRequestIdCmd` and `NotifyFxFundedTradeFxConversionRequestedCmd` in case this fut chain is interrupted mid way, e.g. deployment?

**Conditions and limits:**

- Deployment can interrupt a Future chain midway; internal commands/endpoints could repair cash-reservation FX id and trade notification steps.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1461 · comment 483753094 · PR 8671 · 2024-03-21

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/logic/service/BaseTradingServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:1461 · comment 483753094 · PR 8671 · 2024-03-21

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/logic/service/BaseTradingServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> TT-4025 Retry failed FX conversion request for auto FX trades

## A2-1485 — CraManager: Remove this and move its code to `submitCra`. For other simulation purpose, we can just create the `Input` from state and call `matchAdvisoryProfile` directly, no ne...

**Source stance:** suggestion

**Context:**

> PR 8797 ([INV-2793] feat(advisory): Add endpoint to query eligibility for DPM account tagging. Calculate DPM eligibility on the fly and apply to relevant kafka CustomerAdvisoryProfileMsg), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala; original row 1485.

**Concern stated in the source:** Remove this and move its code to `submitCra`. For other simulation purpose, we can just create the `Input` from state and call `matchAdvisoryProfile` directly, no need to validate again.

**Source-preserving request, proposal, or question:**

> Remove this and move its code to `submitCra`. For other simulation purpose, we can just create the `Input` from state and call `matchAdvisoryProfile` directly, no need to validate again.

**Conditions and limits:**

- submitCra owns validation; simulations can build Input from state and call matchAdvisoryProfile directly.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1485 · comment 485401000 · PR 8797 · 2024-03-26

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Evidence:** anon-2.jsonl:1485 · comment 485401000 · PR 8797 · 2024-03-26

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Explicit source context (pr_title):**

> [INV-2793] feat(advisory): Add endpoint to query eligibility for DPM account tagging. Calculate DPM eligibility on the fly and apply to relevant kafka CustomerAdvisoryProfileMsg

## A2-1487 — Review: Existing naming in `transaction` svc is a bit confusing \(introduced by the multiple versions of entity migration\)

**Source stance:** suggestion

**Context:**

> PR 8795 ([PLATFORM-1092] Postgres read side table migration: Stop writing to gcp readside table for transaction), no inline path; original row 1487.

**Concern stated in the source:** Existing naming in `transaction` svc is a bit confusing \(introduced by the multiple versions of entity migration\)

* I believe the `V3` in existing `TransactionJdbcRepositoryV3` / `TransactionJdbcEventProcessorV3` / `TransactionJdbcProjectionV3` refers to the entity V3, not the version of table or projection. I suppose we should have named them `TransactionV3XXX` instead of `TransactionXXXV3`
* Now that the entity migration has completed successfully, I think we can switch the naming as follow:

    * `TransactionV3JdbcRepositoryV4`: ideally we should split this into single repository and versioned dbHandler \(similar to other services\), but we will clean this next time
    * `TransactionV3JdbcProjectionV2`
    

‌

**Source-preserving request, proposal, or question:**

> Existing naming in `transaction` svc is a bit confusing \(introduced by the multiple versions of entity migration\)
> 
> * I believe the `V3` in existing `TransactionJdbcRepositoryV3` / `TransactionJdbcEventProcessorV3` / `TransactionJdbcProjectionV3` refers to the entity V3, not the version of table or projection. I suppose we should have named them `TransactionV3XXX` instead of `TransactionXXXV3`
> * Now that the entity migration has completed successfully, I think we can switch the naming as follow:
> 
>     * `TransactionV3JdbcRepositoryV4`: ideally we should split this into single repository and versioned dbHandler \(similar to other services\), but we will clean this next time
>     * `TransactionV3JdbcProjectionV2`
>     
> 
> ‌

**Conditions and limits:**

- Entity V3 and table/projection version numbers are independent. Proposed naming: TransactionV3JdbcRepositoryV4, TransactionV3JdbcProjectionV2; handler/repository split deferred.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1487 · comment 484744191 · PR 8795 · 2024-03-25

**Evidence:** anon-2.jsonl:1487 · comment 484744191 · PR 8795 · 2024-03-25

**Explicit source context (pr_title):**

> [PLATFORM-1092] Postgres read side table migration: Stop writing to gcp readside table for transaction

## A2-1498 — InitiateCancellationFlowCmdHandler: It seems the approach taken in this cmd handler is to ignore if request has reached un-cancellable state

**Source stance:** explanation

**Context:**

> PR 8665 (TT-3981 Do not allow cancelling investment requests that have fxConversionRequestId defined), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala; original row 1498.

**Source-preserving request, proposal, or question:**

> It seems the approach taken in this cmd handler is to ignore if request has reached un-cancellable state
> 
> ‌

**Conditions and limits:**

- Command handler convention is to ignore requests in uncancellable state; preserve as an observed local approach.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1498 · comment 481441634 · PR 8665 · 2024-03-13

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala`

**Evidence:** anon-2.jsonl:1498 · comment 481441634 · PR 8665 · 2024-03-13

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala`

**Explicit source context (pr_title):**

> TT-3981 Do not allow cancelling investment requests that have fxConversionRequestId defined

## A2-1499 — InitiateCancellationFlowCmdHandler: Alright let’s leave those as is for now. This exception will also hit the serdes issue, but ok we clean in separate PR.

**Source stance:** explanation

**Context:**

> PR 8665 (TT-3981 Do not allow cancelling investment requests that have fxConversionRequestId defined), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala; original row 1499.

**Source-preserving request, proposal, or question:**

> Alright let’s leave those as is for now. This exception will also hit the serdes issue, but ok we clean in separate PR.

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- Cancellation exception serialization issue is acknowledged but accepted for separate cleanup, not claimed fixed.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1499 · comment 482757887 · PR 8665 · 2024-03-18

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala`

**Evidence:** anon-2.jsonl:1499 · comment 482757887 · PR 8665 · 2024-03-18

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala`

**Explicit source context (hunk):**

> +    existing.fundingInstructions match {
> +      case Some(fundingInstructions: SpecifiedAccountFundingInstructions) if fundingInstructions.fxConversionRequestId.isDefined =>
> +        return Effect.replyError(cmd.replyTo)(
> +          InvestmentSvcException(
> +            s"InvestmentPlanEntity [$entityId] received ${InitiateCancellationFlowCmd.getClass.getSimpleName} but the investment request has " +
> +              s"funding instructions with fxConversionRequestId [${fundingInstructions.fxConversionRequestId.get}], meaning " +
> +              s"that the cash for the FX conversion has already been reserved, and we implicitly assume that the FX conversion " +

**Evidence:** anon-2.jsonl:1499 · comment 482757887 · PR 8665 · 2024-03-18

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala`

**Explicit source context (pr_title):**

> TT-3981 Do not allow cancelling investment requests that have fxConversionRequestId defined

## A2-1500 — InitiateCancellationFlowCmdHandler: Maybe update the msg here to reflect latest decision, it’s not executed but only cash reserved right?

**Source stance:** suggestion

**Context:**

> PR 8665 (TT-3981 Do not allow cancelling investment requests that have fxConversionRequestId defined), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala; original row 1500.

**Source-preserving request, proposal, or question:**

> Maybe update the msg here to reflect latest decision, it’s not executed but only cash reserved right?

**Conditions and limits:**

- Message should say cash reserved rather than executed under latest decision.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1500 · comment 482758186 · PR 8665 · 2024-03-18

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala`

**Evidence:** anon-2.jsonl:1500 · comment 482758186 · PR 8665 · 2024-03-18

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala`

**Explicit source context (pr_title):**

> TT-3981 Do not allow cancelling investment requests that have fxConversionRequestId defined

## A2-1501 — TradingAccountEventProcessor: We should not come here cuz the cmd handler should cancel this already reserved cash in the first place?

**Source stance:** open-question

**Context:**

> PR 8664 (TT-3896 Handle trade cancellation if trade has specified account funding instructions), trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/tradingAccount/processors/TradingAccountEventProcessor.scala; original row 1501.

**Concern stated in the source:** We should not come here cuz the cmd handler should cancel this already reserved cash in the first place?

**Source-preserving request, proposal, or question:**

> We should not come here cuz the cmd handler should cancel this already reserved cash in the first place?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1501 · comment 483369082 · PR 8664 · 2024-03-20

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/tradingAccount/processors/TradingAccountEventProcessor.scala`

**Evidence:** anon-2.jsonl:1501 · comment 483369082 · PR 8664 · 2024-03-20

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/tradingAccount/processors/TradingAccountEventProcessor.scala`

**Explicit source context (pr_title):**

> TT-3896 Handle trade cancellation if trade has specified account funding instructions

## A2-1502 — UpdateTradeFxConversionRequestIdCmdHandler: Are you planning to use same cmd handler for future cases of `fundingInstructions`?

**Source stance:** open-question

**Context:**

> PR 8663 (TT-3887 Update trade and investment request with queued FX conversion request ID), trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateTradeFxConversionRequestIdCmdHandler.scala; original row 1502.

**Concern stated in the source:** Are you planning to use same cmd handler for future cases of `fundingInstructions`?

* if yes, then probably should make this cmd \+ event a bit more generic
* otherwise, let’s also match Some\(\_\) and throw? And maybe rename this cmd \+ event to be a bit specific about fx id of this auto fx funding instructions.

Same suggestion on investment svc side

‌

**Source-preserving request, proposal, or question:**

> Are you planning to use same cmd handler for future cases of `fundingInstructions`?
> 
> * if yes, then probably should make this cmd \+ event a bit more generic
> * otherwise, let’s also match Some\(\_\) and throw? And maybe rename this cmd \+ event to be a bit specific about fx id of this auto fx funding instructions.
> 
> Same suggestion on investment svc side
> 
> ‌

**Conditions and limits:**

- If command will cover future funding instructions, make it generic; otherwise reject existing Some and name specifically for autofx id. Same consideration applies in investment service.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1502 · comment 481440066 · PR 8663 · 2024-03-13

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateTradeFxConversionRequestIdCmdHandler.scala`

**Evidence:** anon-2.jsonl:1502 · comment 481440066 · PR 8663 · 2024-03-13

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateTradeFxConversionRequestIdCmdHandler.scala`

**Explicit source context (pr_title):**

> TT-3887 Update trade and investment request with queued FX conversion request ID

## A2-1510 — AcceptFxCreditSettlementCmdHandler: nits: `events ++= additionalEvts`

**Source stance:** suggestion

**Context:**

> PR 8661 (TT-3483 Handle BUY trades with funding instructions), trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/tradingAccount/handlers/AcceptFxCreditSettlementCmdHandler.scala; original row 1510.

**Source-preserving request, proposal, or question:**

> nits: `events ++= additionalEvts`
> 
> ‌

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1510 · comment 483729884 · PR 8661 · 2024-03-21

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/tradingAccount/handlers/AcceptFxCreditSettlementCmdHandler.scala`

**Evidence:** anon-2.jsonl:1510 · comment 483729884 · PR 8661 · 2024-03-21

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/tradingAccount/handlers/AcceptFxCreditSettlementCmdHandler.scala`

**Explicit source context (hunk):**

>      }
>  
> +    additionalEvts.foreach(events += _)
> +
>      events += FxOrderSettlementConfirmedEvt(fxOrderId)
>      events += BrokerAccountCashBalanceUpdatedEvt(
>        tradingAccount = tradingAccount,

**Evidence:** anon-2.jsonl:1510 · comment 483729884 · PR 8661 · 2024-03-21

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/tradingAccount/handlers/AcceptFxCreditSettlementCmdHandler.scala`

**Explicit source context (pr_title):**

> TT-3483 Handle BUY trades with funding instructions

## A2-1523 — FundSmartHelper: As discussed, let’s try to refactor this a bit more to reduce code dups

**Source stance:** suggestion

**Context:**

> PR 8619 (Resolve INV-2765: Endpoint to derive advisory questionnaire for a given set of instruments.), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/fundsmart/FundSmartHelper.scala; original row 1523.

**Source-preserving request, proposal, or question:**

> As discussed, let’s try to refactor this a bit more to reduce code dups

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1523 · comment 481688509 · PR 8619 · 2024-03-14

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/fundsmart/FundSmartHelper.scala`

**Evidence:** anon-2.jsonl:1523 · comment 481688509 · PR 8619 · 2024-03-14

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/fundsmart/FundSmartHelper.scala`

**Explicit source context (hunk):**

> +            }
> +          }
> +        }
> +      }
> +
> +      trait HkFundSmartAdvisoryQuestions extends FundSmartAdvisoryQuestions[HkAdvisoryQuestionnaire] with RegionSpecific[SilverRegion.Hk.type] {
> +

**Evidence:** anon-2.jsonl:1523 · comment 481688509 · PR 8619 · 2024-03-14

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/helpers/fundsmart/FundSmartHelper.scala`

**Explicit source context (pr_title):**

> Resolve INV-2765: Endpoint to derive advisory questionnaire for a given set of instruments.

## A2-1536 — HkEstimateAccessFeeGoalCreateBehaviour: Ah nvm me. That one is for existing plans. I guess we can refactor a bit, but yea next time

**Source stance:** suggestion

**Context:**

> PR 8488 (Resolve INV-2640: Changes to include estimation for multi-fund goal access fee for single fund goal creation.), charge-impl/src/main/scala/com/endowus/silver/charge/impl/productline/hk/HkEstimateAccessFeeGoalCreateBehaviour.scala; original row 1536.

**Source-preserving request, proposal, or question:**

> Ah nvm me. That one is for existing plans. I guess we can refactor a bit, but yea next time

**Conditions and limits:**

- Source corrects prior helper idea: it is for existing plans; refactor deferred.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1536 · comment 483370698 · PR 8488 · 2024-03-20

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/productline/hk/HkEstimateAccessFeeGoalCreateBehaviour.scala`

**Evidence:** anon-2.jsonl:1536 · comment 483370698 · PR 8488 · 2024-03-20

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/productline/hk/HkEstimateAccessFeeGoalCreateBehaviour.scala`

**Explicit source context (pr_title):**

> Resolve INV-2640: Changes to include estimation for multi-fund goal access fee for single fund goal creation.

## A2-1561 — PersistentEntityRefProvider: Let’s put a scaladoc for this class, noting down all the entity names that were used in the history

**Source stance:** suggestion

**Context:**

> PR 8122 (Feat/INV-2203 clean up transaction old entities), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/PersistentEntityRefProvider.scala; original row 1561.

**Source-preserving request, proposal, or question:**

> Let’s put a scaladoc for this class, noting down all the entity names that were used in the history

**Conditions and limits:**

- Historical entity names must be documented before removing old transaction entities.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1561 · comment 478982324 · PR 8122 · 2024-03-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/PersistentEntityRefProvider.scala`

**Evidence:** anon-2.jsonl:1561 · comment 478982324 · PR 8122 · 2024-03-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/PersistentEntityRefProvider.scala`

**Explicit source context (pr_title):**

> Feat/INV-2203 clean up transaction old entities

## A2-1566 — TransactionJdbcProjectionV2: Let’s not mix the naming, it can be confusing for future readers:

**Source stance:** suggestion

**Context:**

> PR 8122 (Feat/INV-2203 clean up transaction old entities), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/jdbc/TransactionJdbcProjectionV2.scala; original row 1566.

**Concern stated in the source:** Let’s not mix the naming, it can be confusing for future readers:

* `transaction-jdbc-handler-v1` is projection on V2 entity
* `transaction-jdbc-handler-v2` is projection on V3 entity to pipe data to V2

‌

I think let’s just use a bit more descriptive name to indicate that it’s projection from v3 entity to v2 repo. Maybe `transaction-v3-projection-to-v2-repo-v1`… last v1 is the version of the projection

Do same for the v1\_3 projection.

**Source-preserving request, proposal, or question:**

> Let’s not mix the naming, it can be confusing for future readers:
> 
> * `transaction-jdbc-handler-v1` is projection on V2 entity
> * `transaction-jdbc-handler-v2` is projection on V3 entity to pipe data to V2
> 
> ‌
> 
> I think let’s just use a bit more descriptive name to indicate that it’s projection from v3 entity to v2 repo. Maybe `transaction-v3-projection-to-v2-repo-v1`… last v1 is the version of the projection
> 
> Do same for the v1\_3 projection.

**Conditions and limits:**

- Projection source entity version and target repository version must be explicit; example transaction-v3-projection-to-v2-repo-v1 keeps last v1 as projection version.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1566 · comment 479020069 · PR 8122 · 2024-03-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/jdbc/TransactionJdbcProjectionV2.scala`

**Evidence:** anon-2.jsonl:1566 · comment 479020069 · PR 8122 · 2024-03-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/jdbc/TransactionJdbcProjectionV2.scala`

**Explicit source context (pr_title):**

> Feat/INV-2203 clean up transaction old entities

## A2-1583 — InstrumentState: Didn’t realize we are using same model in state and db… it should be cheap enough to convert back to DTO and use all the existing methods there?

**Source stance:** suggestion

**Context:**

> PR 8583 ([INV-2368] feat(instrument): Log warn for illiquid alts), instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentState.scala; original row 1583.

**Concern stated in the source:** Didn’t realize we are using same model in state and db… it should be cheap enough to convert back to DTO and use all the existing methods there?

**Source-preserving request, proposal, or question:**

> Didn’t realize we are using same model in state and db… it should be cheap enough to convert back to DTO and use all the existing methods there?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1583 · comment 479465028 · PR 8583 · 2024-03-07

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentState.scala`

**Evidence:** anon-2.jsonl:1583 · comment 479465028 · PR 8583 · 2024-03-07

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentState.scala`

**Explicit source context (pr_title):**

> [INV-2368] feat(instrument): Log warn for illiquid alts

## A2-1585 — TransactionTypes: We can let the old `FxConversionDetails` having optional accounts, as we are migrating away from this v1 model.

**Source stance:** suggestion

**Context:**

> PR 8011 (TT-3566 Make broker account optional for FX transactions), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/TransactionTypes.scala; original row 1585.

**Concern stated in the source:** We can let the old `FxConversionDetails` having optional accounts, as we are migrating away from this v1 model.

For new `FxTransaction` model:

* Changing `debitBrokerAccount` and `creditBrokerAccount` to optional here makes sense. All existing fx conversion txn would have them populated, and hence still compatible with old FE.
* But I think it’s also good to capture the fact that broker accounts will be available when the txn is settled. Maybe we can consider the following:

    * Add new `SettledFxStatusDetailsV2` that is identical with `SettledFxStatusDetails` with additionally the 2 required broker account fields
    * Change kafka subscriber to populate transaction using V2 instead of V1
    * Add 2 required broker account fields into `SettledFxStatusDetailsDto`
    
        * If entity has V2, map as is
        * If entity has V1, require the outer optional broker account fields in `FxTransaction` to be defined
        
    

‌

**Source-preserving request, proposal, or question:**

> We can let the old `FxConversionDetails` having optional accounts, as we are migrating away from this v1 model.
> 
> For new `FxTransaction` model:
> 
> * Changing `debitBrokerAccount` and `creditBrokerAccount` to optional here makes sense. All existing fx conversion txn would have them populated, and hence still compatible with old FE.
> * But I think it’s also good to capture the fact that broker accounts will be available when the txn is settled. Maybe we can consider the following:
> 
>     * Add new `SettledFxStatusDetailsV2` that is identical with `SettledFxStatusDetails` with additionally the 2 required broker account fields
>     * Change kafka subscriber to populate transaction using V2 instead of V1
>     * Add 2 required broker account fields into `SettledFxStatusDetailsDto`
>     
>         * If entity has V2, map as is
>         * If entity has V1, require the outer optional broker account fields in `FxTransaction` to be defined
>         
>     
> 
> ‌

**Conditions and limits:**

- Old FxConversionDetails can retain optional accounts while new settled FX V2 status requires accounts; V1 DTO conversion must require populated outer accounts.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1585 · comment 475752183 · PR 8011 · 2024-02-26

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/TransactionTypes.scala`

**Evidence:** anon-2.jsonl:1585 · comment 475752183 · PR 8011 · 2024-02-26

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/TransactionTypes.scala`

**Explicit source context (pr_title):**

> TT-3566 Make broker account optional for FX transactions

## A2-1591 — InvestOnceCmdHandler: Just put this check as another if in the block above?

**Source stance:** suggestion

**Context:**

> PR 7947 (TT-3480 Add funding instructions to investment request), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InvestOnceCmdHandler.scala; original row 1591.

**Source-preserving request, proposal, or question:**

> Just put this check as another if in the block above?

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1591 · comment 477278832 · PR 7947 · 2024-03-01

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InvestOnceCmdHandler.scala`

**Evidence:** anon-2.jsonl:1591 · comment 477278832 · PR 7947 · 2024-03-01

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InvestOnceCmdHandler.scala`

**Explicit source context (hunk):**

> +        if (fundingInstructions.fxConversionRequestId.isDefined) {
> +          return Effect.replyError(cmd.replyTo)(
> +            new Exception(
> +              s"Unable to invest once - plan [$entityId] funding instructions has fxConversionRequestId [${cmd.fundingInstructions.get.asInstanceOf[SpecifiedAccountFundingInstructions].fxConversionRequestId.get}] defined!"
> +            )
> +          )
> +        }

**Evidence:** anon-2.jsonl:1591 · comment 477278832 · PR 7947 · 2024-03-01

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InvestOnceCmdHandler.scala`

**Explicit source context (pr_title):**

> TT-3480 Add funding instructions to investment request

## A2-1595 — InvestOnceCmdHandler: Use the matched `fundingInstructions` instead of casting `cmd.fundingInstructions` again

**Source stance:** suggestion

**Context:**

> PR 7947 (TT-3480 Add funding instructions to investment request), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InvestOnceCmdHandler.scala; original row 1595.

**Source-preserving request, proposal, or question:**

> Use the matched `fundingInstructions` instead of casting `cmd.fundingInstructions` again

**Conditions and limits:**

- Use already-matched fundingInstructions rather than casting cmd.fundingInstructions again.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1595 · comment 478494261 · PR 7947 · 2024-03-05

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InvestOnceCmdHandler.scala`

**Evidence:** anon-2.jsonl:1595 · comment 478494261 · PR 7947 · 2024-03-05

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InvestOnceCmdHandler.scala`

**Explicit source context (pr_title):**

> TT-3480 Add funding instructions to investment request

## A2-1600 — RebateDistributionJdbcEventProcessor: Nit naming. We normally name these with snake case `<entity>-jdbc-evt-handler-vX` so maybe `rebate-distribution-jdbc-evt-handler-v1`?

**Source stance:** suggestion

**Context:**

> PR 8353 (Feat/INV-1996/automate trailer rebate), rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/processors/RebateDistributionJdbcEventProcessor.scala; original row 1600.

**Source-preserving request, proposal, or question:**

> Nit naming. We normally name these with snake case `<entity>-jdbc-evt-handler-vX` so maybe `rebate-distribution-jdbc-evt-handler-v1`?
> 
> ‌

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- The source calls the naming convention snake case while its example uses hyphens. Preserve its literal recommendation without silently relabeling the convention.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1600 · comment 476105567 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/processors/RebateDistributionJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:1600 · comment 476105567 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/processors/RebateDistributionJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +  )(implicit ec: ExecutionContext, system: ActorSystem)
> +  extends StrictLogging {
> +
> +  private val Version = 4
> +
> +  private val ProjectionId = s"rebate-distribution-jdbc-evt-handler-v${Version}"
> +

**Evidence:** anon-2.jsonl:1600 · comment 476105567 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/processors/RebateDistributionJdbcEventProcessor.scala`

**Explicit source context (pr_title):**

> Feat/INV-1996/automate trailer rebate

## A2-1624 — InstrumentTable: [person] [person] let’s create tix, if not already, to completely get rid of V1 instrument repository \+ its entity later

**Source stance:** suggestion

**Context:**

> PR 8384 ([PLATFORM-1067] Postgres read side table migration: Stop writing to gcp readside table for instrument), instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/db/jdbc/InstrumentTable.scala; original row 1624.

**Concern stated in the source:** [person] [person] let’s create tix, if not already, to completely get rid of V1 instrument repository \+ its entity later

**Source-preserving request, proposal, or question:**

> [person] [person] let’s create tix, if not already, to completely get rid of V1 instrument repository \+ its entity later

**Conditions and limits:**

- Complete removal of V1 instrument repository/entity is future ticketed work.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1624 · comment 474051966 · PR 8384 · 2024-02-21

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/db/jdbc/InstrumentTable.scala`

> let’s create tix, if not already, to completely get rid of V1 instrument repository \+ its entity later

**Evidence:** anon-2.jsonl:1624 · comment 474051966 · PR 8384 · 2024-02-21

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/db/jdbc/InstrumentTable.scala`

**Explicit source context (pr_title):**

> [PLATFORM-1067] Postgres read side table migration: Stop writing to gcp readside table for instrument

## A2-1636 — RegionalCustomerTopicCustomer: Not possible as of now I think. I mean if any chance of mistake, at least on our side, we only touch the schedules, which are easy to reinstate. A...

**Source stance:** suggestion

**Context:**

> PR 8215 ([INV-1959] feat(goal): Listen to customer deactivated msg), goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala; original row 1636.

**Concern stated in the source:** Not possible as of now I think. I mean if any chance of mistake, at least on our side, we only touch the schedules, which are easy to reinstate. Active goals if any, just let them be, no harm for us.

**Source-preserving request, proposal, or question:**

> Not possible as of now I think. I mean if any chance of mistake, at least on our side, we only touch the schedules, which are easy to reinstate. Active goals if any, just let them be, no harm for us.

**Conditions and limits:**

- Schedules are easy to reinstate; touching active goals is avoided under uncertain manual checks.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1636 · comment 467661196 · PR 8215 · 2024-02-02

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala`

**Evidence:** anon-2.jsonl:1636 · comment 467661196 · PR 8215 · 2024-02-02

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala`

**Explicit source context (pr_title):**

> [INV-1959] feat(goal): Listen to customer deactivated msg

## A2-1638 — RegionalCustomerTopicCustomer: Entity is keyed by goalId so would it be better to increase parallelism for goals to 4, keeping parallelism for plans at 1?

**Source stance:** open-question

**Context:**

> PR 8215 ([INV-1959] feat(goal): Listen to customer deactivated msg), goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala; original row 1638.

**Concern stated in the source:** Entity is keyed by goalId so would it be better to increase parallelism for goals to 4, keeping parallelism for plans at 1?

**Source-preserving request, proposal, or question:**

> Entity is keyed by goalId so would it be better to increase parallelism for goals to 4, keeping parallelism for plans at 1?

**Conditions and limits:**

- Goal entity is keyed goalId; proposed goals parallelism=4 but plans within each goal=1.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1638 · comment 473482567 · PR 8215 · 2024-02-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala`

**Evidence:** anon-2.jsonl:1638 · comment 473482567 · PR 8215 · 2024-02-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala`

**Explicit source context (pr_title):**

> [INV-1959] feat(goal): Listen to customer deactivated msg

## A2-1648 — EmailDataFactory: [person] this one just need a method in `Translator` for ZonedDateTime?

**Source stance:** suggestion

**Context:**

> PR 8240 ([EN-2852] feat(investment)(redemption): zh-Hant-HK support email), investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala; original row 1648.

**Concern stated in the source:** [person] this one just need a method in `Translator` for ZonedDateTime?

```
def translate(locale: Locale, zonedDateTime: ZonedDateTime, englishFormatter: DateTimeFormatter): String = ???
```

‌

**Source-preserving request, proposal, or question:**

> [person] this one just need a method in `Translator` for ZonedDateTime?
> 
> ```
> def translate(locale: Locale, zonedDateTime: ZonedDateTime, englishFormatter: DateTimeFormatter): String = ???
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1648 · comment 467726918 · PR 8240 · 2024-02-02

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala`

> this one just need a method in `Translator` for ZonedDateTime?
> 
> ```
> def translate(locale: Locale, zonedDateTime: ZonedDateTime, englishFormatter: DateTimeFormatter): String = ???
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:1648 · comment 467726918 · PR 8240 · 2024-02-02

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/EmailDataFactory.scala`

**Explicit source context (pr_title):**

> [EN-2852] feat(investment)(redemption): zh-Hant-HK support email

## A2-1716 — package: Let me think a bit more on this. Probably we want to include both the current and previous quarter amount here. Otherwise the amount on full redemption request would be...

**Source stance:** suggestion

**Context:**

> PR 7865 ([INV-2438] feat(charge)(redemption): Split full redemption fee charges by quarter), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/ces/state/package.scala; original row 1716.

**Concern stated in the source:** Let me think a bit more on this. Probably we want to include both the current and previous quarter amount here. Otherwise the amount on full redemption request would be inconsistent

**Source-preserving request, proposal, or question:**

> Let me think a bit more on this. Probably we want to include both the current and previous quarter amount here. Otherwise the amount on full redemption request would be inconsistent

**Conditions and limits:**

- Full redemption request amount should probably include both prior and current quarter; source is still thinking through it.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1716 · comment 454351406 · PR 7865 · 2023-12-18

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/ces/state/package.scala`

**Evidence:** anon-2.jsonl:1716 · comment 454351406 · PR 7865 · 2023-12-18

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/ces/state/package.scala`

**Explicit source context (pr_title):**

> [INV-2438] feat(charge)(redemption): Split full redemption fee charges by quarter

## A2-1717 — InitiateFeeChargeCmdHandler: No issue for charge flow. But I rmb some charge dashboard were checking if we have missing charge, hence last time we added this logic to waive prev...

**Source stance:** suggestion

**Context:**

> PR 7865 ([INV-2438] feat(charge)(redemption): Split full redemption fee charges by quarter), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/InitiateFeeChargeCmdHandler.scala; original row 1717.

**Concern stated in the source:** No issue for charge flow. But I rmb some charge dashboard were checking if we have missing charge, hence last time we added this logic to waive prev quarter if not already waive.

The logic you see here is just refactor or previous version, but I organise it so that we can reuse the `innerHandleInitiateFeeCharge`

**Source-preserving request, proposal, or question:**

> No issue for charge flow. But I rmb some charge dashboard were checking if we have missing charge, hence last time we added this logic to waive prev quarter if not already waive.
> 
> The logic you see here is just refactor or previous version, but I organise it so that we can reuse the `innerHandleInitiateFeeCharge`

**Conditions and limits:**

- Charge dashboards checked for missing previous-quarter charges, motivating explicit waive of previous quarter; refactor shares innerHandleInitiateFeeCharge.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1717 · comment 455021983 · PR 7865 · 2023-12-20

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/InitiateFeeChargeCmdHandler.scala`

**Evidence:** anon-2.jsonl:1717 · comment 455021983 · PR 7865 · 2023-12-20

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/InitiateFeeChargeCmdHandler.scala`

**Explicit source context (pr_title):**

> [INV-2438] feat(charge)(redemption): Split full redemption fee charges by quarter

## A2-1736 — Review: Not touching redemption yet as we would still allow customer to liquidate their AI-only funds \(when they are retail\) or when they are suspended \(POps does on behalf o...

**Source stance:** explanation

**Context:**

> PR 7789 ([INV-2326] feat(advisory)(instrument)(investment)(rebalance): Add support instrument subscription cutoff. Improve tradability checks), no inline path; original row 1736.

**Concern stated in the source:** Not touching redemption yet as we would still allow customer to liquidate their AI-only funds \(when they are retail\) or when they are suspended \(POps does on behalf of customer\)

Will refactor \+ switch to instrumentV2 for redemption in another PR when I work on it next.

**Source-preserving request, proposal, or question:**

> Not touching redemption yet as we would still allow customer to liquidate their AI-only funds \(when they are retail\) or when they are suspended \(POps does on behalf of customer\)
> 
> Will refactor \+ switch to instrumentV2 for redemption in another PR when I work on it next.

**Conditions and limits:**

- Redemption intentionally still permits retail liquidating AI-only funds and suspended-user POps on-behalf liquidation; instrumentV2/tradability refactor deferred.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1736 · comment 451523134 · PR 7789 · 2023-12-07

**Evidence:** anon-2.jsonl:1736 · comment 451523134 · PR 7789 · 2023-12-07

**Explicit source context (pr_title):**

> [INV-2326] feat(advisory)(instrument)(investment)(rebalance): Add support instrument subscription cutoff. Improve tradability checks

## A2-1776 — AltsLcoCalculationMatrix: Feels like this and the scoreCalculator can be refactor a bit more to remove duplicate code, but ok we can iterate on this later

**Source stance:** suggestion

**Context:**

> PR 7673 (Resolve INV-2277: Add alts suitability check for instruments using LCO match.), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/calculators/questionnaire/alts/suitability/AltsLcoCalculationMatrix.scala; original row 1776.

**Concern stated in the source:** Feels like this and the scoreCalculator can be refactor a bit more to remove duplicate code, but ok we can iterate on this later

**Source-preserving request, proposal, or question:**

> Feels like this and the scoreCalculator can be refactor a bit more to remove duplicate code, but ok we can iterate on this later

**Conditions and limits:**

- More duplicate-code refactor can wait.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1776 · comment 450195853 · PR 7673 · 2023-12-04

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/calculators/questionnaire/alts/suitability/AltsLcoCalculationMatrix.scala`

**Evidence:** anon-2.jsonl:1776 · comment 450195853 · PR 7673 · 2023-12-04

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/calculators/questionnaire/alts/suitability/AltsLcoCalculationMatrix.scala`

**Explicit source context (pr_title):**

> Resolve INV-2277: Add alts suitability check for instruments using LCO match.

## A2-1780 — ServiceLogicImpl: We can already trust data from this repo, no need to go entity if repo says no annual yield

**Source stance:** suggestion

**Context:**

> PR 7742 ([INV-2374] feat(marketdata): Reduce sentry noise when syncing annual yield), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala; original row 1780.

**Source-preserving request, proposal, or question:**

> We can already trust data from this repo, no need to go entity if repo says no annual yield

**Conditions and limits:**

- Annual-yield repo is trusted; absent annual yield should not force entity fallback.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1780 · comment 450190446 · PR 7742 · 2023-12-04

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:1780 · comment 450190446 · PR 7742 · 2023-12-04

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-2374] feat(marketdata): Reduce sentry noise when syncing annual yield

## A2-1802 — MarketDataUploader: Call annual yield here too. So you just need to upsert always. No need to link with entity/processor

**Source stance:** suggestion

**Context:**

> PR 7443 (Feat/INV-2229 marketdata ex dividend bond yield), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; original row 1802.

**Source-preserving request, proposal, or question:**

> Call annual yield here too. So you just need to upsert always. No need to link with entity/processor
> 
> ‌

**Conditions and limits:**

- Annual-yield update can directly upsert; source says no entity/processor coupling is needed for that path.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1802 · comment 442753980 · PR 7443 · 2023-11-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:1802 · comment 442753980 · PR 7443 · 2023-11-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> Feat/INV-2229 marketdata ex dividend bond yield

## A3-0068 — InstrumentCommandsHandler.scala: We only have 2 states, None or with instrument… anyhow we already have to list of the cmd for each state, so I think can just split this get handler i

**Source stance:** suggestion

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentCommandsHandler.scala; PR: Resolve INV-2049: New instrument events, event handlers, v2 logic split.

**Source-preserving request, proposal, or question:**

> We only have 2 states, None or with instrument… anyhow we already have to list of the cmd for each state, so I think can just split this get handler in each state case

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:1884 · comment 437286823 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentCommandsHandler.scala`

## A3-0069 — InstrumentState.scala: Updating this should be part of logic/manager and here we can just use data from DTO directly?

**Source stance:** open-question

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentState.scala; PR: Resolve INV-2049: New instrument events, event handlers, v2 logic split.

**Source-preserving request, proposal, or question:**

> Updating this should be part of logic/manager and here we can just use data from DTO directly?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1885 · comment 437288081 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentState.scala`

**Evidence:** anon-2.jsonl:1885 · comment 437288081 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentState.scala`

**Explicit source context (hunk):**

> +    subscriptionDetails = dto.subscriptionDetails.map(SubscriptionDetails.fromDto),
> +    redemptionDetails = dto.redemptionDetails.map(RedemptionDetails.fromDto),
> +    lastModifiedBy = dto.lastModifiedBy,
> +    lastModifiedAt = now
> +  )
> +
> +  def toV1Dto(instrument: Instrument)(implicit region: SilverRegion): InstrumentInfoDtoV1 = convertToV1Dto(toDto(instrument))

## A3-0070 — InstrumentCommandsHandler.scala: And I suppose the only reason we have to list all these cmd is because we need the replyTo which is not available at trait level… I guess we can live 

**Source stance:** explanation

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentCommandsHandler.scala; PR: Resolve INV-2049: New instrument events, event handlers, v2 logic split.

**Concern stated in the source:** And I suppose the only reason we have to list all these cmd is because we need the replyTo which is not available at trait level… I guess we can live with this for now, but this looks so ugly :rofl: It’s existing code anyway

**Source-preserving request, proposal, or question:**

> And I suppose the only reason we have to list all these cmd is because we need the replyTo which is not available at trait level… I guess we can live with this for now, but this looks so ugly :rofl: It’s existing code anyway

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1886 · comment 437289162 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentCommandsHandler.scala`

**Evidence:** anon-2.jsonl:1886 · comment 437289162 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentCommandsHandler.scala`

**Explicit source context (hunk):**

> +        case cmd: PublishInstrumentCmd =>
> +          Effect.reply(cmd.replyTo)(Done)
> +        case cmd: WithReply[Any] =>
> +          Effect.reply(cmd.replyTo)(s"Unable to perform ${cmd.getClass.getSimpleName}, $entityId does not exist!".error)
> +      }
> +  }
> +

## A3-0074 — InstrumentDataUpdateManagerV2.scala: So how do we update from No/Partial to Full status?

**Source stance:** open-question

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala; PR: Resolve INV-2049: New instrument events, event handlers, v2 logic split.

**Source-preserving request, proposal, or question:**

> So how do we update from No/Partial to Full status?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1891 · comment 437299128 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala`

**Evidence:** anon-2.jsonl:1891 · comment 437299128 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala`

**Explicit source context (hunk):**

> +    enabledForFundSmartCma: Boolean,
> +    existingDueDiligenceDetails: DueDiligenceDetailsDto
> +  ): DueDiligenceDetailsDto = existingDueDiligenceDetails match {
> +    case models.NoDueDiligenceDetailsDto | models.PartialDueDiligenceDetailsDto =>
> +      throw BadRequest("Invalid update of whitelisting [fundSmartGwa] and [fundSmartCma] flags since due diligence is not complete.")
> +    case _: FullDueDiligenceDetailsDto =>
> +      FullDueDiligenceDetailsDto(

## A3-0080 — InstrumentCmdDelegator.scala: So what’s the diff? Yours mean we don’t need to worry about other BaseInstrument impl until we need them? And if cmd is invoked on invalid state, e.g.

**Source stance:** open-question

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/handlers/InstrumentCmdDelegator.scala; PR: Resolve INV-2049: New instrument events, event handlers, v2 logic split.

**Source-preserving request, proposal, or question:**

> So what’s the diff? Yours mean we don’t need to worry about other BaseInstrument impl until we need them? And if cmd is invoked on invalid state, e.g. update detail on non-existing instruments, we want to return generic cmd handler not found \(I don’t remember exact error msg\), instead of customized `Unable to update instrument details, $entityId does not exist` ?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:1897 · comment 438080041 · PR 7097 · 2023-10-23

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/handlers/InstrumentCmdDelegator.scala`

## A3-0082 — InstrumentState.scala: Generally I’d prefer to keep these methods as pure getter/setter between dto and model. But yeah we can leave this for now, it’s easy to change later,

**Source stance:** suggestion

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentState.scala; PR: Resolve INV-2049: New instrument events, event handlers, v2 logic split.

**Source-preserving request, proposal, or question:**

> Generally I’d prefer to keep these methods as pure getter/setter between dto and model. But yeah we can leave this for now, it’s easy to change later, if needed

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1899 · comment 438413698 · PR 7097 · 2023-10-24

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentState.scala`

**Evidence:** anon-2.jsonl:1899 · comment 438413698 · PR 7097 · 2023-10-24

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentState.scala`

**Explicit source context (hunk):**

> +    subscriptionDetails = dto.subscriptionDetails.map(SubscriptionDetails.fromDto),
> +    redemptionDetails = dto.redemptionDetails.map(RedemptionDetails.fromDto),
> +    lastModifiedBy = dto.lastModifiedBy,
> +    lastModifiedAt = now
> +  )
> +
> +  def toV1Dto(instrument: Instrument)(implicit region: SilverRegion): InstrumentInfoDtoV1 = convertToV1Dto(toDto(instrument))

## A3-0088 — UpdateCurrentAssetAllocationCmdHandler.scala: Need to break this method… otherwise we will have wrong reason

**Source stance:** requested-change

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/UpdateCurrentAssetAllocationCmdHandler.scala; PR: [INV-1504] feat(goal)(rebalance): Avoid race condition for TAA update between goal modification vs RPC acceptance

**Concern stated in the source:** Need to break this method… otherwise we will have wrong reason

**Source-preserving request, proposal, or question:**

> Need to break this method… otherwise we will have wrong reason

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:1905 · comment 428444163 · PR 6953 · 2023-09-19

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/UpdateCurrentAssetAllocationCmdHandler.scala`

## A3-0090 — AcceptSuggestedRebalanceRequestCmdHandler.scala: Yeah, with new logic, it could be accepted RPC but haven’t triggered yet also. I added some comments to explain.

**Source stance:** explanation

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/AcceptSuggestedRebalanceRequestCmdHandler.scala; PR: [INV-1504] feat(goal)(rebalance): Avoid race condition for TAA update between goal modification vs RPC acceptance

**Source-preserving request, proposal, or question:**

> Yeah, with new logic, it could be accepted RPC but haven’t triggered yet also. I added some comments to explain.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1907 · comment 429841536 · PR 6953 · 2023-09-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/AcceptSuggestedRebalanceRequestCmdHandler.scala`

**Evidence:** anon-2.jsonl:1907 · comment 429841536 · PR 6953 · 2023-09-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/AcceptSuggestedRebalanceRequestCmdHandler.scala`

**Explicit source context (hunk):**

> +        // - goal-modification rebalance, once triggered, would already cancel active threshold breach
> +        // - RPC rebalance, if accepted but not initiated yet, would not interfere with active threshold breach, hence cron might still accept it
> +        // In both cases, threshold breach would be obsolete
> +        val events = generateCancellationEventsForThresholdBreach(plan, request, "Threshold breach was not detected anymore")
> +        return Effect.persist[Event, State](events).thenAck(cmd.replyTo)
> +      } else {
> +        // RPC is accepted by customers

## A3-0091 — UpdateCurrentAssetAllocationCmdHandler.scala: this shouldn’t happen. I log error here to alert just in case.

**Source stance:** explanation

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/UpdateCurrentAssetAllocationCmdHandler.scala; PR: [INV-1504] feat(goal)(rebalance): Avoid race condition for TAA update between goal modification vs RPC acceptance

**Source-preserving request, proposal, or question:**

> Yeah this shouldn’t happen. I log error here to alert just in case.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1908 · comment 429841637 · PR 6953 · 2023-09-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/UpdateCurrentAssetAllocationCmdHandler.scala`

**Evidence:** anon-2.jsonl:1908 · comment 429841637 · PR 6953 · 2023-09-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/UpdateCurrentAssetAllocationCmdHandler.scala`

**Explicit source context (hunk):**

> +        logger.info(s"""
> +        |RebalancePlanEntity [$entityId] is skipping UpdateCurrentAssetAllocationCmd for rebalance request ${existingRequest.rebalanceRequestId}
> +        |which already in status ${existingRequest.status}.
> +        |""".fuse)
> +        Effect.ack(cmd.replyTo)
>  
> -    if (sameRequestAlreadyReceived) {

## A3-0092 — UpdateCurrentAssetAllocationCmdHandler.scala: Same here, this should not happen based on our checks in other cmd handlers. Just logging to alert and do not proceed just in case we miss anything

**Source stance:** explanation

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/UpdateCurrentAssetAllocationCmdHandler.scala; PR: [INV-1504] feat(goal)(rebalance): Avoid race condition for TAA update between goal modification vs RPC acceptance

**Source-preserving request, proposal, or question:**

> Same here, this should not happen based on our checks in other cmd handlers. Just logging to alert and do not proceed just in case we miss anything

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1909 · comment 429841762 · PR 6953 · 2023-09-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/UpdateCurrentAssetAllocationCmdHandler.scala`

**Evidence:** anon-2.jsonl:1909 · comment 429841762 · PR 6953 · 2023-09-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/UpdateCurrentAssetAllocationCmdHandler.scala`

**Explicit source context (hunk):**

> +        |RebalancePlanEntity [$entityId] is skipping UpdateCurrentAssetAllocationCmd for rebalance request ${existingRequest.rebalanceRequestId}
> +        |which already in status ${existingRequest.status}.
> +        |""".fuse)
> +        Effect.ack(cmd.replyTo)
>  
> -    if (sameRequestAlreadyReceived) {
> -      logger.info(s"[$entityId] skip the update current asset allocation cmd because it got same request already received")

## A3-0094 — Rebalance-in-progress RPC acceptance: modification cancellation versus threshold-breach race

**Source stance:** explanation

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/AcceptSuggestedRebalanceRequestCmdHandler.scala; PR: [INV-1504] feat(goal)(rebalance): Avoid race condition for TAA update between goal modification vs RPC acceptance

**Concern stated in the source:** if due to threshold breach, then it’s possible because we don’t block today

**Source-preserving request, proposal, or question:**

> So if rebalance plan side has its entity updated to rebalance-in-progress \(outer if\):
> 
> 1. if due to goal modification, that cmd handler should have already cancelled the RPC, here it should fail at `RebalanceSuggestionAcceptableStatuses` check
> 2. if due to threshold breach, then it’s possible because we don’t block today
> 
> In both cases, we will send error to FE, hence the exception thrown. But \(1\) should not happen, hence the extra error log.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1911 · comment 429930628 · PR 6953 · 2023-09-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/AcceptSuggestedRebalanceRequestCmdHandler.scala`

> So if rebalance plan side has its entity updated to rebalance-in-progress \(outer if\):
> 
> 1. if due to goal modification, that cmd handler should have already cancelled the RPC, here it should fail at `RebalanceSuggestionAcceptableStatuses` check
> 2. if due to threshold breach, then it’s possible because we don’t block today
> 
> In both cases, we will send error to FE, hence the exception thrown. But \(1\) should not happen, hence the extra error log.
> 
> ‌

**Evidence:** anon-2.jsonl:1911 · comment 429930628 · PR 6953 · 2023-09-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/AcceptSuggestedRebalanceRequestCmdHandler.scala`

**Explicit source context (hunk):**

> +        // - goal-modification rebalance, once triggered, would already cancel active RPC
> +        // - threshold-breach rebalance, however, would not interfere with active RPC, hence customer might still accept it
> +        // TODO: Edge logic to notify this to FE, instead of letting customer accepts then throwing error
> +        if (state.inProgressRebalanceRequests.exists(_.reason != RebalanceReason.THRESHOLD_BREACH)) {
> +          logger.error(s"""
> +          |[$entityId] Can not accept the request(id=${request.rebalanceRequestId}, reason=${request.reason})
> +          |because the plan is already rebalancing in progress, however not due to threshold breach.

## A3-0095 — UpdateCurrentAssetAllocationCmdHandler.scala: For RPC, goal svc will send a TAA updated msg which will trigger this cmd. However, we will skip it, cuz we change the flow to trigger both RPC/Breach

**Source stance:** explanation

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/UpdateCurrentAssetAllocationCmdHandler.scala; PR: [INV-1504] feat(goal)(rebalance): Avoid race condition for TAA update between goal modification vs RPC acceptance

**Concern stated in the source:** However, we will skip it, cuz we change the flow to trigger both RPC/Breach rebalance using the rebalance started msg from goal.

**Source-preserving request, proposal, or question:**

> For RPC, goal svc will send a TAA updated msg which will trigger this cmd. However, we will skip it, cuz we change the flow to trigger both RPC/Breach rebalance using the rebalance started msg from goal. Hence this is info log.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1912 · comment 430383223 · PR 6953 · 2023-09-25

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/UpdateCurrentAssetAllocationCmdHandler.scala`

**Evidence:** anon-2.jsonl:1912 · comment 430383223 · PR 6953 · 2023-09-25

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/UpdateCurrentAssetAllocationCmdHandler.scala`

**Explicit source context (hunk):**

> +      cmd.rebalanceRequestId.contains(request.rebalanceRequestId)
> +    } match {
> +      case Some(existingRequest) if existingRequest.reason == RebalanceReason.PORTFOLIO_VERSION_UPDATE =>
> +        logger.info(s"""
> +        |RebalancePlanEntity [$entityId] is skipping UpdateCurrentAssetAllocationCmd for RPC request ${existingRequest.rebalanceRequestId}
> +        |which is in status ${existingRequest.status}. Rebalance will trigger via InitiateAcceptedRebalanceSuggestionCmdHandler instead.
> +        |""".fuse)

## A3-0096 — d56 RPC verification: goal modification, threshold breach, acceptance and race outcomes

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1504] feat(goal)(rebalance): Avoid race condition for TAA update between goal modification vs RPC acceptance

**Concern stated in the source:** * single goal modification
* single threshold breach
* single RPC acceptance
* race between goal modification and RPC acceptance: goal modification is rejected if RPC reaches goal svc first, otherwise RPC is ignored and overridden by goal modification

**Source-preserving request, proposal, or question:**

> Tested in d56 the following scenarios, all are working as expected
> 
> * single goal modification
> * single threshold breach
> * single RPC acceptance
> * race between goal modification and RPC acceptance: goal modification is rejected if RPC reaches goal svc first, otherwise RPC is ignored and overridden by goal modification

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The four scenarios and RPC/goal-modification race outcomes are reported verification only.

**Evidence:** anon-2.jsonl:1913 · comment 438089407 · PR 6953 · 2023-10-23

> Tested in d56 the following scenarios, all are working as expected
> 
> * single goal modification
> * single threshold breach
> * single RPC acceptance
> * race between goal modification and RPC acceptance: goal modification is rejected if RPC reaches goal svc first, otherwise RPC is ignored and overridden by goal modification
> 
> ‌

## A3-0111 — package.scala: Just put this in `state/package` or even companion object of the get cmd… It’s a simple wrapper, everywhere else should continue to interact with List

**Source stance:** suggestion

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/commons/package.scala; PR: [INV-1988] fix(rebalance): Encapsulate reply to be serializable

**Source-preserving request, proposal, or question:**

> Just put this in `state/package` or even companion object of the get cmd… It’s a simple wrapper, everywhere else should continue to interact with List\[\]

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:1928 · comment 433953872 · PR 7119 · 2023-10-09

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/commons/package.scala`

## A3-0116 — RPC endpoints intentionally differ: customer readside versus goal entity consistency

**Source stance:** requested-change

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala; PR: [INV-1988] feat(gateway, rebalance): migrate recommended portfolio changes endpoint from davinci

**Source-preserving request, proposal, or question:**

> Ah nevermind me lol. Let’s put a comment to explain that customer endpoint is using readside while goal endpoint is using entity for data consistency

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source rows 1932, 1933: Struck-through shared-code suggestion is revised to explain customer-readside versus goal-entity behavior.

**Evidence:** anon-2.jsonl:1933 · comment 431718424 · PR 6874 · 2023-09-29

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:1933 · comment 431718424 · PR 6874 · 2023-09-29

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +      plans = goal.plans.map(p => (p.planId, p.tradingAccountType, goal.name, goal.investmentGoalType))
> +      recommendedPortfolioChangeDtos <- Source(plans)
> +        .mapAsync(2) {
> +          case (planId, tradingAccountType, goalName, goalType) =>
> +            for {
> +              rebalanceRequestDtos <- getRebalanceRequestDtosForGoal(
> +                customerId = goal.customerId,

## A3-0135 — ServiceLogicImpl.scala: Should we add some validations here? e.g. request is indeed for RPC and still either pendingAcceptance/rejected

**Source stance:** suggestion

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala; PR: [INV1987] feat(rebalance): add rebalance summary endpoint

**Source-preserving request, proposal, or question:**

> Should we add some validations here? e.g. request is indeed for RPC and still either pendingAcceptance/rejected

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1953 · comment 429831884 · PR 6868 · 2023-09-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:1953 · comment 429831884 · PR 6868 · 2023-09-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +  override def getRecommendedPortfolioChangesSummary(planId: UUID, requestId: UUID, displayCcy: CurrencyUnit): Future[RecommendedPortfolioChangesSummaryDto] = {
> +    for {
> +      rebalanceRequest <- findRebalanceRequest(planId, requestId)
> +      customerId = rebalanceRequest.customerId
> +      goalId = rebalanceRequest.goalId
> +      tradingAccountType = rebalanceRequest.tradingAccountType

## A3-0139 — RPC read-only summary may see accepted/cancelled TAA; FE-list precondition currently tolerated

**Source stance:** explanation

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala; PR: [INV1987] feat(rebalance): add rebalance summary endpoint

**Source-preserving request, proposal, or question:**

> Indeed the accept RPC flow has validation inside the cmd handler, so it’s protected. Here, this endpoint is read-only so we don’t have that protection. And data might be off if the RPC already accepted or cancelled \(plan TAA might have already moved\).
> 
> I guess it’s ok for now, as FE only calls this endpoint for the ones we return in RPC list endpoint.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Read endpoint lacks acceptance-handler protection; source tolerates this under current FE calling convention.

**Evidence:** anon-2.jsonl:1957 · comment 430310387 · PR 6868 · 2023-09-25

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:1957 · comment 430310387 · PR 6868 · 2023-09-25

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +  override def getRecommendedPortfolioChangesSummary(planId: UUID, requestId: UUID, displayCcy: CurrencyUnit): Future[RecommendedPortfolioChangesSummaryDto] = {
> +    for {
> +      rebalanceRequest <- findRebalanceRequest(planId, requestId)
> +      customerId = rebalanceRequest.customerId
> +      goalId = rebalanceRequest.goalId
> +      tradingAccountType = rebalanceRequest.tradingAccountType

## A3-0148 — MV-before-plan-topic race creates planProfile with wrong planCcy; remove early creation

**Source stance:** observed-defect

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/PlanTimeSeriesTopicSubscriber.scala; PR: [INV-2014] feat(voucher)(charge): Support discount + tax simulation in fee query endpoint

**Concern stated in the source:** Bug here causing planProfile in charge having wrong planCcy if somehow MV arrives before planProfile is created via kafka from plan topic.

Removed this code completely to avoid race condition.

**Source-preserving request, proposal, or question:**

> Bug here causing planProfile in charge having wrong planCcy if somehow MV arrives before planProfile is created via kafka from plan topic.
> 
> Removed this code completely to avoid race condition. PlanProfile will be eventually created, and here we simply need a goalType

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1967 · comment 431835256 · PR 7042 · 2023-09-29

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/PlanTimeSeriesTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:1967 · comment 431835256 · PR 7042 · 2023-09-29

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/PlanTimeSeriesTopicSubscriber.scala`

**Explicit source context (hunk):**

> )
>    }
>  
> -  private def getGoalTypeMayBeInitPlanProfile(d: DailyMarketValueDto, noCache: Boolean, goalId: UUID, planId: UUID) = {
> +  private def queryGoalType(d: DailyMarketValueDto, noCache: Boolean, goalId: UUID, planId: UUID) = {
>      val maybeFromCache = cache.getIfPresent(goalId)
> -    val goalTypeFut = if (!noCache && maybeFromCache.isDefined) {
> -      Future.successful(maybeFromCache.get)
> -    } else {
> -      for {
> -        maybePlanProfile <- refProvider.getFeeManagerEntity(planId).ask(GetPlanProfileCmd(_))
> -        goalType <- if (maybePlanProfile.isEmpty || maybePlanProfile.get.targetPortfolio.isEmpty) {
> -          for {
> -            goal <- goalService.getGoalById(goalId).in

## A3-0150 — Voucher wallet calculation needs full GetVoucherWalletStateCmd; entity load is bottleneck

**Source stance:** explanation

**Context:**

> voucher-impl/src/main/scala/com/endowus/silver/voucher/impl/entities/voucherWallet/VoucherWalletEntity.scala; PR: [INV-2014] feat(voucher)(charge): Support discount + tax simulation in fee query endpoint

**Source-preserving request, proposal, or question:**

> Ah we don’t have existing adequate readside for this. Will need to return whole state via `GetVoucherWalletStateCmd` to perform this calculation outside.
> 
> However, calculation itself is very simple, and in memory. The bottleneck would still be loading the entity itself.
> 
> Plus, we do this at customer level, not at plan level, so I think should be ok.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1969 · comment 432267560 · PR 7042 · 2023-10-02

Source path: `voucher-impl/src/main/scala/com/endowus/silver/voucher/impl/entities/voucherWallet/VoucherWalletEntity.scala`

**Evidence:** anon-2.jsonl:1969 · comment 432267560 · PR 7042 · 2023-10-02

Source path: `voucher-impl/src/main/scala/com/endowus/silver/voucher/impl/entities/voucherWallet/VoucherWalletEntity.scala`

**Explicit source context (hunk):**

> +    Effect.persist[Event, State](events.toList).thenAck(cmd.replyTo)
> +  }
> +
> +  def handleSimulateDiscountCmd(entityId: EntityId, cmd: SimulateDiscountCmd, state: VoucherWalletState): Persist = {
> +    if (state.rewardedVouchers.isEmpty || cmd.requests.isEmpty) {
> +      return Effect.replySuccess(cmd.replyTo)(SimulatedDiscounts(List()))
> +    }

## A3-0155 — RebalanceMsgLogicImpl.scala: Yea should be correct I think. If deletedAt is present, it is deleted

**Source stance:** explanation

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/subscriber/impl/RebalanceMsgLogicImpl.scala; PR: Feat/INV-1972 deleted orderv2 transaction

**Source-preserving request, proposal, or question:**

> Yea should be correct I think. If deletedAt is present, it is deleted

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:1974 · comment 431717546 · PR 7040 · 2023-09-29

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/subscriber/impl/RebalanceMsgLogicImpl.scala`

## A3-0176 — InstrumentCommands.scala: This cmd actually feels off.. we shouldn’t need to check this in ServiceLogic later, just let the other cmd handler does the check?

**Source stance:** suggestion

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentCommands.scala; PR: Resolve INV-1797: Instrument entity v2 initial work

**Source-preserving request, proposal, or question:**

> This cmd actually feels off.. we shouldn’t need to check this in ServiceLogic later, just let the other cmd handler does the check?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1995 · comment 430325451 · PR 6760 · 2023-09-25

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentCommands.scala`

**Evidence:** anon-2.jsonl:1995 · comment 430325451 · PR 6760 · 2023-09-25

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentCommands.scala`

**Explicit source context (hunk):**

> +    implicit def format(implicit system: ActorSystem[_]): Format[GetInstrumentCmd] = Json.format
> +  }
> +
> +  case class CreateInstrumentCmd(instrument: BaseInstrument, replyTo: ActorRef[StatusReply[InstrumentReply]]) extends InstrumentCmd
> +
> +  object CreateInstrumentCmd {
> +    implicit def format(implicit system: ActorSystem[_], region: SilverRegion): Format[CreateInstrumentCmd] = Json.format

## A3-0177 — TypedInstrumentEventsHandler.scala: If simple enough, I think we can just put in the entity. Only those cmd handlers that have a lot of logic then we can split out to aid readability.

**Source stance:** suggestion

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/TypedInstrumentEventsHandler.scala; PR: Resolve INV-1797: Instrument entity v2 initial work

**Source-preserving request, proposal, or question:**

> If simple enough, I think we can just put in the entity. Only those cmd handlers that have a lot of logic then we can split out to aid readability.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:1996 · comment 430327821 · PR 6760 · 2023-09-25

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/TypedInstrumentEventsHandler.scala`

## A3-0191 — InvestmentTransactionV2Transformer.scala: `SUBMITTED_INTERNALLY_AND_PENDING_EXTERNAL_BROKER_SUBMISSION` should have orders already?

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/transformers/InvestmentTransactionV2Transformer.scala; PR: Feat/INV-1972 transaction migrator processor

**Source-preserving request, proposal, or question:**

> `SUBMITTED_INTERNALLY_AND_PENDING_EXTERNAL_BROKER_SUBMISSION` should have orders already?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2011 · comment 426648814 · PR 6863 · 2023-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/transformers/InvestmentTransactionV2Transformer.scala`

**Evidence:** anon-2.jsonl:2011 · comment 426648814 · PR 6863 · 2023-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/transformers/InvestmentTransactionV2Transformer.scala`

**Explicit source context (hunk):**

> +
> +  val investmentService: InvestmentService
> +
> +  def handleInvestmentTransaction(transaction: Transaction, eventTimestamp: ZonedDateTime): Future[InvestmentTransaction] = {
> +    for {
> +      investmentData <- investmentService
> +        .findInvestmentRequestById(transaction.planId.get, transaction.transactionId)

## A3-0192 — InvestmentTransactionV2Transformer.scala: patch will blindly copy and toV2Order will set status according to assumedAt/confirmedAt… so we will have assumed order here even if it’s still pendin

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/transformers/InvestmentTransactionV2Transformer.scala; PR: Feat/INV-1972 transaction migrator processor

**Source-preserving request, proposal, or question:**

> patch will blindly copy and toV2Order will set status according to assumedAt/confirmedAt… so we will have assumed order here even if it’s still pending status?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2012 · comment 426649156 · PR 6863 · 2023-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/transformers/InvestmentTransactionV2Transformer.scala`

**Evidence:** anon-2.jsonl:2012 · comment 426649156 · PR 6863 · 2023-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/transformers/InvestmentTransactionV2Transformer.scala`

**Explicit source context (hunk):**

> +          shouldFallbackOn = {
> +            case _: NotFound => true
> +            case _ => false
> +          },
> +          futFallback = for {
> +            planInvestments <- investmentService.findInvestmentRequestsForPlan(transaction.planId.get).invoke()
> +            investmentData = planInvestments.find(_.investmentRequestId == transaction.transactionId).getOrElse(

## A3-0195 — RedemptionTransactionV2Transformer.scala: Submitted internally should have orders?

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/transformers/RedemptionTransactionV2Transformer.scala; PR: Feat/INV-1972 transaction migrator processor

**Source-preserving request, proposal, or question:**

> Submitted internally should have orders?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2016 · comment 426655305 · PR 6863 · 2023-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/transformers/RedemptionTransactionV2Transformer.scala`

**Evidence:** anon-2.jsonl:2016 · comment 426655305 · PR 6863 · 2023-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/transformers/RedemptionTransactionV2Transformer.scala`

**Explicit source context (hunk):**

> +        ccy = transaction.ccy,
> +        createdAt = transaction.createdAt,
> +        customerId = transaction.customerId,
> +        tradingAccountType = transaction.tradingAccountType,
> +        goalId = transaction.goalId.get,
> +        planId = transaction.planId.get,
> +        recurringTransactionId = transaction.recurringTransactionId,

## A3-0206 — CustomerTransactionMigrationEventProcessor.scala: Yea this one is purely just to capture the requestedBy/reason - which helps to explain these manual override if we have to dig in future. If we don’t 

**Source stance:** explanation

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/CustomerTransactionMigrationEventProcessor.scala; PR: Feat/INV-1972 transaction migrator processor

**Source-preserving request, proposal, or question:**

> Yea this one is purely just to capture the requestedBy/reason - which helps to explain these manual override if we have to dig in future.
> 
> If we don’t want to look up entity, we can always add a command to override without state \(or make it optional in current cmd\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2027 · comment 428086048 · PR 6863 · 2023-09-18

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/CustomerTransactionMigrationEventProcessor.scala`

**Evidence:** anon-2.jsonl:2027 · comment 428086048 · PR 6863 · 2023-09-18

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/CustomerTransactionMigrationEventProcessor.scala`

**Explicit source context (hunk):**

> +        .map(_.transaction)
> +      transactionV2 <- convertTransaction(transaction, eventTimestamp)
> +      res <- refProvider.getTransactionEntityRef(transaction.transactionId)
> +        .ask(ForceOverrideTransactionCmd(
> +          _,
> +          transaction = transactionV2,
> +          expectedExistingTransaction = existingTransaction,

## A3-0228 — DetectExpiringRecurringInvestmentCmdHandler.scala: Why don’t we just send the communication directly from the scheduler? I’m thinking this is really not an event for GoalEntity - no logic in cmd handle

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/DetectExpiringRecurringInvestmentCmdHandler.scala; PR: [EN-1992] Add support for recurring investment expiring communications

**Source-preserving request, proposal, or question:**

> Why don’t we just send the communication directly from the scheduler? I’m thinking this is really not an event for GoalEntity - no logic in cmd handler, no state changes in entity…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2051 · comment 420897481 · PR 6715 · 2023-08-21

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/handlers/DetectExpiringRecurringInvestmentCmdHandler.scala`

## A3-0235 — Expiring-schedule Kafka lag/replay must not notify a replacement schedule

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringInvestmentScheduleManager.scala; PR: [EN-1992] Add support for recurring investment expiring communications

**Source-preserving request, proposal, or question:**

> Should we validate if schedule is still expiring here, before sending comm? In case the we kafka messages got stuck too long / replayed somehow, and queried plan here actually has another schedule?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2058 · comment 424829675 · PR 6715 · 2023-09-05

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringInvestmentScheduleManager.scala`

**Evidence:** anon-2.jsonl:2058 · comment 424829675 · PR 6715 · 2023-09-05

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringInvestmentScheduleManager.scala`

**Explicit source context (hunk):**

> +
> +  def publishDailyPlanRecurringInvestmentScheduleExpiredTriggerMsg(overrideExecuteDate: Option[LocalDate]): Future[Done] = {
> +    val executeDate = overrideExecuteDate.getOrElse(dateTimeProvider.localDateNow)
> +
> +    logger.logTime(s"streaming expired recurring investment schedules") {
> +      planRecurringInvestmentScheduleJdbcRepository
> +        .streamRecurringInvestmentSchedulesByExpiredOnDate(

## A3-0244 — Idempotent command permits bounded AskTimeout retry

**Source stance:** explanation

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringInvestmentScheduleManager.scala; PR: [EN-2017] Add support for recurring investment expired removal

**Source-preserving request, proposal, or question:**

> This cmd should be idempotent so it’s safe to retry a few times before giving up. Helps us avoid toil on transient issues like AskTimeout

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2067 · comment 424832834 · PR 6804 · 2023-09-05

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringInvestmentScheduleManager.scala`

**Evidence:** anon-2.jsonl:2067 · comment 424832834 · PR 6804 · 2023-09-05

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/managers/BasePlanRecurringInvestmentScheduleManager.scala`

**Explicit source context (hunk):**

> +    planId: UUID,
> +    schedule: RecurringTransactionSchedule
> +  ): Future[Done] = {
> +    FutureUtils
> +      .futureWithRetry(
> +        fut = for {
> +          _ <- refProvider

## A3-0257 — RecurringInvestmentScheduleJdbcEventProcessor.scala: `upsertPlanRecurringInvestmentSchedule` will skip if schedule is None? don’t we need another method to delete in dbHandler?

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala; PR: [EN-2021] Add readside table for plan recurring investment

**Source-preserving request, proposal, or question:**

> `upsertPlanRecurringInvestmentSchedule` will skip if schedule is None? don’t we need another method to delete in dbHandler?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2081 · comment 422183564 · PR 6740 · 2023-08-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2081 · comment 422183564 · PR 6740 · 2023-08-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +        endingOnDate = scheduleEndingOnDate,
> +        recurrenceEndConfig = scheduleEndConfig,
> +        expiredOnDate = getExpiredOnDate(scheduleEndingOnDate, scheduleEndConfig),
> +        updatedAt = updatedAt
> +      )
> +      val resultFut = for {
> +        result <- scheduleJdbcDbHandler.upsert(schedule)

## A3-0263 — Schedule deactivation domain events belong in command/PlanProjection; JDBC writes only

**Source stance:** suggestion

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleHistoryJdbcEventProcessor.scala; PR: [EN-2021] Add readside table for plan recurring investment

**Source-preserving request, proposal, or question:**

> Ideally I’d prefer that either:
> 
> * `DeactivateGoalCmdHandler` should also check and emit `PlanRecurringInvestmentScheduleRemovedEvt`
> * or `PlanProjection` to handle `PlanDeactivatedEvt` and trigger cmd `StopRecurringInvestmentScheduleCmd`
> 
> Then in jdbc projections \(both history and latest\), we just perform purely db update.
> 
> 
> 
> Today we don’t have such logic, and the `RecurringInvestmentProcessor` only cares about active plans, and that’s why it works.
> 
> I think let’s add the above logic, and we can leave the old inactive plans with recurring schedule as is, or run a script to stop them. But let’s not mix the logic here.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Do not mix deactivation/schedule domain behavior into JDBC projections; preserves both command/event alternatives and historical inactive-plan options.

**Evidence:** anon-2.jsonl:2087 · comment 422617963 · PR 6740 · 2023-08-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleHistoryJdbcEventProcessor.scala`

> Ideally I’d prefer that either:
> 
> * `DeactivateGoalCmdHandler` should also check and emit `PlanRecurringInvestmentScheduleRemovedEvt`
> * or `PlanProjection` to handle `PlanDeactivatedEvt` and trigger cmd `StopRecurringInvestmentScheduleCmd`
> 
> Then in jdbc projections \(both history and latest\), we just perform purely db update.
> 
> ‌
> 
> Today we don’t have such logic, and the `RecurringInvestmentProcessor` only cares about active plans, and that’s why it works.
> 
> I think let’s add the above logic, and we can leave the old inactive plans with recurring schedule as is, or run a script to stop them. But let’s not mix the logic here.
> 
> ‌

## A3-0271 — RecurringInvestmentScheduleHelper.scala: This is a helper method. IMO we shouldn’t use State here unless we need data from it.

**Source stance:** suggestion

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/RecurringInvestmentScheduleHelper.scala; PR: More recurring cmd processors schedulers

**Source-preserving request, proposal, or question:**

> This is a helper method. IMO we shouldn’t use State here unless we need data from it.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2095 · comment 419092359 · PR 6558 · 2023-08-14

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/RecurringInvestmentScheduleHelper.scala`

**Evidence:** anon-2.jsonl:2095 · comment 419092359 · PR 6558 · 2023-08-14

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/RecurringInvestmentScheduleHelper.scala`

**Explicit source context (hunk):**

> +    * @param pastRequests List of Past InvestmentRequest], this list should from the current State.
> +    * @param recurringSchedule the RecurringInvestmentSchedule
> +    */
> +  def calculateSequenceNumber(pastRequests: List[InvestmentRequest], recurringSchedule: RecurringInvestmentSchedule): Int = {
> +    import com.endowus.silver.commons.utils.TraversableOnceUtils.TraversableOnceExtensions
> +
> +    pastRequests

## A3-0277 — Schedule-update command validates persisted interval and plan/schedule existence under race

**Source stance:** requested-change

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/UpdateNextUpcomingInvestmentDateCmdHandler.scala; PR: More recurring cmd processors schedulers

**Concern stated in the source:** * if plan not found, throw
* if plan.recurringInvestmentSchedule not found, throw
* otherwise, validate against plan.recurringInvestmentSchedule.interval instead of against input cmd.interval

Additionally, we might want to validate state’s interval vs cmd.interval, it’s a possible race condition in which some flow tries to update, and at the same time, customer remove/update the schedule?

**Source-preserving request, proposal, or question:**

> Shouldn’t the cmd handler validate against the interval in state data?
> 
> * if plan not found, throw
> * if plan.recurringInvestmentSchedule not found, throw
> * otherwise, validate against plan.recurringInvestmentSchedule.interval instead of against input cmd.interval
> 
> Additionally, we might want to validate state’s interval vs cmd.interval, it’s a possible race condition in which some flow tries to update, and at the same time, customer remove/update the schedule?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2101 · comment 419109046 · PR 6558 · 2023-08-14

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/UpdateNextUpcomingInvestmentDateCmdHandler.scala`

> Shouldn’t the cmd handler validate against the interval in state data?
> 
> * if plan not found, throw
> * if plan.recurringInvestmentSchedule not found, throw
> * otherwise, validate against plan.recurringInvestmentSchedule.interval instead of against input cmd.interval
> 
> Additionally, we might want to validate state’s interval vs cmd.interval, it’s a possible race condition in which some flow tries to update, and at the same time, customer remove/update the schedule?
> 
> ‌

**Evidence:** anon-2.jsonl:2101 · comment 419109046 · PR 6558 · 2023-08-14

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/UpdateNextUpcomingInvestmentDateCmdHandler.scala`

**Explicit source context (hunk):**

> +    if (state.maybeInvestmentPlan.isEmpty || maybeSchedule.isEmpty) {
> +      return Effect.ack(cmd.replyTo)
> +    }
> +    val schedule = maybeSchedule.get
> +    // Race condition check
> +    val stateInterval = schedule.interval
> +    if (stateInterval != cmd.interval) {

## A3-0323 — Three-MCCY-broker creation: partial success, retry and stale active-account readside

**Source stance:** open-question

**Context:**

> broker-impl/src/main/scala/com/endowus/silver/broker/impl/logic/service/BaseBrokerServiceLogicImpl.scala; PR: [INV-1723]: feat(broker): SG - add create mccy brokers on base broker creation via event processor handler

**Concern stated in the source:** * event processor catches exception and retries
* the flow queries active broker accounts - which might still not return 1st in the list yet due to eventual consistency
* we might invoke `CreateBrokerAccountCmd` again for 1st?

**Source-preserving request, proposal, or question:**

> Thinking out loud… say we are creating 3 mccy brokers, 1st succeeded, 2nd failed due to whatever reason
> 
> * event processor catches exception and retries
> * the flow queries active broker accounts - which might still not return 1st in the list yet due to eventual consistency
> * we might invoke `CreateBrokerAccountCmd` again for 1st? And it seems the cmd handler is not idempotent?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Keep exact three-MCCY-broker partial-success/retry/eventual-readside/non-idempotent-create scenario as an unresolved concern.

**Evidence:** anon-2.jsonl:2148 · comment 419067251 · PR 6580 · 2023-08-14

Source path: `broker-impl/src/main/scala/com/endowus/silver/broker/impl/logic/service/BaseBrokerServiceLogicImpl.scala`

> Thinking out loud… say we are creating 3 mccy brokers, 1st succeeded, 2nd failed due to whatever reason
> 
> * event processor catches exception and retries
> * the flow queries active broker accounts - which might still not return 1st in the list yet due to eventual consistency
> * we might invoke `CreateBrokerAccountCmd` again for 1st? And it seems the cmd handler is not idempotent?
> 
> ‌

## A3-0325 — TAA has four entities/two BQ copies; remove rebalance TAA entity and janitor remaining three

**Source stance:** explanation

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala; PR: [INV-1939] feat(rebalance): Add endpoint to sync rebalance plan state to readside (due to missed events)

**Source-preserving request, proposal, or question:**

> Yes. There are 4 entities having this TAA, only 2 have data in BQ. That’s why we didn’t add to the dashboard last time.
> 
> There are planned tasks to get rid of one useless entity \(TAA entity in rebalance\), and add janitor for the other 3 \(goal, rebalance, trading\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Preserve four TAA entities, two in BQ, intended removal of rebalance TAA entity, janitors for goal/rebalance/trading.

**Evidence:** anon-2.jsonl:2150 · comment 421228601 · PR 6764 · 2023-08-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2150 · comment 421228601 · PR 6764 · 2023-08-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +  override def syncReadSideRebalancePlan(planId: UUID): Future[RebalancePlanDto] = {
> +    for {
> +      maybeRebalancePlan <- refProvider.getPlanRebalancerEntityRef(planId).ask(GetRebalancePlanCmd(_))
> +      result <- maybeRebalancePlan match {
> +        case Some(rebalancePlan) =>
> +          rebalancePlanJdbcRepository

## A3-0363 — RebateDistributionTopicSubscriberV2.scala: Hmm actually `RequestedAmountStatusDetails` should only be used for the initial status, e.g. `CREATED_AND_PENDING_INTERNAL_BROKER_SUBMISSION` / `PROCE

**Source stance:** requested-change

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RebateDistributionTopicSubscriberV2.scala; PR: Feat/INV-1866 rebate v2 model

**Source-preserving request, proposal, or question:**

> Hmm actually `RequestedAmountStatusDetails` should only be used for the initial status, e.g. `CREATED_AND_PENDING_INTERNAL_BROKER_SUBMISSION` / `PROCESSING` \(fxwallet\). Anything after that should be `PendingAmountStatusDetails` or `PendingOrdersStatusDetails`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2189 · comment 419083312 · PR 6687 · 2023-08-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RebateDistributionTopicSubscriberV2.scala`

**Evidence:** anon-2.jsonl:2189 · comment 419083312 · PR 6687 · 2023-08-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RebateDistributionTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> +      val statusDetails = PendingAmountStatusDetails(
> +        transactionStatus = TransactionStatus.SUBMITTED_EXTERNALLY_AND_PENDING_SETTLEMENT,
> +        requestedAmount = msg.distributedRebateAmount,
> +        requestedAt = msg.createdAt
> +      )
> +      val transaction = createRebateTransaction(
> +        rebateRequestId = msg.rebateRequestId,

## A3-0365 — Requested-state submission statuses: remove unused external, preserve existing internal if prod data

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/TransactionTypes.scala; PR: Feat/INV-1866 rebate v2 model

**Concern stated in the source:** Ideally I would want to remove submitted-internally status from this state as well, cuz it should already be pending status.

**Source-preserving request, proposal, or question:**

> WDYT about removing this submitted-externally status in Requested state?
> 
> Ideally I would want to remove submitted-internally status from this state as well, cuz it should already be pending status.
> 
> Looking at usage, looks like:
> 
> * no flow is using submitted-externally status here yet, should be safe to remove
> * `WithdrawalRequestAcceptedMsg` is using submitted-internally status in Requested state
> 
>     * I suppose we should have put it as Pending state
>     * Can we check in prod if we have withdrawal txn yet? If yes \(likely\), then I guess too late, and we can keep submitted-internally here

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- External-submission status appears unused; internal-submission removal depends on checking production withdrawal transactions, with compatibility retention if present.

**Evidence:** anon-2.jsonl:2191 · comment 419362224 · PR 6687 · 2023-08-15

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/TransactionTypes.scala`

> WDYT about removing this submitted-externally status in Requested state?
> 
> Ideally I would want to remove submitted-internally status from this state as well, cuz it should already be pending status.
> 
> Looking at usage, looks like:
> 
> * no flow is using submitted-externally status here yet, should be safe to remove
> * `WithdrawalRequestAcceptedMsg` is using submitted-internally status in Requested state
> 
>     * I suppose we should have put it as Pending state
>     * Can we check in prod if we have withdrawal txn yet? If yes \(likely\), then I guess too late, and we can keep submitted-internally here
>     
> 
> ‌

**Evidence:** anon-2.jsonl:2191 · comment 419362224 · PR 6687 · 2023-08-15

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/TransactionTypes.scala`

**Explicit source context (hunk):**

> val ApplicableTransactionStatuses: Set[common.TransactionStatus.Value] = Set(
>        TransactionStatus.CREATED_AND_PENDING_INTERNAL_BROKER_SUBMISSION,
>        TransactionStatus.SUBMITTED_INTERNALLY_AND_PENDING_EXTERNAL_BROKER_SUBMISSION,
> -      TransactionStatus.SUBMITTED_EXTERNALLY_AND_PENDING_SETTLEMENT,
>        TransactionStatus.PROCESSING
>      )

## A3-0366 — RebateDistributionTopicSubscriberV2.scala: If we are keeping submitted-internally in Requested state, then I suppose we can let this one be in Requested state :pray:

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RebateDistributionTopicSubscriberV2.scala; PR: Feat/INV-1866 rebate v2 model

**Source-preserving request, proposal, or question:**

> If we are keeping submitted-internally in Requested state, then I suppose we can let this one be in Requested state :pray:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2192 · comment 419362475 · PR 6687 · 2023-08-15

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RebateDistributionTopicSubscriberV2.scala`

**Evidence:** anon-2.jsonl:2192 · comment 419362475 · PR 6687 · 2023-08-15

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RebateDistributionTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> +    case msg: RebateDistributionRequestCreatedMsg if msg.distributedRebateAmount > 0 =>
> +      logger.info(s"Received message that rebate distribution request was created. Plan Id: ${msg.planId}, Rebate request ID: ${msg.rebateRequestId}")
> +      val statusDetails = RequestedAmountStatusDetails(
> +        transactionStatus = TransactionStatus.SUBMITTED_INTERNALLY_AND_PENDING_EXTERNAL_BROKER_SUBMISSION,
> +        requestedAmount = msg.distributedRebateAmount,
> +        requestedAt = msg.createdAt
> +      )

## A3-0389 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Should we also handle `InvestmentPlanDeactivatedEvt`?

**Source stance:** open-question

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> Should we also handle `InvestmentPlanDeactivatedEvt`?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2216 · comment 416497726 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2216 · comment 416497726 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +        ele => insertRequestedDate(ele.event.planId, ele.event.request)
> +      )
> +      .build(READ_SIDE_ID, InvestmentPlanEvt.NumShards, LagomMigrator.tag(InvestmentPlanEvt.Tag), migrator, system)
> +  }
> +
> +  private def createSchedule(planId: UUID, investmentPlanFromEvt: InvestmentPlan): Future[Unit] = {
> +    for {

## A3-0391 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Here we use latest data of investmentPlan, so you may see a schedule created here with an already deactivated plan. Not sure but now I’m thinking if w

**Source stance:** open-question

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> Here we use latest data of investmentPlan, so you may see a schedule created here with an already deactivated plan. Not sure but now I’m thinking if we need the 3 timestamp fields at plan level at all?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2218 · comment 416500395 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2218 · comment 416500395 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +              planUpdatedAt = investmentPlanFromEvt.updatedAt,
> +              recurringAmount = investmentPlanFromEvt.recurringInvestmentSchedule.map(_.investmentAmount).get,
> +              recurringInterval = investmentPlanFromEvt.recurringInvestmentSchedule.map(_.interval).get,
> +              startingDate = investmentPlanFromEvt.recurringInvestmentSchedule.map(_.startingFrom).get,
> +              endingDate = None,
> +              requestedDates = List()
> +            )

## A3-0398 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Actually, here you should use the `recurringInvestmentSchedule` inside the investmentPlan of the event, instead of fetching latest from entity Also, i

**Source stance:** requested-change

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> Actually, here you should use the `recurringInvestmentSchedule` inside the investmentPlan of the event, instead of fetching latest from entity
> 
> Also, if we store plan level fields, you still fetch from entity for every `upsertSchedule` call

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2225 · comment 416509831 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2225 · comment 416509831 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +              planUpdatedAt = investmentPlanFromEvt.updatedAt,
> +              recurringAmount = investmentPlanFromEvt.recurringInvestmentSchedule.map(_.investmentAmount).get,
> +              recurringInterval = investmentPlanFromEvt.recurringInvestmentSchedule.map(_.interval).get,
> +              startingDate = investmentPlanFromEvt.recurringInvestmentSchedule.map(_.startingFrom).get,
> +              endingDate = None,
> +              requestedDates = List()
> +            )

## A3-0402 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: `MakeRecurringInvestmentCmdHandler` set correct reason. Only `InvestOnceCmdHandler` overrides to initial investment if first one

**Source stance:** explanation

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> `MakeRecurringInvestmentCmdHandler` set correct reason. Only `InvestOnceCmdHandler` overrides to initial investment if first one

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2229 · comment 416534116 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2229 · comment 416534116 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +
> +  private def insertRequestedDate(planId: UUID, investmentRequest: InvestmentRequest): Future[Unit] = {
> +    for {
> +      _ <- if (investmentRequest.reason == InvestmentReason.RECURRING_INVESTMENT) {
> +        investmentScheduleActivePeriodJdbcRepository.insertRequestedDateByPlanId(planId, investmentRequest.createdAt)
> +      } else {
> +        Future.successful()

## A3-0403 — UpdateCustomerPreferencesCmdHandler.scala: Requirement as of now yeah… but I’m asking if it even makes sense to block this if we already block at rebalance triggering side

**Source stance:** open-question

**Context:**

> customer-impl/src/main/scala/com/endowus/silver/customer/impl/customer/handlers/impls/UpdateCustomerPreferencesCmdHandler.scala; PR: [INV-1840] feat(customer)(rebalance): Block auto-rebalance for suspended customers

**Source-preserving request, proposal, or question:**

> Requirement as of now yeah… but I’m asking if it even makes sense to block this if we already block at rebalance triggering side

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source row2231 explicitly clarifies actual triggering in breach logic rather than this preferences configuration. The question does not establish that suspended-customer checks belong in both places.

**Evidence:** anon-2.jsonl:2230 · comment 416505087 · PR 6636 · 2023-08-03

Source path: `customer-impl/src/main/scala/com/endowus/silver/customer/impl/customer/handlers/impls/UpdateCustomerPreferencesCmdHandler.scala`

**Evidence:** anon-2.jsonl:2230 · comment 416505087 · PR 6636 · 2023-08-03

Source path: `customer-impl/src/main/scala/com/endowus/silver/customer/impl/customer/handlers/impls/UpdateCustomerPreferencesCmdHandler.scala`

**Explicit source context (hunk):**

> throw CustomerSvcException(s"Unable to process UpdateCustomerPreferencesCmd - customer [$entityId] does not exist]", CustomerSvcErrorType.CUSTOMER_DOES_NOT_EXIST)
>      )
>  
> +    if (customer.status == CustomerStatus.SUSPENDED && cmd.preferences.autoRebalancingEnabled.contains(true)) {
> +      throw CustomerSvcException(
> +        s"Unable to enable auto-rebalance config - customer [$entityId] is suspended",
> +        CustomerSvcErrorType.INVALID_UPDATE_ATTEMPT

## A3-0406 — SgServiceLogicImpl.scala: As of now, we do not support deactivating individual plans under a goal. All plans of same goal must be deactivated together. But this might change in

**Source stance:** explanation

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala; PR: Feat/INV-1633/goal perf across risk targets

**Source-preserving request, proposal, or question:**

> As of now, we do not support deactivating individual plans under a goal. All plans of same goal must be deactivated together. But this might change in future.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2235 · comment 409387842 · PR 6389 · 2023-07-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2235 · comment 409387842 · PR 6389 · 2023-07-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +        case esgProduct: EsgProductDto => AdvisoryTag.ESG
> +        case factorsProduct: FactorsProductDto => AdvisoryTag.FACTORS
> +        case _ => throw BadRequest(s"[calculateGoalPerformancesAcrossRelatedRiskDrivenPortfolios] Unsupported productLineAndIntent=[${product}]")
> +      }
> +    }
> +    def getPlanMarketValues (plans: List[PlanDto]):  Future[Map[UUID, MarketValueDto]] = {
> +      val planIdsString = plans.map(_.planId.toString).mkString(",")

## A3-0407 — SgServiceLogicImpl.scala: This will return empty if goal is inactive. So maybe check that first. Or handle empty validPlans here

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala; PR: Feat/INV-1633/goal perf across risk targets

**Source-preserving request, proposal, or question:**

> This will return empty if goal is inactive. So maybe check that first. Or handle empty validPlans here

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2236 · comment 409387939 · PR 6389 · 2023-07-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2236 · comment 409387939 · PR 6389 · 2023-07-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/SgServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +        case esgProduct: EsgProductDto => AdvisoryTag.ESG
> +        case factorsProduct: FactorsProductDto => AdvisoryTag.FACTORS
> +        case _ => throw BadRequest(s"[calculateGoalPerformancesAcrossRelatedRiskDrivenPortfolios] Unsupported productLineAndIntent=[${product}]")
> +      }
> +    }
> +    def getPlanMarketValues (plans: List[PlanDto]):  Future[Map[UUID, MarketValueDto]] = {
> +      val planIdsString = plans.map(_.planId.toString).mkString(",")

## A3-0428 — package.scala: I think it’s cleaner to create new cmd, mark old one deprecated. Once we switch the usage completely, it’s simple to remove the old cmd whenever we to

**Source stance:** suggestion

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/ces/commands/package.scala; PR: Feat/INV-1600/productline cash smart goal create and modify

**Source-preserving request, proposal, or question:**

> Yeah I think it’s cleaner to create new cmd, mark old one deprecated. Once we switch the usage completely, it’s simple to remove the old cmd whenever we touch the service again.
> 
> Chance of running into ’s example is low, but not non-zero. Once we hit that case, it might be troublesome to deal with, especially for FundSmart

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- New cmd+deprecation proposal preserves low-probability but nonzero FundSmart compatibility risk, not universal mandatory command versioning.

**Evidence:** anon-2.jsonl:2258 · comment 405844795 · PR 6115 · 2023-06-23

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/ces/commands/package.scala`

> Yeah I think it’s cleaner to create new cmd, mark old one deprecated. Once we switch the usage completely, it’s simple to remove the old cmd whenever we touch the service again.
> 
> Chance of running into

**Evidence:** anon-2.jsonl:2258 · comment 405844795 · PR 6115 · 2023-06-23

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/ces/commands/package.scala`

> ’s example is low, but not non-zero. Once we hit that case, it might be troublesome to deal with, especially for FundSmart

## A3-0445 — package.scala: AFAICS, all manual orders we support so far are all amount-based orders. I wanted to keep this request for all trades, and let the cmd handler decide 

**Source stance:** explanation

**Context:**

> trading-api/src/main/scala/com/endowus/silver/trading/api/requests/package.scala; PR: [INV-1719] feat(charge)(trading): Fee charge leakage

**Source-preserving request, proposal, or question:**

> AFAICS, all manual orders we support so far are all amount-based orders. I wanted to keep this request for all trades, and let the cmd handler decide how much it can support \(which we only allow fee redemption trade as of now\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2277 · comment 412640428 · PR 6463 · 2023-07-19

Source path: `trading-api/src/main/scala/com/endowus/silver/trading/api/requests/package.scala`

**Evidence:** anon-2.jsonl:2277 · comment 412640428 · PR 6463 · 2023-07-19

Source path: `trading-api/src/main/scala/com/endowus/silver/trading/api/requests/package.scala`

**Explicit source context (hunk):**

> +    require(!requestBy.isBlank, "requestedBy cannot be blank.")
> +    require(!reason.isBlank, "reason cannot be blank.")
> +    require(manualOrders.nonEmpty, "manualOrders cannot be empty")
> +    require(manualOrders.values.forall(_ > 0), "manualOrders cannot contain non-positive amount")
> +  }
> +
> +  object UpdateTradeWithManualOrdersRequest {

## A3-0446 — UpdateTradeWithManualOrdersCmdHandler.scala: these basic validations I just follow existing code. It’s not clear why in some places we reply ack, reply message or reply error. Note that reply err

**Source stance:** explanation

**Context:**

> trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateTradeWithManualOrdersCmdHandler.scala; PR: [INV-1719] feat(charge)(trading): Fee charge leakage

**Concern stated in the source:** Note that reply error will require an exception - which we know will cause serdes issue \(until we come up with standard approach on svc exception vs internal exception\).

**Source-preserving request, proposal, or question:**

> yeah these basic validations I just follow existing code. It’s not clear why in some places we reply ack, reply message or reply error.
> 
> Note that reply error will require an exception - which we know will cause serdes issue \(until we come up with standard approach on svc exception vs internal exception\). I’m not changing this bit in this PR yet, just to limit down the scope.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Reply ack/message/error convention and service-vs-internal-exception serdes remain unresolved; source explicitly avoids changing them in this PR.

**Evidence:** anon-2.jsonl:2278 · comment 412641747 · PR 6463 · 2023-07-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateTradeWithManualOrdersCmdHandler.scala`

> yeah these basic validations I just follow existing code. It’s not clear why in some places we reply ack, reply message or reply error.
> 
> Note that reply error will require an exception - which we know will cause serdes issue \(until we come up with standard approach on svc exception vs internal exception\). I’m not changing this bit in this PR yet, just to limit down the scope.
> 
> ‌

**Evidence:** anon-2.jsonl:2278 · comment 412641747 · PR 6463 · 2023-07-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateTradeWithManualOrdersCmdHandler.scala`

**Explicit source context (hunk):**

> +    val taa = state.maybeTaa.get
> +
> +    if (trade.status != TradeStatus.WAITING_FOR_MARKET_DATA) {
> +      return Effect.replyMessage(cmd.replyTo)(s"$here - Trade [${cmd.tradeId}] is unable to handle UpdateTradeWithManualOrdersCmd as it is not in the [${TradeStatus.WAITING_FOR_MARKET_DATA}] status, it is in [${trade.status}]")
> +    }
> +
> +    tryGenerateManualOrders(profile, trade, taa, state, cmd) match {

## A3-0447 — Empty generated orders before/after Lagom removal: log+Done with no event preserves outcome

**Source stance:** explanation

**Context:**

> trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateMarketDataCmdHandler.scala; PR: [INV-1719] feat(charge)(trading): Fee charge leakage

**Source-preserving request, proposal, or question:**

> yeah I deliberately changed this code a bit as existing code is misleading, but effective behavior is same.
> 
> 
> 
> Existing code before Lagom removal:
> 
> * If generated order is empty, throw exception
> * Catch exception, log error and reply Done without any events
> 
> 
> 
> Existing code after Lagom removal:
> 
> * If generated order is empty, reply error
> * Catch exception is bypassed
> * Exception is caught in `PlanTraderEventProcessor#handleMarketDataRequestedEvt` , log error and return Done
> 
> 
> 
> New logic:
> 
> * If generated order is empty, log error and reply Done without any event

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Three historical branches preserve pre-removal throw/catch+Done, post-removal replyError caught in event processor, new local log+Done without event.

**Evidence:** anon-2.jsonl:2279 · comment 412644210 · PR 6463 · 2023-07-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateMarketDataCmdHandler.scala`

> yeah I deliberately changed this code a bit as existing code is misleading, but effective behavior is same.
> 
> ‌
> 
> Existing code before Lagom removal:
> 
> * If generated order is empty, throw exception
> * Catch exception, log error and reply Done without any events
> 
> ‌
> 
> Existing code after Lagom removal:
> 
> * If generated order is empty, reply error
> * Catch exception is bypassed
> * Exception is caught in `PlanTraderEventProcessor#handleMarketDataRequestedEvt` , log error and return Done
> 
> ‌
> 
> New logic:
> 
> * If generated order is empty, log error and reply Done without any event
> 
> ‌

**Evidence:** anon-2.jsonl:2279 · comment 412644210 · PR 6463 · 2023-07-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateMarketDataCmdHandler.scala`

**Explicit source context (hunk):**

> settlementConfirmedAmount = Some(reservedAmount),
>            settlementConfirmedAt = Some(currentTime)
>          )
> -        events += TradeSettlementConfirmedEvt(planProfile = profile, trade = settledTrade, forcedRepublish = None)
> -        return Effect.persist(events.toList).thenAck(cmd.replyTo)
> +        return Effect
> +          .persist[Event, State](TradeSettlementConfirmedEvt(planProfile = profile, trade = settledTrade, forcedRepublish = None))
> +          .thenAck(cmd.replyTo)
>        }
>      }
>  
> -    try {
> -      val generatedOrders = if (trade.buySell == BuySell.BUY) {
> -        if (trade.cashReservations.isEmpty) {
> -          logger.error(
> -            s"PlanTraderEntity [$enti

## A3-0448 — UpdateMarketDataCmdHandler.scala: I extract the event logic for fee to separate method so if we enter here, don’t need to worry about fee anymore

**Source stance:** explanation

**Context:**

> trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateMarketDataCmdHandler.scala; PR: [INV-1719] feat(charge)(trading): Fee charge leakage

**Source-preserving request, proposal, or question:**

> I extract the event logic for fee to separate method so if we enter here, don’t need to worry about fee anymore

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2281 · comment 412646547 · PR 6463 · 2023-07-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateMarketDataCmdHandler.scala`

**Evidence:** anon-2.jsonl:2281 · comment 412646547 · PR 6463 · 2023-07-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateMarketDataCmdHandler.scala`

**Explicit source context (hunk):**

> +      )
> +    }
> +
> +    if (validOrders.exists(order => order.buySell == BuySell.SELL && !order.isUnitBasedOrder)) {
> +      logger.warn(
> +        s"PlanTraderEntity [$entityId] generated sell orders that are not unit-based and also not fee charges. Amount-based orders are deprecated and shouldn't be used anymore (except fee charges). " +
> +          s"Trade: ${trade.tradeId}, Orders: ${Json.toJson(validOrders)}"

## A3-0450 — PlanTraderEntityTestForSellFeeCharge.scala: No events mean state will not change right?

**Source stance:** open-question

**Context:**

> trading-impl/src/test/scala/com/endowus/silver/trading/imp/entities/plan/PlanTraderEntityTestForSellFeeCharge.scala; PR: [INV-1719] feat(charge)(trading): Fee charge leakage

**Source-preserving request, proposal, or question:**

> No events mean state will not change right?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2283 · comment 412646982 · PR 6463 · 2023-07-19

Source path: `trading-impl/src/test/scala/com/endowus/silver/trading/imp/entities/plan/PlanTraderEntityTestForSellFeeCharge.scala`

**Evidence:** anon-2.jsonl:2283 · comment 412646982 · PR 6463 · 2023-07-19

Source path: `trading-impl/src/test/scala/com/endowus/silver/trading/imp/entities/plan/PlanTraderEntityTestForSellFeeCharge.scala`

**Explicit source context (hunk):**

> outcome3.reply shouldBe Ack
> -        outcome3.events should have size 1
> -        outcome3.events.head shouldBe an[TradeSettlementConfirmedEvt]
> +        outcome3.events shouldBe empty
> +        outcome3.state.trades.find(_.tradeId == requestSellCmd.stub.tradeId).map(_.status) should contain(TradeStatus.WAITING_FOR_MARKET_DATA)
> +    }

## A3-0451 — replyMessage uses StatusReply.error(String) to avoid Throwable serdes custom type

**Source stance:** explanation

**Context:**

> trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateTradeWithManualOrdersCmdHandler.scala; PR: [INV-1719] feat(charge)(trading): Fee charge leakage

**Source-preserving request, proposal, or question:**

> replyMessage is a special replyError that will serdes properly and we don’t need make up some custom error type
> 
> ```
>     def replyMessage[R, E, S](replyTo: ActorRef[StatusReply[R]])(message: String): ReplyEffect[E, S] =
>       Effect.none[E, S].thenReply[StatusReply[R]](replyTo)(_ => StatusReply.error[R](message))
> 
>     def replyError[R, E, S](replyTo: ActorRef[StatusReply[R]])(e: Throwable): ReplyEffect[E, S] =
>       Effect.none[E, S].thenReply[StatusReply[R]](replyTo)(_ => StatusReply.error[R](e))
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2284 · comment 412687380 · PR 6463 · 2023-07-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateTradeWithManualOrdersCmdHandler.scala`

> replyMessage is a special replyError that will serdes properly and we don’t need make up some custom error type
> 
> ```
>     def replyMessage[R, E, S](replyTo: ActorRef[StatusReply[R]])(message: String): ReplyEffect[E, S] =
>       Effect.none[E, S].thenReply[StatusReply[R]](replyTo)(_ => StatusReply.error[R](message))
> 
>     def replyError[R, E, S](replyTo: ActorRef[StatusReply[R]])(e: Throwable): ReplyEffect[E, S] =
>       Effect.none[E, S].thenReply[StatusReply[R]](replyTo)(_ => StatusReply.error[R](e))
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2284 · comment 412687380 · PR 6463 · 2023-07-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateTradeWithManualOrdersCmdHandler.scala`

**Explicit source context (hunk):**

> +    // Only support fee redemption trade as of now
> +    val maybeTrade = state.trades.find(s => s.tradeId == cmd.tradeId && s.buySell == BuySell.SELL && s.feeChargeRequestId.nonEmpty)
> +    if (maybeTrade.isEmpty) {
> +      return Effect.replyMessage(cmd.replyTo)(s"$here unable to find the fee redemption trade [${cmd.tradeId}]")
> +    }
> +    val trade = maybeTrade.get
> +    val profile = state.maybeProfile.get

## A3-0452 — UpdateTradeWithManualOrdersCmdHandler.scala: I updated to replyMessage here to give immediate error to caller instead of having to check Kibana/Sentry

**Source stance:** explanation

**Context:**

> trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateTradeWithManualOrdersCmdHandler.scala; PR: [INV-1719] feat(charge)(trading): Fee charge leakage

**Source-preserving request, proposal, or question:**

> I updated to replyMessage here to give immediate error to caller instead of having to check Kibana/Sentry

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2285 · comment 412687636 · PR 6463 · 2023-07-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateTradeWithManualOrdersCmdHandler.scala`

**Evidence:** anon-2.jsonl:2285 · comment 412687636 · PR 6463 · 2023-07-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateTradeWithManualOrdersCmdHandler.scala`

**Explicit source context (hunk):**

> +    val taa = state.maybeTaa.get
> +
> +    if (trade.status != TradeStatus.WAITING_FOR_MARKET_DATA) {
> +      return Effect.replyMessage(cmd.replyTo)(s"$here - Trade [${cmd.tradeId}] is unable to handle UpdateTradeWithManualOrdersCmd as it is not in the [${TradeStatus.WAITING_FOR_MARKET_DATA}] status, it is in [${trade.status}]")
> +    }
> +
> +    tryGenerateManualOrders(profile, trade, taa, state, cmd) match {

## A3-0453 — UpdateTradeWithManualOrdersCmdHandler.scala: I’m not changing the `UpdateMarketDataCmdHandler` side as it seems to “expect” it to happen in its info logging ``` (perhaps the events got replayed b

**Source stance:** explanation

**Context:**

> trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateTradeWithManualOrdersCmdHandler.scala; PR: [INV-1719] feat(charge)(trading): Fee charge leakage

**Source-preserving request, proposal, or question:**

> I’m not changing the `UpdateMarketDataCmdHandler` side as it seems to “expect” it to happen in its info logging
> 
> ```
> (perhaps the events got replayed by the event processor)
> ```
> 
> ```
>     if (trade.status != TradeStatus.WAITING_FOR_MARKET_DATA) {
>       logger.info(
>         s"PlanTrader [$entityId] received the market data update for the trade [${cmd.tradeId}] but it is not in the [${TradeStatus.WAITING_FOR_MARKET_DATA}] status, it is in [${trade.status}] so ignoring it... (perhaps the events got replayed by the event processor)"
>       )
>       return Effect.ack(cmd.replyTo)
>     }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- UpdateMarketDataCmdHandler ignored non-WAITING_FOR_MARKET_DATA status before; source intentionally leaves expected replay behavior unchanged.

**Evidence:** anon-2.jsonl:2286 · comment 412688253 · PR 6463 · 2023-07-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateTradeWithManualOrdersCmdHandler.scala`

> I’m not changing the `UpdateMarketDataCmdHandler` side as it seems to “expect” it to happen in its info logging
> 
> ```
> (perhaps the events got replayed by the event processor)
> ```
> 
> ```
>     if (trade.status != TradeStatus.WAITING_FOR_MARKET_DATA) {
>       logger.info(
>         s"PlanTrader [$entityId] received the market data update for the trade [${cmd.tradeId}] but it is not in the [${TradeStatus.WAITING_FOR_MARKET_DATA}] status, it is in [${trade.status}] so ignoring it... (perhaps the events got replayed by the event processor)"
>       )
>       return Effect.ack(cmd.replyTo)
>     }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2286 · comment 412688253 · PR 6463 · 2023-07-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/handlers/UpdateTradeWithManualOrdersCmdHandler.scala`

**Explicit source context (hunk):**

> +    val taa = state.maybeTaa.get
> +
> +    if (trade.status != TradeStatus.WAITING_FOR_MARKET_DATA) {
> +      return Effect.replyMessage(cmd.replyTo)(s"$here - Trade [${cmd.tradeId}] is unable to handle UpdateTradeWithManualOrdersCmd as it is not in the [${TradeStatus.WAITING_FOR_MARKET_DATA}] status, it is in [${trade.status}]")
> +    }
> +
> +    tryGenerateManualOrders(profile, trade, taa, state, cmd) match {

## A3-0458 — WithdrawalTopicSubscriber.scala: Should we go to entity if not found in readside?

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/WithdrawalTopicSubscriber.scala; PR: [INV-1425] feat(report): Added tax details to instrumentTransactionDto and refactor accessFeeTax statement calculation

**Source-preserving request, proposal, or question:**

> Should we go to entity if not found in readside?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2291 · comment 407990288 · PR 6309 · 2023-07-03

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/WithdrawalTopicSubscriber.scala`

## A3-0480 — package.scala: we can just move this method there, instead of state

**Source stance:** suggestion

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/state/package.scala; PR: Release/INV-1396 charge GST

**Source-preserving request, proposal, or question:**

> Maybe we can just move this method there, instead of state

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2314 · comment 409187534 · PR 6378 · 2023-07-06

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/state/package.scala`

## A3-0500 — : Don’t you need an endpoint to trigger the cmd too?

**Source stance:** open-question

**Context:**

> None; PR: Resolve INV-1750: Add cmd to manually update the TAA of the rebalance plan entity.

**Source-preserving request, proposal, or question:**

> Don’t you need an endpoint to trigger the cmd too?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2336 · comment 407561969 · PR 6323 · 2023-06-30

## A3-0502 — RebalancePlanEntityTest.scala: check exactly new new TAA matches what provided in cmd? Also let’s verify the emitted events contain only the TAA updated evt, and nothing else. Do yo

**Source stance:** suggestion

**Context:**

> rebalance-impl/src/test/scala/com/endowus/silver/rebalance/impl/entities/RebalancePlanEntityTest.scala; PR: Resolve INV-1750: Add cmd to manually update the TAA of the rebalance plan entity.

**Source-preserving request, proposal, or question:**

> Maybe check exactly new new TAA matches what provided in cmd?
> 
> Also let’s verify the emitted events contain only the TAA updated evt, and nothing else.
> 
> Do you want to add a few more cases in which the cmd is skipped/rejected when existing state doesn’t allow change TAA?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2338 · comment 407980732 · PR 6323 · 2023-07-03

Source path: `rebalance-impl/src/test/scala/com/endowus/silver/rebalance/impl/entities/RebalancePlanEntityTest.scala`

**Evidence:** anon-2.jsonl:2338 · comment 407980732 · PR 6323 · 2023-07-03

Source path: `rebalance-impl/src/test/scala/com/endowus/silver/rebalance/impl/entities/RebalancePlanEntityTest.scala`

**Explicit source context (hunk):**

> +
> +    val updatedTaa = driver.runCommand(cmd).state.plan.get.currentTaa
> +
> +    originalState.plan.get.currentTaa.instrumentWeights shouldNot equal(updatedTaa.instrumentWeights)
> +  }
>  }

## A3-0505 — d56 fee-withdrawal deletion test: error-before,200-after, reservation/events/DELETED checks

**Source stance:** reported-verification

**Context:**

> None; PR: [TT-2544] fix(broker)(trading): Allow deleting FeeWithdrawal request/transaction

**Source-preserving request, proposal, or question:**

> Tested the below in d56
> 
> ## Existing state
> 
> ### Transaction
> 
> "requestedAmount": 25.78,
> 
> "status": "SUBMITTED_INTERNALLY_AND_PENDING_EXTERNAL_BROKER_SUBMISSION",
> 
> ### TradingAccountEntity
> 
> Cash reservation
> 
> Withdrawal
> 
> ### Broker transaction \(contain many other fee withdrawals\)
> 
> ## Trigger withdrawal request deletion
> 
> Before fix deployment:
> 
> "error_code": "INVALID_TRANSACTION_TYPE"
> 
> After fix deployment: 200 OK
> 
> ![](<url>
> ## State after deletion
> 
> ### Broker transaction \(has deletedAt populated for corresponding `withdrawalRequestId`\)
> 
> "deletedAt": "2023-07-04T21:15:41.445097+08:00[Asia/Singapore]",
> 
> ### TradingAccountEntity
> 
> Cash reservation is deleted from state
> 
> Withdrawal \(deletedAt populated for both `brokerAccountCashWithdrawals` and withdrawalRequest\)
> 
> Events
> 
> ### Transaction
> 
> Fee withdrawal txn is deleted from A&B query. Status is updated to deleted in entity
> 
> "status": "DELETED",
> 
> 
> 
> Events (exact retained source list):
> 
> ```
> CashReservationDeletedEvt
> BrokerAccountCashBalanceUpdatedEvt
> BrokerAccountWithdrawalRequestUpdatedEvt
> CashWithdrawalRequestDeletedEvt
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Reported d56 fee-withdrawal deletion test: before INVALID_TRANSACTION_TYPE; after200; deletedAt on matching withdrawal and nested cash withdrawal, reservation removed, balance-update event emitted, four named events, transaction DELETED and absent A&B. Incidental IDs/account numbers and verbose repeated JSON omitted.
- Repeated test-output/JSON/CLI blocks are omitted; the retained prose and selected exact output-field lines are the evidence. No test outcome beyond those statements is inferred.
- Related source row2342 qualifies the balance claim: d56 cash balance was affected by test setup; only attempted recalculation and the emitted BrokerAccountCashBalanceUpdatedEvt are established, not validated balance arithmetic.

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> Tested the below in d56

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> ‌
> 
> ## Existing state
> 
> ### Transaction

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> "requestedAmount": 25.78,

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> "status": "SUBMITTED_INTERNALLY_AND_PENDING_EXTERNAL_BROKER_SUBMISSION",

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> ### TradingAccountEntity
> 
> Cash reservation

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> Withdrawal

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> ### Broker transaction \(contain many other fee withdrawals\)

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> ‌
> 
> ## Trigger withdrawal request deletion

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> Before fix deployment:

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> "error_code": "INVALID_TRANSACTION_TYPE"

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> After fix deployment: 200 OK
> 
> ![](<url>
> ## State after deletion
> 
> ### Broker transaction \(has deletedAt populated for corresponding `withdrawalRequestId`\)

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> "deletedAt": "2023-07-04T21:15:41.445097+08:00[Asia/Singapore]",

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> ### TradingAccountEntity
> 
> Cash reservation is deleted from state
> 
> Withdrawal \(deletedAt populated for both `brokerAccountCashWithdrawals` and withdrawalRequest\)

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> Events

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> ### Transaction
> 
> Fee withdrawal txn is deleted from A&B query. Status is updated to deleted in entity

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> "status": "DELETED",

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> ‌

**Evidence:** anon-2.jsonl:2341 · comment 408503098 · PR 6354 · 2023-07-04

> CashReservationDeletedEvt
> BrokerAccountCashBalanceUpdatedEvt
> BrokerAccountWithdrawalRequestUpdatedEvt
> CashWithdrawalRequestDeletedEvt

**Evidence:** anon-2.jsonl:2342 · comment 408504744 · PR 6354 · 2023-07-04

> The cash balance is a bit messed up due to testing in d56, but it did try to recalculate the balance.

## A3-0506 — : The cash balance is a bit messed up due to testing in d56, but it did try to recalculate the balance. The warning in transaction svc about missing fee

**Source stance:** reported-verification

**Context:**

> None; PR: [TT-2544] fix(broker)(trading): Allow deleting FeeWithdrawal request/transaction

**Source-preserving request, proposal, or question:**

> The cash balance is a bit messed up due to testing in d56, but it did try to recalculate the balance.
> 
> The warning in transaction svc about missing feeDetails is what fixed in trading, released today \(this one is old charge\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Cash balance in d56 was affected by testing; only recalculation attempt is asserted. Missing feeDetails warning relates to old charge and separate released trading fix.
- Related source row2341 contains the event/deletion test. This row limits any claim there to attempted balance recalculation; it does not verify the resulting balance amount.

**Evidence:** anon-2.jsonl:2342 · comment 408504744 · PR 6354 · 2023-07-04

## A3-0513 — TriggerThresholdBreachedRebalanceCmdHandler.scala: No you need to extends PlayJsonSerializable for `RebalanceSvcException` `RebalanceSvcException` is a case class, so it has default apply method ``` ca

**Source stance:** requested-change

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/TriggerThresholdBreachedRebalanceCmdHandler.scala; PR: [INV-1303] feat(rebalance): Increase min backoff to 1.5s

**Source-preserving request, proposal, or question:**

> No you need to extends PlayJsonSerializable for `RebalanceSvcException`
> 
> `RebalanceSvcException` is a case class, so it has default apply method
> 
> ```
> case class Foo(....)
> 
> // all these 3 are same
> val foo1 = Foo(...)
> val foo2 = Foo.apply(...)
> val foo3 = new Foo(...)
> ```
> 
> But that has nothing to do with serdes

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2349 · comment 406945346 · PR 6313 · 2023-06-28

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/TriggerThresholdBreachedRebalanceCmdHandler.scala`

**Evidence:** anon-2.jsonl:2349 · comment 406945346 · PR 6313 · 2023-06-28

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/TriggerThresholdBreachedRebalanceCmdHandler.scala`

**Explicit source context (hunk):**

> if (plan != cmd.loadedRebalancePlan) {
>        return Effect.replyError(cmd.replyTo)(
> -        new RebalanceSvcException(s"current plan state is inconsistent with command caller plan state for planId [${plan.planId}] received!",
> +        RebalanceSvcException(s"current plan state is inconsistent with command caller plan state for planId [${plan.planId}] received!",
>            RebalanceSvcErrorType.CONCURRENT_MODIFICATION
>          )
>        )

## A3-0515 — Post-Lagom API contract exception versus actor serializer; goal internal exception pattern unresolved

**Source stance:** explanation

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/TriggerThresholdBreachedRebalanceCmdHandler.scala; PR: [INV-1303] feat(rebalance): Increase min backoff to 1.5s

**Source-preserving request, proposal, or question:**

> Yeah this is where the voodoo happens.
> 
> 
> 
> Before:
> 
> * SvcException extends Lagom TransportException which the Lagom ExceptionSerializer knows how to serdes them. The `LagomServiceExceptionHelper` is extra logic to help avoiding sentry spamming
> * This same exception is also used to throw inside entity/cmdHandler. These can be serdes thanks to `JsonSerializer[AdvisorySvcException]`
> 
> 
> 
> After Lagom removal:
> 
> * SvcException in \*-api module are now intended as API contract only. They are converted to HTTP error via `EndpointResultCompat#mapToApiError`
> * akka serdes now is configured as
> 
> ```
> akka {
>   actor {
>     serializers {
>       play-json = "com.endowus.silver.persistence.serialization.PlayJsonSerializer"
>     }
>     serialization-bindings {
>       "akka.Done" = akka-misc
>       "akka.actor.Address" = akka-misc
>       "akka.remote.UniqueAddress" = akka-misc
>       "com.endowus.silver.persistence.serialization.PlayJsonSerializable" = play-json
>     }
>   }
> }
> ```
> 
> * this is why if we want serdes to work… we need to extends `PlayJsonSerializable` \(all the state/cmd/evt do this\)
> * however, it’s debate-able whether we want to add this to our API contract. You can see none of the services do this, except for goal svc
> 
> 
> 
> Goal svc does it in a subtle way:
> 
> * it creates another `GoalSvcException` inside goal-impl and throw this in entity/cmdHandler
> * this is why serdes works for goal svc \(and only goal svc\)
> * and if such internal GoalSvcException is propagate to http, it converts back to the goal-api GoalSvcException
> 
> ```
>   val ServiceErrorMap: Throwable => Throwable = {
>     case logic.GoalSvcException(message, errorType) => GoalSvcException.toApiError(GoalSvcException(message, errorType))
>     case e: GoalSvcException                        => GoalSvcException.toApiError(e)
>     case e                                          => e
>   }
> ```
> 
> 
> 
> So following goal svc should work - but I’m not sure if this is the right way to do it. Let’s think more before we mass apply this pattern

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Detailed before/after Lagom-removal serdes distinction retained. Goal internal GoalSvcException mapping is a possible model explicitly NOT approved for mass adoption.

**Evidence:** anon-2.jsonl:2351 · comment 407028769 · PR 6313 · 2023-06-28

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/TriggerThresholdBreachedRebalanceCmdHandler.scala`

> Yeah this is where the voodoo happens.
> 
> ‌
> 
> Before:
> 
> * SvcException extends Lagom TransportException which the Lagom ExceptionSerializer knows how to serdes them. The `LagomServiceExceptionHelper` is extra logic to help avoiding sentry spamming
> * This same exception is also used to throw inside entity/cmdHandler. These can be serdes thanks to `JsonSerializer[AdvisorySvcException]`
> 
> ‌
> 
> After Lagom removal:
> 
> * SvcException in \*-api module are now intended as API contract only. They are converted to HTTP error via `EndpointResultCompat#mapToApiError`
> * akka serdes now is configured as
> 
> ```
> akka {
>   actor {
>     serializers {
>       play-json = "com.endowus.silver.persistence.serialization.PlayJsonSerializer"
>     }
>     serialization-bindings {
>       "akka.Done" = akka-misc
>       "akka.actor.Address" = akka-misc
>       "akka.remote.UniqueAddress" = akka-misc
>       "com.endowus.silver.persistence.serialization.PlayJsonSerializable" = play-json
>     }
>   }
> }
> ```
> 
> * this is why if we want serdes to work… we need to extends `PlayJsonSerializable` \(all the state/cmd/evt do this\)
> * however, it’s debate-able whether we want to add this to our API contract. You can see none of the services do this, except for goal svc
> 
> ‌
> 
> Goal svc does it in a subtle way:
> 
> * it creates another `GoalSvcException` inside goal-impl and throw this in entity/cmdHandler
> * this is why serdes works for goal svc \(and only goal svc\)
> * and if such internal GoalSvcException is propagate to http, it converts back to the goal-api GoalSvcException
> 
> ```
>   val ServiceErrorMap: Throwable => Throwable = {
>     case logic.GoalSvcException(message, errorType) => GoalSvcException.toApiError(GoalSvcException(message, errorType))
>     case e: GoalSvcException                        => GoalSvcException.toApiError(e)
>     case e                                          => e
>   }
> ```
> 
> ‌
> 
> So following goal svc should work - but I’m not sure if this is the right way to do it. Let’s think more before we mass apply this pattern

**Evidence:** anon-2.jsonl:2351 · comment 407028769 · PR 6313 · 2023-06-28

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/TriggerThresholdBreachedRebalanceCmdHandler.scala`

**Explicit source context (hunk):**

> if (plan != cmd.loadedRebalancePlan) {
>        return Effect.replyError(cmd.replyTo)(
> -        new RebalanceSvcException(s"current plan state is inconsistent with command caller plan state for planId [${plan.planId}] received!",
> +        RebalanceSvcException(s"current plan state is inconsistent with command caller plan state for planId [${plan.planId}] received!",
>            RebalanceSvcErrorType.CONCURRENT_MODIFICATION
>          )
>        )

## A3-0524 — chargeTopic.scala: There are a few validation in the cmd handler. Essentially we should only allow backfilling if it does not affect final chargeable amount. However, th

**Source stance:** explanation

**Context:**

> charge-api/src/main/scala/com/endowus/silver/charge/api/msg/chargeTopic.scala; PR: [INV-1710] feat(charge): Add endpoint to support back-filling absorbed GST in completed fee charge

**Source-preserving request, proposal, or question:**

> There are a few validation in the cmd handler. Essentially we should only allow backfilling if it does not affect final chargeable amount.
> 
> However, the REST endpoint is specifically created to backfill absorbed tax

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2361 · comment 406980219 · PR 6306 · 2023-06-28

Source path: `charge-api/src/main/scala/com/endowus/silver/charge/api/msg/chargeTopic.scala`

**Evidence:** anon-2.jsonl:2361 · comment 406980219 · PR 6306 · 2023-06-28

Source path: `charge-api/src/main/scala/com/endowus/silver/charge/api/msg/chargeTopic.scala`

**Explicit source context (hunk):**

> implicit val format: Format[FeeChargeRequestDeletedMsg] = Json.format
>  }
>  
> +case class FeeChargeTaxDetailsBackFilledMsg(
> +  year: Int,
> +  quarter: Quarter,
> +  startDate: LocalDate,

## A3-0532 — commands.scala: Just to make sure we don’t wrongly override existing data in case the cmd is called twice, unless the force flag is set \(cuz it will be called via pr

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/commands/commands.scala; PR: [INV-1709] feat(charge): SG charge logic for GST

**Concern stated in the source:** Just to make sure we don’t wrongly override existing data in case the cmd is called twice, unless the force flag is set \(cuz it will be called via projection now\)

**Source-preserving request, proposal, or question:**

> Just to make sure we don’t wrongly override existing data in case the cmd is called twice, unless the force flag is set \(cuz it will be called via projection now\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2371 · comment 405918078 · PR 6283 · 2023-06-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/commands/commands.scala`

**Evidence:** anon-2.jsonl:2371 · comment 405918078 · PR 6283 · 2023-06-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/commands/commands.scala`

**Explicit source context (hunk):**

> finalizedFeeAmountAfterDiscount: BigDecimal,
> -    appliedDiscounts: List[AppliedDiscount]
> +    appliedDiscounts: List[AppliedDiscount],
> +    forceUpdate: Option[Boolean]
>    ) extends FeeManagerCmd
>        with ReplyType[Done]

## A3-0533 — InitiateFeeRedemptionCmdHandler.scala: this is how SG flow works today. `CHARGEABLE_FEE_FINALIZED` is not used at all

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/InitiateFeeRedemptionCmdHandler.scala; PR: [INV-1709] feat(charge): SG charge logic for GST

**Source-preserving request, proposal, or question:**

> Yeah this is how SG flow works today. `CHARGEABLE_FEE_FINALIZED` is not used at all

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2373 · comment 405918353 · PR 6283 · 2023-06-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/InitiateFeeRedemptionCmdHandler.scala`

**Evidence:** anon-2.jsonl:2373 · comment 405918353 · PR 6283 · 2023-06-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/handlers/InitiateFeeRedemptionCmdHandler.scala`

**Explicit source context (hunk):**

> +
> +    val feeCharge = maybeExisting.get
> +    // Reuse existing PendingDiscount status since next status is either terminal, or for fee redemption requested
> +    if (feeCharge.status != PlanFeeChargeStatus.FEE_CHARGE_INITIATED_PENDING_DISCOUNT_CALCULATION) {
> +      logger.warn(s"Ignoring InitiateFeeRedemptionCmd as FeeManagerEntity[$entityId] FeeChargeRequest[${cmd.feeChargeRequestId}] in status ${feeCharge.status}")
> +      return Effect.ack(cmd.replyTo)
> +    }

## A3-0534 — InvestmentTransferEventProcessor.scala: We need to return Future to chain it here. Otherwise, event processor won’t wait for investOnce and `NotifyInvestmentProcessInitiatedCmd` to complete 

**Source stance:** requested-change

**Context:**

> trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/investmentTransfer/processors/InvestmentTransferEventProcessor.scala; PR: TT-2498 Update InvestmentTransferProjection to skip RedemptionCompletedEvt if target plan is deactivated

**Concern stated in the source:** Otherwise, event processor won’t wait for investOnce and `NotifyInvestmentProcessInitiatedCmd` to complete before moving to next evt

**Source-preserving request, proposal, or question:**

> We need to return Future to chain it here. Otherwise, event processor won’t wait for investOnce and `NotifyInvestmentProcessInitiatedCmd` to complete before moving to next evt

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2374 · comment 406027382 · PR 6290 · 2023-06-23

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/investmentTransfer/processors/InvestmentTransferEventProcessor.scala`

**Evidence:** anon-2.jsonl:2374 · comment 406027382 · PR 6290 · 2023-06-23

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/investmentTransfer/processors/InvestmentTransferEventProcessor.scala`

**Explicit source context (hunk):**

> +      .invoke()
> +      .map(p => p.deactivatedAt.nonEmpty)
> +      .flatMap {
> +
> +        case true =>
> +          // 2023-06-23: For transfers between plans (whereby we do a redemption followed by investment), if
> +          // the target plan was deactivated before the investment request was created, log this error for manual

## A3-0550 — SgPlanUpsertValidationBehaviour.scala: we don’t expect to receive portfolioId in summary step at all. The warn log in summary behaviour is just there, in case FE sends us. We validate and b

**Source stance:** explanation

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgPlanUpsertValidationBehaviour.scala; PR: Feat/INV-1106/plan upsert income satellite, cashsmart

**Concern stated in the source:** This is because we use same request schema for both summary and confirmation

**Source-preserving request, proposal, or question:**

> I think we don’t expect to receive portfolioId in summary step at all. The warn log in summary behaviour is just there, in case FE sends us. We validate and block correctly in confirmation behaviour.
> 
> This is because we use same request schema for both summary and confirmation

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2394 · comment 404500815 · PR 5921 · 2023-06-19

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgPlanUpsertValidationBehaviour.scala`

**Evidence:** anon-2.jsonl:2394 · comment 404500815 · PR 5921 · 2023-06-19

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/planupsert/sg/SgPlanUpsertValidationBehaviour.scala`

**Explicit source context (hunk):**

> +    goal: GoalDto,
> +    request: SgPlanUpsertRequest with StyleDrivenPortfolioBasedProduct with SinglePlanDerivedPortfolioBasedRequest with TagBasedAdvisedPortfolioRequest with StyleDrivenPortfolioBasedRequest[T]
> +  ): Future[Done] = {
> +    validateExistingPlanAndPortfolioAgainstRequest(
> +      mayBeExistingPlan = mayBeExistingPlan,
> +      mayBeRequestedPlanId = request.planId,
> +      mayBeRequestPortfolioId = request.portfolioId,

## A3-0552 — TriggerThresholdBreachedRebalanceCmdHandler.scala: We don’t really change anything to RebalancePlan here right?

**Source stance:** open-question

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/TriggerThresholdBreachedRebalanceCmdHandler.scala; PR: Feat/INV-1303 rebalance refactor phase 3

**Source-preserving request, proposal, or question:**

> We don’t really change anything to RebalancePlan here right?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2396 · comment 404495780 · PR 6056 · 2023-06-19

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/TriggerThresholdBreachedRebalanceCmdHandler.scala`

**Evidence:** anon-2.jsonl:2396 · comment 404495780 · PR 6056 · 2023-06-19

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/TriggerThresholdBreachedRebalanceCmdHandler.scala`

**Explicit source context (hunk):**

> +  ): Persist = {
> +    val plan = state.plan.get
> +
> +    if (plan != cmd.loadedRebalancePlan) {
> +      return Effect.replyError(cmd.replyTo)(
> +        new RebalanceSvcException(s"current plan state is inconsistent with command caller plan state for planId [${plan.planId}] received!",
> +          RebalanceSvcErrorType.CONCURRENT_MODIFICATION

## A3-0561 — AltsRedeemOnceEdgeLogic.scala: units balance is updated accordingly when orders are generated

**Source stance:** explanation

**Context:**

> redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/edge/AltsRedeemOnceEdgeLogic.scala; PR: [INV-1597] feat(redemption): Add RedeemOnce edge endpoint for Alts

**Source-preserving request, proposal, or question:**

> Yup units balance is updated accordingly when orders are generated

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2407 · comment 403125664 · PR 6128 · 2023-06-14

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/edge/AltsRedeemOnceEdgeLogic.scala`

**Evidence:** anon-2.jsonl:2407 · comment 403125664 · PR 6128 · 2023-06-14

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/edge/AltsRedeemOnceEdgeLogic.scala`

**Explicit source context (hunk):**

> +          instrumentId,
> +          throw RedemptionSvcException(s"Unable to find the latest price for instrument $instrumentId", RedemptionSvcErrorType.INTERNAL_ERROR)
> +        )
> +        instrumentPrice * instrumentBalance.availableUnits
> +      }.sum
> +      planLiveMv = planMv - planBalance.pendingRedemptionAmount.getOrElse(BigDecimal(0))
> +    } yield planLiveMv.setScale(2, RoundingMode.HALF_EVEN)

## A3-0573 — BrokerAccountTopicSubscriberCommunicationLogic.scala: Since it’s within investment svc, should we inject refProvider and just use ``` investmentRequests <- refProvider.getPlanInvestmentManagerEntityRef(UU

**Source stance:** suggestion

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/BrokerAccountTopicSubscriberCommunicationLogic.scala; PR: [EN-982] fix(investment): ignore if there is no pending investment

**Source-preserving request, proposal, or question:**

> Since it’s within investment svc, should we inject refProvider and just use
> 
> ```
> investmentRequests <- refProvider.getPlanInvestmentManagerEntityRef(UUID.fromString(planId)).ask(GetPendingInitialInvestmentRequestCmd(_))
> ```
> 
> 
> 
> So we don’t have wonky exception handling here

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2420 · comment 401774605 · PR 6162 · 2023-06-08

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/BrokerAccountTopicSubscriberCommunicationLogic.scala`

> Since it’s within investment svc, should we inject refProvider and just use
> 
> ```
> investmentRequests <- refProvider.getPlanInvestmentManagerEntityRef(UUID.fromString(planId)).ask(GetPendingInitialInvestmentRequestCmd(_))
> ```
> 
> ‌
> 
> So we don’t have wonky exception handling here

**Evidence:** anon-2.jsonl:2420 · comment 401774605 · PR 6162 · 2023-06-08

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/subscribers/BrokerAccountTopicSubscriberCommunicationLogic.scala`

**Explicit source context (hunk):**

> +                            )
> +                          ),
> +                          category = Category.PLATFORM
>                          )
> -                      ),
> -                      category = Category.PLATFORM
> +                      )

## A3-0576 — Alts cashOnlyFee test:1.5M holding,10K pending,5K cash,12381.46 fee waits for funding

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1300] feat(charge)(redemption)(trading)(investment): Cash reservation for Alts fee charge

**Source-preserving request, proposal, or question:**

> Created new Alts-B3 plan:
> 
> * customerId = ``
> * goalId = ``
> * planId = ``
> 
> 
> 
> Setup existing investment \(1.5M\) \+ one pending \(10K\) with insufficient cash balance \(5K\)
> 
> Trigger Q1 charge. Calculated amount = `12381.46`
> 
> Observe that both the investment and fee redemption are in PENDING\_SUBMISSION status, and their corresponding trades are in WAITING\_FOR\_FUNDING status.
> 
> 
> 
> Fee redemption: feeChargeDetails has new field `cashOnlyFee` = true
> 
> "cashOnlyFee": true
> 
> "requestedAmount": 12381.46,
> 
> "status": "PENDING_SUBMISSION",
> 

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Alts-B3 scenario retains1.5M existing+10K pending investment,5K cash, Q1 fee12381.46, PENDING_SUBMISSION/WAITING_FOR_FUNDING and cashOnlyFee=true. Incidental IDs and verbose JSON omitted.
- Repeated test-output/JSON/CLI blocks are omitted; the retained prose and selected exact output-field lines are the evidence. No test outcome beyond those statements is inferred.

**Evidence:** anon-2.jsonl:2423 · comment 398540227 · PR 6096 · 2023-05-29

> Created new Alts-B3 plan:
> 
> * customerId = `

**Evidence:** anon-2.jsonl:2423 · comment 398540227 · PR 6096 · 2023-05-29

> `
> * goalId = `

**Evidence:** anon-2.jsonl:2423 · comment 398540227 · PR 6096 · 2023-05-29

> `
> * planId = `

**Evidence:** anon-2.jsonl:2423 · comment 398540227 · PR 6096 · 2023-05-29

> `
> 
> ‌
> 
> Setup existing investment \(1.5M\) \+ one pending \(10K\) with insufficient cash balance \(5K\)
> 
> Trigger Q1 charge. Calculated amount = `12381.46`
> 
> Observe that both the investment and fee redemption are in PENDING\_SUBMISSION status, and their corresponding trades are in WAITING\_FOR\_FUNDING status.
> 
> ‌
> 
> Fee redemption: feeChargeDetails has new field `cashOnlyFee` = true

**Evidence:** anon-2.jsonl:2423 · comment 398540227 · PR 6096 · 2023-05-29

> "cashOnlyFee": true

**Evidence:** anon-2.jsonl:2423 · comment 398540227 · PR 6096 · 2023-05-29

> "requestedAmount": 12381.46,

**Evidence:** anon-2.jsonl:2423 · comment 398540227 · PR 6096 · 2023-05-29

> "status": "PENDING_SUBMISSION",

**Evidence:** anon-2.jsonl:2423 · comment 398540227 · PR 6096 · 2023-05-29

> ‌
> 
> ‌

## A3-0577 — CashSmartUSD cashOnlyFee=false test:173.74 fee eagerly reserves cash and completes

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1300] feat(charge)(redemption)(trading)(investment): Cash reservation for Alts fee charge

**Source-preserving request, proposal, or question:**

> Trigger charge for another normal CashSmart USD plan
> 
> * goalId = ``
> * planId = ``
> * feeAmount = `173.74`
> 
> 
> 
> Observe that this fee charge is still using eager cash reservation as existing logic. Since charge amount is under cash balance, the fee charge completed right away
> 
> 
> 
> FeeChargeRequest \(new field `cashOnlyFee` = false\)
> 
> "cashOnlyFee": false
> 
> "status": "FEE_CHARGE_COMPLETED",
> 
> Fee redemption \(new field `cashOnlyFee` = false\)
> 
> "status": "COMPLETED",
> 
> "reservedAmount": 173.74
> 
> Trade
> 

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- CashSmartUSD comparison retains173.74 fee, existing eager reservation, immediate completion under cash balance and cashOnlyFee=false. Incidental IDs and repeated JSON omitted.
- Repeated test-output/JSON/CLI blocks are omitted; the retained prose and selected exact output-field lines are the evidence. No test outcome beyond those statements is inferred.

**Evidence:** anon-2.jsonl:2424 · comment 398541448 · PR 6096 · 2023-05-29

> Trigger charge for another normal CashSmart USD plan
> 
> * goalId = `

**Evidence:** anon-2.jsonl:2424 · comment 398541448 · PR 6096 · 2023-05-29

> `
> * planId = `

**Evidence:** anon-2.jsonl:2424 · comment 398541448 · PR 6096 · 2023-05-29

> `
> * feeAmount = `173.74`
> 
> ‌
> 
> Observe that this fee charge is still using eager cash reservation as existing logic. Since charge amount is under cash balance, the fee charge completed right away
> 
> ‌
> 
> FeeChargeRequest \(new field `cashOnlyFee` = false\)

**Evidence:** anon-2.jsonl:2424 · comment 398541448 · PR 6096 · 2023-05-29

> "cashOnlyFee": false

**Evidence:** anon-2.jsonl:2424 · comment 398541448 · PR 6096 · 2023-05-29

> "status": "FEE_CHARGE_COMPLETED",

**Evidence:** anon-2.jsonl:2424 · comment 398541448 · PR 6096 · 2023-05-29

> ‌
> 
> Fee redemption \(new field `cashOnlyFee` = false\)

**Evidence:** anon-2.jsonl:2424 · comment 398541448 · PR 6096 · 2023-05-29

> "status": "COMPLETED",

**Evidence:** anon-2.jsonl:2424 · comment 398541448 · PR 6096 · 2023-05-29

> "reservedAmount": 173.74

**Evidence:** anon-2.jsonl:2424 · comment 398541448 · PR 6096 · 2023-05-29

> ‌
> 
> Trade

**Evidence:** anon-2.jsonl:2424 · comment 398541448 · PR 6096 · 2023-05-29

> ‌

## A3-0578 — 15K top-up funds Alts fee before earlier investment;12381.46 fee completes

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1300] feat(charge)(redemption)(trading)(investment): Cash reservation for Alts fee charge

**Source-preserving request, proposal, or question:**

> Top up balance to 15K - which is sufficient to fund either the fee redemption / investment
> 
> 
> 
> Observe that even though investment was created first, fee redemption takes priority
> 
> 
> 
> FeeChargeRequest
> 
> "cashOnlyFee": true
> 
> "status": "FEE_CHARGE_COMPLETED",
> 
> "redeemedAmount": 12381.46,
> 
> Fee redemption
> 
> "status": "COMPLETED",
> 
> Trade
> 

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- 15K top-up can fund either investment or fee; fee redemption takes priority despite later creation. Fee12381.46 reaches completed status with cashOnlyFee=true. Repeated JSON omitted.
- Repeated test-output/JSON/CLI blocks are omitted; the retained prose and selected exact output-field lines are the evidence. No test outcome beyond those statements is inferred.

**Evidence:** anon-2.jsonl:2425 · comment 398542712 · PR 6096 · 2023-05-29

> Top up balance to 15K - which is sufficient to fund either the fee redemption / investment
> 
> ‌
> 
> Observe that even though investment was created first, fee redemption takes priority
> 
> ‌
> 
> FeeChargeRequest

**Evidence:** anon-2.jsonl:2425 · comment 398542712 · PR 6096 · 2023-05-29

> "cashOnlyFee": true

**Evidence:** anon-2.jsonl:2425 · comment 398542712 · PR 6096 · 2023-05-29

> "status": "FEE_CHARGE_COMPLETED",

**Evidence:** anon-2.jsonl:2425 · comment 398542712 · PR 6096 · 2023-05-29

> "redeemedAmount": 12381.46,

**Evidence:** anon-2.jsonl:2425 · comment 398542712 · PR 6096 · 2023-05-29

> ‌
> 
> Fee redemption

**Evidence:** anon-2.jsonl:2425 · comment 398542712 · PR 6096 · 2023-05-29

> "status": "COMPLETED",

**Evidence:** anon-2.jsonl:2425 · comment 398542712 · PR 6096 · 2023-05-29

> ‌
> 
> Trade

**Evidence:** anon-2.jsonl:2425 · comment 398542712 · PR 6096 · 2023-05-29

> ‌

## A3-0603 — FeeChargeRequestProjection.scala: If cash reservation fails, we will log this error and delete the fee charge request. We would have separate dashboard/admin screen to keep track of wh

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/FeeChargeRequestProjection.scala; PR: [INV-1300] feat(charge)(trading)(redemption): Cash reservation for Alts fee charge

**Source-preserving request, proposal, or question:**

> If cash reservation fails, we will log this error and delete the fee charge request. We would have separate dashboard/admin screen to keep track of which Alts plans have not been charge. I think this is sufficient.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2451 · comment 397444205 · PR 6057 · 2023-05-25

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/FeeChargeRequestProjection.scala`

## A3-0604 — Alts cash-reservation remote call in projection; Kafka request/result ideal lacks trading events

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/FeeChargeRequestProjection.scala; PR: [INV-1300] feat(charge)(trading)(redemption): Cash reservation for Alts fee charge

**Source-preserving request, proposal, or question:**

> It’s fine to have remote call in projection class \(not fine in cmd handler\)
> 
> In ideal workflow situation:
> 
> * charge to publish kafka msg `FeeCashReservationRequestedMsg`
> * trading listens to charge topic, handles that msg and reserve cash
> * trading to publish kafka msg about the cash reservation results
> 
>     * today it doesn’t publish any messages for cash reservation at all
>     * there is no event for cash reservation failure
>     
> * charge to consume these cash reservation messages, and continue to flow
> 
> 
> 
> For the scope of this ticket, I went with the approach in this PR

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Remote call in projection tolerated for scope; ideal request/result Kafka workflow cannot fully exist today because trading publishes neither reservation messages nor failure event.

**Evidence:** anon-2.jsonl:2452 · comment 397445492 · PR 6057 · 2023-05-25

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/FeeChargeRequestProjection.scala`

> It’s fine to have remote call in projection class \(not fine in cmd handler\)
> 
> In ideal workflow situation:
> 
> * charge to publish kafka msg `FeeCashReservationRequestedMsg`
> * trading listens to charge topic, handles that msg and reserve cash
> * trading to publish kafka msg about the cash reservation results
> 
>     * today it doesn’t publish any messages for cash reservation at all
>     * there is no event for cash reservation failure
>     
> * charge to consume these cash reservation messages, and continue to flow
> 
> ‌
> 
> For the scope of this ticket, I went with the approach in this PR

## A3-0613 — package.scala: Use `terminalTradeStatuses` ?

**Source stance:** open-question

**Context:**

> trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/ces/state/package.scala; PR: TT-2320 Set cancelledAt for invalid orders and filter for trade status when looking for pending amount sell orders

**Source-preserving request, proposal, or question:**

> Use `terminalTradeStatuses` ?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2462 · comment 397196616 · PR 6071 · 2023-05-24

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/ces/state/package.scala`

**Evidence:** anon-2.jsonl:2462 · comment 397196616 · PR 6071 · 2023-05-24

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/ces/state/package.scala`

**Explicit source context (hunk):**

> )
>  
>      val pendingSettlementAmountBasedSellOrders: List[Order] = trades
> +      .filter(t => !TradeStatus.terminalTradeStatuses.contains(t.status))
>        .flatMap(_.orders)
>        .filter(
>          s =>

## A3-0631 — : Tested in d34. ### Invest manually with one instrument in an existing plan with 2 instruments 50-50 After investment settles, MV is updated and thresh

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1212] feat(rebalance): HK Rebalance communication for threshold breach

**Source-preserving request, proposal, or question:**

> Tested in d34.
> 
> ### Invest manually with one instrument in an existing plan with 2 instruments 50-50
> 
> After investment settles, MV is updated and threshold breach is triggered automatically
> 
> "status": "REBALANCING_SUGGESTED_PENDING_ACCEPTANCE",
> 
> "reason": "THRESHOLD_BREACH",
> 
> "instrumentWeights": {
> 
> Email communication is trigger
> 
> [<url> data-inline-card='' } 
> 
> ![](<url>
> Verified customer name, goal name, account name, action by timestamp, CTA url is correct
> 
> Clicked CTA, login and it brings to Preferences page correctly

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Manual one-instrument investment in50/50 two-instrument HK plan triggers breach after settlement/MV; notification values and Preferences CTA tested.
- Repeated test-output/JSON/CLI blocks are omitted; the retained prose and selected exact output-field lines are the evidence. No test outcome beyond those statements is inferred.
- HK scope in the authored title/constraint comes from the explicitly quoted PR title, not from the comment prose or an unavailable hunk.

**Evidence:** anon-2.jsonl:2480 · comment 391448129 · PR 5904 · 2023-05-03

> Tested in d34.
> 
> ### Invest manually with one instrument in an existing plan with 2 instruments 50-50
> 
> After investment settles, MV is updated and threshold breach is triggered automatically

**Evidence:** anon-2.jsonl:2480 · comment 391448129 · PR 5904 · 2023-05-03

> "status": "REBALANCING_SUGGESTED_PENDING_ACCEPTANCE",

**Evidence:** anon-2.jsonl:2480 · comment 391448129 · PR 5904 · 2023-05-03

> "reason": "THRESHOLD_BREACH",

**Evidence:** anon-2.jsonl:2480 · comment 391448129 · PR 5904 · 2023-05-03

> "instrumentWeights": {

**Evidence:** anon-2.jsonl:2480 · comment 391448129 · PR 5904 · 2023-05-03

> Email communication is trigger
> 
> [<url> data-inline-card='' } 
> 
> ![](<url>
> Verified customer name, goal name, account name, action by timestamp, CTA url is correct
> 
> Clicked CTA, login and it brings to Preferences page correctly
> 
> ‌

**Evidence:** anon-2.jsonl:2480 · comment 391448129 · PR 5904 · 2023-05-03

**Explicit source context (pr_title):**

> [INV-1212] feat(rebalance): HK Rebalance communication for threshold breach

## A3-0632 — : Trigger the endpoint to accept all threshold breach requests And settle the rebalance trade ``` { "rebalanceRequestId": "", "status": "REBALANCING_COM

**Source stance:** reported-verification

**Context:**

> None; PR: [INV-1212] feat(rebalance): HK Rebalance communication for threshold breach

**Source-preserving request, proposal, or question:**

> Trigger the endpoint to accept all threshold breach requests
> 
> And settle the rebalance trade
> 
> "status": "REBALANCING_COMPLETED",
> 
> "totalSoldAmount": 2003.01,
> 
> "totalPurchasedAmount": 2003.01,
> 
> Email communication is triggered
> 
> [<url> data-inline-card='' } 
> 
> ![](<url>
> Verified customer name, goal name, account name, CTA url is correct
> 
> Clicked CTA, login and it brings to A&B page correctly

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Acceptance and settlement completes rebalance; notification A&B CTA tested. Preserve reported test only, not mandate.
- Repeated test-output/JSON/CLI blocks are omitted; the retained prose and selected exact output-field lines are the evidence. No test outcome beyond those statements is inferred.

**Evidence:** anon-2.jsonl:2481 · comment 391451997 · PR 5904 · 2023-05-03

> Trigger the endpoint to accept all threshold breach requests
> 
> And settle the rebalance trade

**Evidence:** anon-2.jsonl:2481 · comment 391451997 · PR 5904 · 2023-05-03

> "status": "REBALANCING_COMPLETED",

**Evidence:** anon-2.jsonl:2481 · comment 391451997 · PR 5904 · 2023-05-03

> "totalSoldAmount": 2003.01,

**Evidence:** anon-2.jsonl:2481 · comment 391451997 · PR 5904 · 2023-05-03

> "totalPurchasedAmount": 2003.01,

**Evidence:** anon-2.jsonl:2481 · comment 391451997 · PR 5904 · 2023-05-03

> Email communication is triggered
> 
> [<url> data-inline-card='' } 
> 
> ![](<url>
> Verified customer name, goal name, account name, CTA url is correct
> 
> Clicked CTA, login and it brings to A&B page correctly

## A3-0662 — package.scala: The comment above says new txn would have `DISTRIBUTION_RECEIVED` but we are removing it?

**Source stance:** open-question

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/common/package.scala; PR: Feat/INV-1414 update activity transaction status

**Source-preserving request, proposal, or question:**

> The comment above says new txn would have `DISTRIBUTION_RECEIVED` but we are removing it?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2512 · comment 389710702 · PR 5841 · 2023-04-26

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/common/package.scala`

**Evidence:** anon-2.jsonl:2512 · comment 389710702 · PR 5841 · 2023-04-26

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/common/package.scala`

**Explicit source context (hunk):**

> object TransactionType extends Enumeration {
>      val INVESTMENT, REDEMPTION, REBALANCE, DEPOSIT, INTEREST_RECEIVED, WITHDRAWAL, FEE_WITHDRAWAL, FEE_REDEMPTION,
> -    TRAILER_REBATE, DIVIDEND_RECEIVED, DISTRIBUTION_RECEIVED, FX_CONVERSION, ASSET_TRANSFER = Value
> +    TRAILER_REBATE, DIVIDEND_RECEIVED, FX_CONVERSION, ASSET_TRANSFER = Value
>      type TransactionType = Value
>      implicit val format: Format[TransactionType] = enumFormat(TransactionType)
>    }

## A3-0666 — package.scala: use `CREATED_AND_PENDING_INTERNAL_BROKER_SUBMISSION` for requested status

**Source stance:** requested-change

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/common/package.scala; PR: [INV-1437] feat(transaction): Models

**Source-preserving request, proposal, or question:**

> Let’s use `CREATED_AND_PENDING_INTERNAL_BROKER_SUBMISSION` for requested status

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2516 · comment 387921515 · PR 5770 · 2023-04-19

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/common/package.scala`

## A3-0672 — TransactionTypes.scala: RequestedUnitStatusDetailsDto \{ transactionStatus // required `CREATED_AND_PENDING_INTERNAL_BROKER_SUBMISSION` requestedUnits requestedAt \}

**Source stance:** suggestion

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala; PR: [INV-1437] feat(transaction): Models

**Source-preserving request, proposal, or question:**

> RequestedUnitStatusDetailsDto \{
> 
> transactionStatus // required `CREATED_AND_PENDING_INTERNAL_BROKER_SUBMISSION`
> 
> requestedUnits
> 
> requestedAt
> 
> \}

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2522 · comment 387926462 · PR 5770 · 2023-04-19

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Evidence:** anon-2.jsonl:2522 · comment 387926462 · PR 5770 · 2023-04-19

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Explicit source context (hunk):**

> sealed trait FxStatusDetailsDto extends TransactionStatusDetailsDto
>    sealed trait RebalanceStatusDetailsDto extends TransactionStatusDetailsDto
>    sealed trait DistributionStatusDetailsDto extends TransactionStatusDetailsDto
> +  sealed trait AssetTransferStatusDetailsDto extends TransactionStatusDetailsDto
> +
>    //TODO: Add more traits for other transaction types when being defined

## A3-0673 — TransactionTypes.scala: PendingUnitStatusDetailsDto \{ transactionStatus // required `...` requestedUnits requestedAt \}

**Source stance:** suggestion

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala; PR: [INV-1437] feat(transaction): Models

**Source-preserving request, proposal, or question:**

> PendingUnitStatusDetailsDto \{
> 
> transactionStatus // required `...`
> 
> requestedUnits
> 
> requestedAt
> 
> \}

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2523 · comment 387926772 · PR 5770 · 2023-04-19

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Evidence:** anon-2.jsonl:2523 · comment 387926772 · PR 5770 · 2023-04-19

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Explicit source context (hunk):**

> +    transactionStatus: TransactionStatus,
> +    requestedUnits: BigDecimal,
> +    requestedAt: ZonedDateTime
> +  ) extends AssetTransferStatusDetailsDto
> +
> +  object RequestedUnitsStatusDetailsDto {
> +    val format: Format[RequestedUnitsStatusDetailsDto] = Json.format[RequestedUnitsStatusDetailsDto]

## A3-0674 — TransactionTypes.scala: `SettledUnitsStatusDetails`\{ transactionStatus // SETTLEMENT\_CONFIRM settledUnits settledAt settledPrice settledPriceDate \}

**Source stance:** suggestion

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala; PR: [INV-1437] feat(transaction): Models

**Source-preserving request, proposal, or question:**

> `SettledUnitsStatusDetails`\{
> 
> transactionStatus // SETTLEMENT\_CONFIRM
> 
> settledUnits
> 
> settledAt
> 
> settledPrice
> 
> settledPriceDate
> 
> \}

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2524 · comment 387929296 · PR 5770 · 2023-04-19

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

## A3-0675 — TransactionTypes.scala: If rejected also contains units, we can drop this field

**Source stance:** suggestion

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala; PR: [INV-1437] feat(transaction): Models

**Source-preserving request, proposal, or question:**

> If rejected also contains units, we can drop this field

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2525 · comment 387931652 · PR 5770 · 2023-04-19

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Evidence:** anon-2.jsonl:2525 · comment 387931652 · PR 5770 · 2023-04-19

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Explicit source context (hunk):**

> +    createdAt: ZonedDateTime,
> +    customerId: UUID,
> +    goalId: UUID,
> +    planId: UUID,
> +    ccy: CurrencyUnit,
> +    tradingAccountType: TradingAccountType,
> +    statusDetails: AssetTransferStatusDetailsDto,

## A3-0700 — PortfolioVersionUpgradeRebalanceRequestsGenerator.scala: Hmm looks like we need same check in auto RPC via `RebalanceCompletedEvt` too?

**Source stance:** open-question

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/managers/PortfolioVersionUpgradeRebalanceRequestsGenerator.scala; PR: [INV-1491] feat(rebalance): Run RPC in background. Skip RPC if already requested manually

**Source-preserving request, proposal, or question:**

> Hmm looks like we need same check in auto RPC via `RebalanceCompletedEvt` too?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2551 · comment 389076879 · PR 5818 · 2023-04-24

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/managers/PortfolioVersionUpgradeRebalanceRequestsGenerator.scala`

## A3-0704 — Historical event-handler change accepted as specific exception, supporting Jira unavailable

**Source stance:** suggestion

**Context:**

> None; PR: [INV-1473] feat(portfolio): Update logic about latest TAA in ModelPortfolioEntity

**Source-preserving request, proposal, or question:**

> It’s against the rule of not changing behaviour of event handler in EventSource…. but in this specific case, I think it’s safe to do so.
> 
> More context in Jira [<url> data-inline-card='' }

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Changing event handler behavior is accepted only as source-specific safe exception; supporting Jira is redacted and not available.

**Evidence:** anon-2.jsonl:2555 · comment 388008639 · PR 5787 · 2023-04-19

## A3-0706 — Missing PlanSubscriber: inactive fine, active requires manual investigation/add-back

**Source stance:** explanation

**Context:**

> amend-scripts/src/main/scala/rebalance/PreRpcValidation.scala; PR: [INV-1432] feat(amend-scripts): Pre-RPC data consistency validation

**Source-preserving request, proposal, or question:**

> PlanSubscriber in rebalance keeps track of the planIds subscribing to a portfolioId \+ effectiveDate. This is how we trigger RPC for existing plans. If missing \+ deactivated, all good. If missing \+ active, figure why? If intentional, we should fix whatever required and add it back. Else, just add it back. Either way it needs manual investigation.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Missing subscriber+deactivated is fine; missing+active requires manual investigation and repair/add-back. Keep portfolioId+effectiveDate subscription meaning.

**Evidence:** anon-2.jsonl:2557 · comment 387563551 · PR 5762 · 2023-04-18

Source path: `amend-scripts/src/main/scala/rebalance/PreRpcValidation.scala`

**Evidence:** anon-2.jsonl:2557 · comment 387563551 · PR 5762 · 2023-04-18

Source path: `amend-scripts/src/main/scala/rebalance/PreRpcValidation.scala`

**Explicit source context (hunk):**

> +    planProfile: PlanProfileValidationData
> +  ): Future[PlanProfileInconsistencyActionItem] = {
> +    val obsoletePlanSubscriber = planProfile.symptoms match {
> +      case List(MissingSubscriberInRebalanceSvc) => false
> +      case List(MissingInGoalSvc, MissingInRebalanceSvc, MissingInTradingSvc) => true
> +    }
> +

## A3-0735 — common.conf: `silver.entity-ref.ask-timeout` to make it clear that this timeout is only used for the EntityRef?

**Source stance:** suggestion

**Context:**

> rebalance-impl/src/main/resources/common.conf; PR: Fix/INV-1151 rebalance entity refactor phase 1 timeout

**Source-preserving request, proposal, or question:**

> Maybe `silver.entity-ref.ask-timeout` to make it clear that this timeout is only used for the EntityRef?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2587 · comment 381120932 · PR 5589 · 2023-03-24

Source path: `rebalance-impl/src/main/resources/common.conf`

**Evidence:** anon-2.jsonl:2587 · comment 381120932 · PR 5589 · 2023-03-24

Source path: `rebalance-impl/src/main/resources/common.conf`

**Explicit source context (hunk):**

> eventual-consistency-delay = 2s
>  }
>  
> +silver.entity-ref.ask-timeout = 30s
> +
>  lagom {
>    persistence {

## A3-0740 — Rebalance cash-release timing: pending-MV double-count window until buy export

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkRebalanceTopicSubscriber.scala; PR: [INV-1191] feat(compliance): HK Earmark logic for Rebalance flow

**Source-preserving request, proposal, or question:**

> Since we do not have updates from `timeseries` yet, we can rely on rebalance updates itself. `timeseries` would already capture the pending order as soon as they are generated, however we only release when the buy trade is exported.
> 
> This is the double counting window. If timeseries lags too long behind, we might release before the pending amount is captured. Until we have updates from timeseries, exported event is practical enough \(somewhat safe since there are decent hours between order generation and trade export, and not days like settlement assumed/confirmed\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Preserve order-generation-to-export double-count window, stale-timeseries early-release risk, and pragmatic export-event fallback while timeseries messages absent.

**Evidence:** anon-2.jsonl:2592 · comment 380318979 · PR 5530 · 2023-03-22

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkRebalanceTopicSubscriber.scala`

> Since we do not have updates from `timeseries` yet, we can rely on rebalance updates itself. `timeseries` would already capture the pending order as soon as they are generated, however we only release when the buy trade is exported.
> 
> This is the double counting window. If timeseries lags too long behind, we might release before the pending amount is captured. Until we have updates from timeseries, exported event is practical enough \(somewhat safe since there are decent hours between order generation and trade export, and not days like settlement assumed/confirmed\)
> 
> ‌

**Evidence:** anon-2.jsonl:2592 · comment 380318979 · PR 5530 · 2023-03-22

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkRebalanceTopicSubscriber.scala`

**Explicit source context (hunk):**

> +      // Hence, we use the order amount which is calculated using latest price available as approximation.
> +      // This amount can be further buffered if needed in future.
> +      val earmarkAmount = msg.rebalanceRequest.sellOrders.flatMap(_.orderAmount).sum
> +      createEarmark(
> +        msg.customerId,
> +        mapRebalanceBuyEarmarkId(msg.goalId, msg.planId, msg.rebalanceRequest.rebalanceRequestId),
> +        earmarkAmount,

## A3-0745 — HkRebalanceTopicSubscriber.scala: that makes sense. Our earmark as of now is immutable, so I’m not updating it yet. When we need to, I’ll revisit this flow :thumbsup: For now, using th

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkRebalanceTopicSubscriber.scala; PR: [INV-1191] feat(compliance): HK Earmark logic for Rebalance flow

**Source-preserving request, proposal, or question:**

> Yeah that makes sense. Our earmark as of now is immutable, so I’m not updating it yet. When we need to, I’ll revisit this flow :thumbsup:  For now, using this original sell amount is good enough I think.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2597 · comment 381119511 · PR 5530 · 2023-03-24

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkRebalanceTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:2597 · comment 381119511 · PR 5530 · 2023-03-24

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkRebalanceTopicSubscriber.scala`

**Explicit source context (hunk):**

> +
> +  def handle(message: RebalanceMsg): Future[Done] = message match {
> +    case msg: RebalanceTradeSubmittedExternallyMsg
> +        if msg.rebalanceRequest.status == RebalanceRequestStatus.SELL_TRADE_SUBMITTED_EXTERNALLY_PENDING_SETTLEMENT =>
> +      // Since we do not know exact amount to earmark until these sell orders are settled, however, it would be too late then.
> +      // Hence, we use the order amount which is calculated using latest price available as approximation.
> +      // This amount can be further buffered if needed in future.

## A3-0822 — Recurring failure email: actual reason, event-domain coupling and direct-publish deferral

**Source stance:** suggestion

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/communication/hk/HkRecurringInvestmentFailureEmailComposer.scala; PR: Resolve INV-1135: Send email for failed recurring investments with state change info

**Concern stated in the source:** And if we add all applicable compliance block reasons \(so that we can evolve the email logic freely\), we would also bake the compliance domain to investment event domain.

* Since it might fail, we should retry, and add support to retry manually via endpoint, if needed
* You can add all the failure reasons here, but no need to think too hard, cuz it’s all on the fly - nothing is persisted
* If it gets too slow and starts impacting the main triggering flow, we can revisit moving to event processor \(or postpone further by dispatching to another kafka topic, and construct the email and publish to communication from there\)

**Source-preserving request, proposal, or question:**

> Yeah simulation only makes sense if we want to warn user about potential failure in the upcoming-recurring-investment email. For this jira, we want to include exactly the failure reason. This means the entry point to construct the email should already contain the failure reason, passed from the `RecurringInvestmentProcessor`.
> 
> 
> 
> This can be achieved via Cmd\+Evt like what you did here. However, I feel we might couple our event domain with the copy \(suitability VS risk breach\), e.g today we add CrBreach as reason, tmr copy wants to distinguish between Cat1 breach vs Cat2 breach. And if we add all applicable compliance block reasons \(so that we can evolve the email logic freely\), we would also bake the compliance domain to investment event domain. Not to mention, we would likely support this to SG too - in which case, do we want to handle SG vs HK failure reason in the event?
> 
> 
> 
> The above is not necessarily wrong, but I don’t think we know everything to decide it now. And there’s a way to postpone this decision: by publishing directly to communication in the `RecurringInvestmentProcessor`
> 
> * Since it might fail, we should retry, and add support to retry manually via endpoint, if needed
> * You can add all the failure reasons here, but no need to think too hard, cuz it’s all on the fly - nothing is persisted
> * If it gets too slow and starts impacting the main triggering flow, we can revisit moving to event processor \(or postpone further by dispatching to another kafka topic, and construct the email and publish to communication from there\)
> 
> 
> 
> `RecurringInvestmentRequestFailedEvent` with proper region-specific failure reason sounds like a good thing to me, I’m just not sure we’re ready to implement it yet.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Keep upcoming-warning simulation distinct from actual failure reason. Persisted region/compliance/copy coupling is unresolved; direct publish with bounded retry/manual endpoint is a deferral option, later task topic/event flow conditional on slowness.

**Evidence:** anon-2.jsonl:2679 · comment 369402726 · PR 5203 · 2023-02-13

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/communication/hk/HkRecurringInvestmentFailureEmailComposer.scala`

> Yeah simulation only makes sense if we want to warn user about potential failure in the upcoming-recurring-investment email. For this jira, we want to include exactly the failure reason. This means the entry point to construct the email should already contain the failure reason, passed from the `RecurringInvestmentProcessor`.
> 
> ‌
> 
> This can be achieved via Cmd\+Evt like what you did here. However, I feel we might couple our event domain with the copy \(suitability VS risk breach\), e.g today we add CrBreach as reason, tmr copy wants to distinguish between Cat1 breach vs Cat2 breach. And if we add all applicable compliance block reasons \(so that we can evolve the email logic freely\), we would also bake the compliance domain to investment event domain. Not to mention, we would likely support this to SG too - in which case, do we want to handle SG vs HK failure reason in the event?
> 
> ‌
> 
> The above is not necessarily wrong, but I don’t think we know everything to decide it now. And there’s a way to postpone this decision: by publishing directly to communication in the `RecurringInvestmentProcessor`
> 
> * Since it might fail, we should retry, and add support to retry manually via endpoint, if needed
> * You can add all the failure reasons here, but no need to think too hard, cuz it’s all on the fly - nothing is persisted
> * If it gets too slow and starts impacting the main triggering flow, we can revisit moving to event processor \(or postpone further by dispatching to another kafka topic, and construct the email and publish to communication from there\)
> 
> ‌
> 
> `RecurringInvestmentRequestFailedEvent` with proper region-specific failure reason sounds like a good thing to me, I’m just not sure we’re ready to implement it yet. 
> 
> ‌

## A3-0856 — CustomerAdvisoryProfileCommands.scala: Cmd starts with verb… so it’s CheckExpiryCmd…

**Source stance:** requested-change

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/ces/CustomerAdvisoryProfileCommands.scala; PR: [INV-1134] feat(Advisory): Added CRAExpired event and message

**Source-preserving request, proposal, or question:**

> Nit: Cmd starts with verb… so it’s CheckExpiryCmd…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2714 · comment 371898148 · PR 5320 · 2023-02-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/ces/CustomerAdvisoryProfileCommands.scala`

**Evidence:** anon-2.jsonl:2714 · comment 371898148 · PR 5320 · 2023-02-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/ces/CustomerAdvisoryProfileCommands.scala`

**Explicit source context (hunk):**

> -}
> \ No newline at end of file
> +}
> +
> +case object CheckCraExpiryCmd extends CustomerAdvisoryProfileCmd
> +  with ReplyType[Done] {
> +  implicit val format: Format[CheckCraExpiryCmd.type] = singletonFormat(CheckCraExpiryCmd)

## A3-0863 — SgServiceLogicImpl.scala: Why don’t we read from entity here?

**Source stance:** open-question

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/SgServiceLogicImpl.scala; PR: [SILVER-14633] feat(charge): Refactor sync with redemption to account states

**Source-preserving request, proposal, or question:**

> Why don’t we read from entity here?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2721 · comment 371632173 · PR 5309 · 2023-02-21

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/SgServiceLogicImpl.scala`

## A3-0864 — SgServiceLogicImpl.scala: Ah this is just to compare between charge entity and charge readside? I think we can skip this, cuz we will anyhow fetch from entity and write again -

**Source stance:** suggestion

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/SgServiceLogicImpl.scala; PR: [SILVER-14633] feat(charge): Refactor sync with redemption to account states

**Concern stated in the source:** I think we can skip this, cuz we will anyhow fetch from entity and write again - which should upsert in readside

**Source-preserving request, proposal, or question:**

> Ah this is just to compare between charge entity and charge readside? I think we can skip this, cuz we will anyhow fetch from entity and write again - which should upsert in readside

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2722 · comment 371634458 · PR 5309 · 2023-02-21

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/SgServiceLogicImpl.scala`

## A3-0919 — CraManager.scala: Hmm this will emit `ExpiryDateOverriddenEvt` which is not what happening here… I think we will need another pair of cmd/event

**Source stance:** observed-defect

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Hmm this will emit `ExpiryDateOverriddenEvt` which is not what happening here… I think we will need another pair of cmd/event

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2778 · comment 367135684 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Evidence:** anon-2.jsonl:2778 · comment 367135684 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Explicit source context (hunk):**

> +        case _: VulnerableCustomerProfile =>
> +          logger.warn(s"Customer $customerId is vulnerable")
> +          Future.successful(Done)
> +      }
> +    } yield Done
> +  }
> +

## A3-0928 — CRA expiry override versus check: date-update event separate from expired-flag event

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> OverrideExpiryDateCmd\(customerId, expiryDate\)  
> CheckExpiryDateCmd\(customerId\)  
>   
> Entity:
> 
> * override cmd handler: emit ExpiryDateOverriddenEvt, and potentially CraExpiredEvt
> * check cmd handler: noop or CraExpiredEvt
> * ExpiryDateOverriddenEvt handler: update date
> * CraExpiredEvt handler: update flag
> 
> 
> 
> compliance: CraExpiredEvt

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Keep override command emits override+possibly expiration event while check emits noop/expiration; handlers update date versus flag separately; compliance consumes expiry event.

**Evidence:** anon-2.jsonl:2787 · comment 367146282 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

> OverrideExpiryDateCmd\(customerId, expiryDate\)  
> CheckExpiryDateCmd\(customerId\)  
>   
> Entity:
> 
> * override cmd handler: emit ExpiryDateOverriddenEvt, and potentially CraExpiredEvt
> * check cmd handler: noop or CraExpiredEvt
> * ExpiryDateOverriddenEvt handler: update date
> * CraExpiredEvt handler: update flag
> 
> ‌
> 
> compliance: CraExpiredEvt
> 
> ‌

**Evidence:** anon-2.jsonl:2787 · comment 367146282 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Explicit source context (hunk):**

> +        case _: VulnerableCustomerProfile =>
> +          logger.warn(s"Customer $customerId is vulnerable")
> +          Future.successful(Done)
> +      }
> +    } yield Done
> +  }
> +

## A3-0943 — CraManager.scala: I guess no need to add “maybe” bit - it’s already part of `simulateOnly` flag? maybe just `internalSubmitCra` or something like that?

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala; PR: Feat/INV-895 simulate VC

**Source-preserving request, proposal, or question:**

> I guess no need to add “maybe” bit - it’s already part of `simulateOnly` flag? maybe just `internalSubmitCra` or something like that?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2803 · comment 358801350 · PR 4858 · 2023-01-10

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Evidence:** anon-2.jsonl:2803 · comment 358801350 · PR 4858 · 2023-01-10

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Explicit source context (hunk):**

> for {
>        questionnaire <- getLatestQuestionnaire(request.craQuestionnaireVersion)
>        _ <- validateSubmission(request.craQuestionnaire, questionnaire)
>  
>        age <- getAge(customerId)
> +
>        advisoryProfileResult <- matchAdvisoryProfile(Input(request, age), questionnaire)

## A3-0961 — CraManager.scala: put a comment here, or even an error log that if `daysUntilExpiry` < 0… because if so, `riskProfileStatus` should have been updated to Expired

**Source stance:** requested-change

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala; PR: Feat/INV-895 simulate VC

**Concern stated in the source:** Let’s put a comment here, or even an error log that if `daysUntilExpiry` < 0… because if so, `riskProfileStatus` should have been updated to Expired

**Source-preserving request, proposal, or question:**

> Let’s put a comment here, or even an error log that if `daysUntilExpiry` < 0… because if so, `riskProfileStatus` should have been updated to Expired

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2821 · comment 359929056 · PR 4858 · 2023-01-13

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Evidence:** anon-2.jsonl:2821 · comment 359929056 · PR 4858 · 2023-01-13

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Explicit source context (hunk):**

> +                customerInGP,
> +                customerGPEnds
> +              )
> +
> +              res = Set(maybeCraExpiring, maybeCustomerInGP).flatten
> +            } yield res
> +          }

## A3-0984 — InvestmentCommunicationV2EventProcessor.scala: `SettlementAssumed` won’t have these confirmed fields…

**Source stance:** observed-defect

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentCommunicationV2EventProcessor.scala; PR: EN-120 Handle Investment Completed and Upcoming Recurring Investment emails using Comms V2

**Source-preserving request, proposal, or question:**

> `SettlementAssumed` won’t have these confirmed fields…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2844 · comment 354940832 · PR 4890 · 2022-12-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:2844 · comment 354940832 · PR 4890 · 2022-12-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> +  def investmentRequestSettlementConfirmedEvtHandler(ele: EventStreamElement[InvestmentRequestSettlementConfirmedEvt]): Future[List[BoundStatement]] = {
> +    val request = ele.event.request
> +    if (InvestmentCommunicationV2EventProcessor.ValidCommunicationReasons.contains(request.reason) &&
> +        request.confirmedSettlementAmount.isDefined &&
> +        request.confirmedAt.isDefined &&
> +        request.confirmedAt.get.isAfter(dateTimeProvider.now.minusDays(2))) {
> +

## A3-0985 — InvestmentCommunicationV2EventProcessor.scala: confirmed fields are only populated when the status is settlement confirmed

**Source stance:** explanation

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentCommunicationV2EventProcessor.scala; PR: EN-120 Handle Investment Completed and Upcoming Recurring Investment emails using Comms V2

**Source-preserving request, proposal, or question:**

> yeah confirmed fields are only populated when the status is settlement confirmed

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2845 · comment 354941215 · PR 4890 · 2022-12-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/InvestmentCommunicationV2EventProcessor.scala`

## A3-1046 — HkServiceLogicImpl.scala: We don’t need this cuz the cmd already returns Done?

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/HkServiceLogicImpl.scala; PR: Feat/INV-840 plan upsert confirmation

**Concern stated in the source:** We don’t need this cuz the cmd already returns Done?

**Source-preserving request, proposal, or question:**

> We don’t need this cuz the cmd already returns Done?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2910 · comment 349048911 · PR 4779 · 2022-11-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/HkServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2910 · comment 349048911 · PR 4779 · 2022-11-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/HkServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +            requestedBy = request.requestedBy
> +          )
> +        )
> +    }
> +  }
>  }

## A3-1051 — Recurring acknowledgement retained dormant; next schedule refreshes it

**Source stance:** explanation

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/helpers/hk/HkComplianceValidatorImpl.scala; PR: Feat/INV-854 hook compliance plan upsert goal

**Source-preserving request, proposal, or question:**

> Right so we discuss there is no need to remove recurring ack, since it will just stay dormant, and new schedule will refresh the ack again.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Final source discussion says recurring ack need not be removed: dormant ack is refreshed by new schedule.
- Related source rows 2913, 2914, 2915: Acknowledgement removal proposals are withdrawn: dormant ack retained and refreshed with new schedule.

**Evidence:** anon-2.jsonl:2915 · comment 350896403 · PR 4822 · 2022-12-05

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/helpers/hk/HkComplianceValidatorImpl.scala`

**Evidence:** anon-2.jsonl:2915 · comment 350896403 · PR 4822 · 2022-12-05

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/helpers/hk/HkComplianceValidatorImpl.scala`

**Explicit source context (hunk):**

> Future.failed(BadRequest("Not implemented for Hk"))
>  
>    override def validateUpsertRecurringInvestmentRequest(customerId: UUID, request: UpdateRecurringInvestmentScheduleRequestV2, plan: Plan): Future[Done] = {
> -    logger.error("Not hooked with compliance service recurring investment request")
> -    Future.successful(Done)
> +    for {
> +      _ <- Future.unit
> +      complianceAcks = convertToTradingAcknowledgements(request.customerAcknowledgements)
> +      complianceResponse <- complianceService
> +        .checkCustomerTradingRestriction(customerId)
> +        .invoke(
> +          PlanRecurringInvestmentUpsertRestrictionRequest(
> +            goalId = request.goalId,
> +            planId = requ

## A3-1109 — PlanAcknowledgementManagerEvents.scala: Cmd I guess we can merge them all in single `RemoveAcknowledgementsCmd`, but let’s not merge them in events

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/acknowledgements/ces/PlanAcknowledgementManagerEvents.scala; PR: [INV-675] Added modify acks with testcase

**Source-preserving request, proposal, or question:**

> Cmd I guess we can merge them all in single `RemoveAcknowledgementsCmd`, but let’s not merge them in events

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2976 · comment 343433664 · PR 4605 · 2022-11-07

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/acknowledgements/ces/PlanAcknowledgementManagerEvents.scala`

**Evidence:** anon-2.jsonl:2976 · comment 343433664 · PR 4605 · 2022-11-07

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/acknowledgements/ces/PlanAcknowledgementManagerEvents.scala`

**Explicit source context (hunk):**

> implicit val format: Format[AcknowledgedRecurringInvestmentEvt] = Json.format
>    }
>  
> +  case object CraCat2AcknowledgementRemovedEvt extends PlanAcknowledgementManagerEvent {
> +    implicit val format: Format[CraCat2AcknowledgementRemovedEvt.type] = Json.format
> +  }
> +

## A3-1112 — ModifyPlanAcknowledgementsLogic.scala: Hmm now that I see this, I want to break the request \+ cmd out too… if customer sends request to delete recurring investment schedule, we will automa

**Source stance:** open-question

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/ModifyPlanAcknowledgementsLogic.scala; PR: [INV-675] Added modify acks with testcase

**Source-preserving request, proposal, or question:**

> Hmm now that I see this, I want to break the request \+ cmd out too… if customer sends request to delete recurring investment schedule, we will automatically remove their ack in recurring transfer schedules?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2979 · comment 343541624 · PR 4605 · 2022-11-07

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/ModifyPlanAcknowledgementsLogic.scala`

**Evidence:** anon-2.jsonl:2979 · comment 343541624 · PR 4605 · 2022-11-07

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/ModifyPlanAcknowledgementsLogic.scala`

**Explicit source context (hunk):**

> +      List(maybeRemoveCraCat2AckCmd, maybeRemoveRecurringInvestmentAcksCmd).flatten
> +    )(cmd => refProvider.getPlanAcknowledgementManagerEntity(planId).ask(cmd))
> +      .map(_ => Done)
> +  }
> +}

## A3-1120 — Ack compensation/recon alternative tolerates eventual correction unlike CR earmark

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala; PR: Feat/INV-558 CR audit

**Concern stated in the source:** But then, we still need to carefully check before applying because of concurrent requests.

And it’s ok because this only affects recurring flow, unlike earmark which will affect CR calculation.

**Source-preserving request, proposal, or question:**

> So for acks, it’s somewhat tricky to correctly reverse it unless we inspect the old events. We might potentially return the old state as part of command, so one can use it as \(manual\) compensating saga. But then, we still need to carefully check before applying because of concurrent requests.
> 
> OTOH, most of the time it’s harmless to leave the ack there. We can build recon logic for ack too, e.g. CAT1 goals with persisted CAT2 ack, goals with recurring investment with persisted recurring ack. This way, we can eventually fix the acks without building complicated workflow logic. And it’s ok because this only affects recurring flow, unlike earmark which will affect CR calculation.
> 
> I can update the logging message here a bit to indicate that we will have recon for it, instead of just purely “can ignore”.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Ack rollback needs prior events/state and concurrent-request checks; proposed reconciliation accepted as eventual alternative because recurring ack less critical than CR earmark. Preserve examples and uncertainty.

**Evidence:** anon-2.jsonl:2991 · comment 344062610 · PR 4628 · 2022-11-09

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala`

**Evidence:** anon-2.jsonl:2991 · comment 344062610 · PR 4628 · 2022-11-09

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala`

**Explicit source context (hunk):**

> } yield response
>    }
>  
>    private def doCraChecks(
>      request: TradingRestrictionRequest,
>      customerId: UUID,
> +    referenceId: UUID,

## A3-1133 — QueryTradingRestrictionLogic.scala: Hmm, not every plan would have persisted acks?

**Source stance:** open-question

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/QueryTradingRestrictionLogic.scala; PR: [INV-669] State change impacted plans

**Source-preserving request, proposal, or question:**

> Hmm, not every plan would have persisted acks?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:3004 · comment 342007862 · PR 4577 · 2022-11-01

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/QueryTradingRestrictionLogic.scala`

## A3-1134 — QueryTradingRestrictionLogic.scala: Right ok, so we lookup for all plans, and the entity has initial empty state if no acks. Should be able to lazy this, and only lookup acks if plan has

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/QueryTradingRestrictionLogic.scala; PR: [INV-669] State change impacted plans

**Source-preserving request, proposal, or question:**

> Right ok, so we lookup for all plans, and the entity has initial empty state if no acks.
> 
> Should be able to lazy this, and only lookup acks if plan has recurring schedule?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:3005 · comment 342007987 · PR 4577 · 2022-11-01

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/QueryTradingRestrictionLogic.scala`

## A3-1183 — TransactionService.scala: customerId is there for old endpoint because the entity is at customer level

**Source stance:** explanation

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/TransactionService.scala; PR: feat/INV-442 Transaction V2 Impl

**Concern stated in the source:** Yeah customerId is there for old endpoint because the entity is at customer level

**Source-preserving request, proposal, or question:**

> Yeah customerId is there for old endpoint because the entity is at customer level

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3056 · comment 337480800 · PR 4436 · 2022-10-13

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/TransactionService.scala`

**Evidence:** anon-2.jsonl:3056 · comment 337480800 · PR 4436 · 2022-10-13

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/TransactionService.scala`

**Explicit source context (hunk):**

> "/api/v1/transaction/query-transactions?customerId&accountType&goalId&planId&transactionTypes&readFromDb&ccy",
>            queryTransactions _
>          ),
> +        //TODO: Do we need to implement V2 of this API for new transaction model? There's only 1 difference in this API and the above API. Check method `correctInfoDateInOldDividends`
>          restCall(
>            Method.GET,
>            "/api/v1/transaction/query-transactions-for-activities?customerId&accountType&goalId&planId&transactionTypes&readFromDb&ccy",

## A3-1187 — TransactionService.scala: We still need ability to override txn if needed in HK though

**Source stance:** requested-change

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/TransactionService.scala; PR: feat/INV-442 Transaction V2 Impl

**Source-preserving request, proposal, or question:**

> We still need ability to override txn if needed in HK though

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3060 · comment 339574431 · PR 4436 · 2022-10-21

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/TransactionService.scala`

**Evidence:** anon-2.jsonl:3060 · comment 339574431 · PR 4436 · 2022-10-21

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/TransactionService.scala`

**Explicit source context (hunk):**

> pathCall("/internal/transaction/page", internalPaginateCustomerTransactions _),
> -        restCall(Method.POST, "/internal/transaction/override", internalForceOverrideTransaction _)
> +        pathCall("/internal/v2/transaction/page", internalPaginateTransactions _),
> +        //TODO: Make breaking change to this API to start supporting new Transaction model after migrations is done in SG?
> +        restCall(Method.POST, "/internal/transaction/override", internalForceOverrideTransaction _),
>        )
>        .withAutoAcl(true)

## A3-1189 — package.scala: Should be ok to drop this I think. Once order moves to confirmed state, we should no longer need to use data from assumed state.

**Source stance:** suggestion

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/package.scala; PR: INV-555 feat: Investment Transaction and Orders modelling

**Source-preserving request, proposal, or question:**

> Should be ok to drop this I think. Once order moves to confirmed state, we should no longer need to use data from assumed state.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:3062 · comment 339254065 · PR 4490 · 2022-10-20

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/package.scala`

## A3-1190 — TransactionTypes.scala: I’m not sure how we are planning to use this DTO… accepting a transactionStatus in constructor and enforce it to be exactly one value always… this loo

**Source stance:** open-question

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala; PR: INV-555 feat: Investment Transaction and Orders modelling

**Source-preserving request, proposal, or question:**

> I’m not sure how we are planning to use this DTO… accepting a transactionStatus in constructor and enforce it to be exactly one value always… this looks weird..
> 
> Should we just override `def transactionStatus: TransactionStatus` and return that exact status instead?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3063 · comment 339255454 · PR 4490 · 2022-10-20

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Evidence:** anon-2.jsonl:3063 · comment 339255454 · PR 4490 · 2022-10-20

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Explicit source context (hunk):**

> +    transactionStatus: TransactionStatus,
> +    cancellingAt: ZonedDateTime
> +  ) extends InvestmentStatusDetailsDto {
> +    require(TransactionStatus.CANCELLING == transactionStatus)
> +  }
> +
> +  object CancellingStatusDetailsDto {

## A3-1191 — TransactionTypes.scala: Right, pending might have different statuses

**Source stance:** explanation

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala; PR: INV-555 feat: Investment Transaction and Orders modelling

**Source-preserving request, proposal, or question:**

> Right, pending might have different statuses

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3064 · comment 339255619 · PR 4490 · 2022-10-20

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Evidence:** anon-2.jsonl:3064 · comment 339255619 · PR 4490 · 2022-10-20

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Explicit source context (hunk):**

> +    transactionStatus: TransactionStatus,
> +    cancellingAt: ZonedDateTime
> +  ) extends InvestmentStatusDetailsDto {
> +    require(TransactionStatus.CANCELLING == transactionStatus)
> +  }
> +
> +  object CancellingStatusDetailsDto {

## A3-1193 — Pending order has amount or units; settlement both; mixed lists and latest-state model

**Source stance:** suggestion

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala; PR: INV-555 feat: Investment Transaction and Orders modelling

**Source-preserving request, proposal, or question:**

> Do we have need to tell our consumer if order is unit or amount based? I think if that question ever comes up, it should be checked at source, rather than transaction.
> 
> So how about:
> 
> * pending order have amount and unit both optional, and a require clause to check at least one is populated
> * assumed and confirmed order have amount and unit both required
> 
> 
> 
> A transaction can have mix of all of these in its order list. Then we don’t need to split too much:
> 
> * requested state
> * pending state
> * settlement state: either assumed or confirmed, once confirmed we don’t care about assumed data

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Pending amount/units at least one, settlement both required, mixed-order transaction, confirmed no longer needs assumed data; source proposal, not proof of accepted schema.

**Evidence:** anon-2.jsonl:3066 · comment 339260432 · PR 4490 · 2022-10-20

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

> Do we have need to tell our consumer if order is unit or amount based? I think if that question ever comes up, it should be checked at source, rather than transaction.
> 
> So how about:
> 
> * pending order have amount and unit both optional, and a require clause to check at least one is populated
> * assumed and confirmed order have amount and unit both required
> 
> ‌
> 
> A transaction can have mix of all of these in its order list. Then we don’t need to split too much:
> 
> * requested state
> * pending state
> * settlement state: either assumed or confirmed, once confirmed we don’t care about assumed data
> 
> ‌

**Evidence:** anon-2.jsonl:3066 · comment 339260432 · PR 4490 · 2022-10-20

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Explicit source context (hunk):**

> +    )
> +  }
> +
>    case class RejectedAmountStatusDetailsDto(
>      transactionStatus: TransactionStatus,
>      rejectedAmount: BigDecimal,
>      rejectedAt: ZonedDateTime

## A3-1197 — PlanAcknowledgementManagerEvents.scala: Generally, we want to capture events as facts that happened, so this should be `CraCat2AckedEvt`

**Source stance:** requested-change

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/acknowledgements/ces/PlanAcknowledgementManagerEvents.scala; PR: Feat/INV-560 recurring and ack persistence

**Source-preserving request, proposal, or question:**

> Generally, we want to capture events as facts that happened, so this should be `CraCat2AckedEvt`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3070 · comment 337483304 · PR 4477 · 2022-10-13

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/acknowledgements/ces/PlanAcknowledgementManagerEvents.scala`

**Evidence:** anon-2.jsonl:3070 · comment 337483304 · PR 4477 · 2022-10-13

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/acknowledgements/ces/PlanAcknowledgementManagerEvents.scala`

**Explicit source context (hunk):**

> +      AggregateEventTag.sharded[PlanAcknowledgementManagerEvent](NumShards)
> +  }
> +
> +  case class AcknowledgedCraCat2Evt(
> +     ackTime: Instant
> +  ) extends PlanAcknowledgementManagerEvent
> +

## A3-1203 — PlanAcknowledgementManagerEntity.scala: I’m thinking this should be set in Cmd instead…

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/acknowledgements/PlanAcknowledgementManagerEntity.scala; PR: Feat/INV-560 recurring and ack persistence

**Source-preserving request, proposal, or question:**

> I’m thinking this should be set in Cmd instead…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3076 · comment 337484235 · PR 4477 · 2022-10-13

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/acknowledgements/PlanAcknowledgementManagerEntity.scala`

**Evidence:** anon-2.jsonl:3076 · comment 337484235 · PR 4477 · 2022-10-13

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/acknowledgements/PlanAcknowledgementManagerEntity.scala`

**Explicit source context (hunk):**

> +      .onCommand[AcknowledgeCraCat2Cmd, Done] {
> +        case (cmd: AcknowledgeCraCat2Cmd, ctx, state) =>
> +          ctx.thenPersist(
> +            AcknowledgedCraCat2Evt(cmd.ackTime)
> +          )(_ => ctx.reply(Done))
> +      }
> +      .onCommand[AcknowledgeRecurringTransfer, Done] {

## A3-1213 — TradingRestrictionLogic.scala: If request is an instance of `RecurringInvestmentRestrictionRequest`, we would load the ack from persisted state, and then refresh the timestamp in th

**Source stance:** observed-defect

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala; PR: Feat/INV-560 recurring and ack persistence

**Concern stated in the source:** If request is an instance of `RecurringInvestmentRestrictionRequest`, we would load the ack from persisted state, and then refresh the timestamp in this else block… not good idea I think..

**Source-preserving request, proposal, or question:**

> If request is an instance of `RecurringInvestmentRestrictionRequest`, we would load the ack from persisted state, and then refresh the timestamp in this else block… not good idea I think..

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3088 · comment 338188031 · PR 4477 · 2022-10-17

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala`

**Evidence:** anon-2.jsonl:3088 · comment 338188031 · PR 4477 · 2022-10-17

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala`

**Explicit source context (hunk):**

> +          case CraCat2Ack => AcknowledgeCraCat2Cmd(Instant.now())
> +          case RecurringTransactionAck => if (request.isInstanceOf[PlanRecurringTransferUpsertRestrictionRequest]) {
> +            AcknowledgeRecurringTransfer(Instant.now())
> +          } else {
> +            AcknowledgeRecurringInvestment(Instant.now())
> +          }
> +        })(

## A3-1214 — CustomerAdvisoryProfileEntity.scala: purely just in case. Because I can’t apply the event on this state anyway

**Source stance:** explanation

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileEntity.scala; PR: [INV-656] feat(advisory): Internal endpoint to force override CRA expiry date

**Concern stated in the source:** Because I can’t apply the event on this state anyway

**Source-preserving request, proposal, or question:**

> Yeah purely just in case. Because I can’t apply the event on this state anyway

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3089 · comment 340343292 · PR 4526 · 2022-10-25

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileEntity.scala`

**Evidence:** anon-2.jsonl:3089 · comment 340343292 · PR 4526 · 2022-10-25

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileEntity.scala`

**Explicit source context (hunk):**

> +      .onEvent {
> +        case (evt: ExpiryDateOverriddenEvt, state: Initialized) =>
> +          state.advisoryProfile match {
> +            case _: VulnerableCustomerProfile =>
> +              logger.error("Unexpected {} for VC customer. Skip applying event on state", evt)
> +              state
> +

## A3-1233 — TradingRestrictionLogic.scala: Should we move this “get acks” as a method on the request itself? This looks messy

**Source stance:** open-question

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala; PR: Feat/INV-560 cra2 complex ack

**Source-preserving request, proposal, or question:**

> Should we move this “get acks” as a method on the request itself? This looks messy

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:3109 · comment 336582418 · PR 4449 · 2022-10-10

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala`

## A3-1237 — TradingRestrictionRequest.scala: Can we remove the default impl and explicitly return empty set in the Recurring request instance? I think it’s better that way, since if we add new re

**Source stance:** requested-change

**Context:**

> compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/tradingRestriction/TradingRestrictionRequest.scala; PR: Feat/INV-560 cra2 complex ack

**Source-preserving request, proposal, or question:**

> Can we remove the default impl and explicitly return empty set in the Recurring request instance? I think it’s better that way, since if we add new request type, we immediately have to think about ack requirements.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3115 · comment 336783659 · PR 4449 · 2022-10-11

Source path: `compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/tradingRestriction/TradingRestrictionRequest.scala`

**Evidence:** anon-2.jsonl:3115 · comment 336783659 · PR 4449 · 2022-10-11

Source path: `compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/tradingRestriction/TradingRestrictionRequest.scala`

**Explicit source context (hunk):**

> -sealed trait TradingRestrictionRequest extends TradingIntention
> +sealed trait TradingRestrictionRequest extends TradingIntention {
> +  def acknowledgements: Set[TradingAcknowledgementDto]
> +}
> +
>  case class GoalCreationRestrictionRequest(
>    goalId: UUID,

## A3-1246 — TradingRestrictionLogic.scala: But then again, when customer goes thru the invest-once flow in UI, they will see the current TAA in PlanDto…. the TaaModificationEarmark should reall

**Source stance:** open-question

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala; PR: Feat/INV-560 cra2 complex ack

**Concern stated in the source:** the TaaModificationEarmark should really be short-lived… I get the concern, but let’s see if we can handle these cases differently… otherwise logic gonna explode

**Source-preserving request, proposal, or question:**

> But then again, when customer goes thru the invest-once flow in UI, they will see the current TAA in PlanDto…. the TaaModificationEarmark should really be short-lived… I get the concern, but let’s see if we can handle these cases differently… otherwise logic gonna explode

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source rows 3124, 3126, 3127: Earmark-aware lookup proposal is revised: request-supplied TAA+ack here; customer-levelCR honors earmark.

**Evidence:** anon-2.jsonl:3126 · comment 336816754 · PR 4449 · 2022-10-11

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala`

**Evidence:** anon-2.jsonl:3126 · comment 336816754 · PR 4449 · 2022-10-11

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala`

**Explicit source context (hunk):**

> +  private def doCraCat2Checks(
> +    request: TradingRestrictionRequest,
> +    targetAllocation: Map[InstrumentProfile, BigDecimal],
> +    acks: Set[TradingAcknowledgementDto]
> +  ) (
> +    customerId: UUID,

## A3-1247 — Supplied TAA+ack sufficient for request; customer CR must honor TaaModificationEarmark

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala; PR: Feat/INV-560 cra2 complex ack

**Concern stated in the source:** We don’t need to look up again, even in rare race condition in which exists a TaaModificationEarmark for same plan.

This is because it can happen to another completely different plan, as CR breach is validation at customer level.

Conclusion, we don’t need to change anything here, except for maybe find a way to structure/comment code so that this logic is clear for reader.

**Source-preserving request, proposal, or question:**

> FYI…
> 
> I and  chatted offline on this topic:
> 
> * The request provides the TAA together with corresponding acks for that specific TAA. We don’t need to look up again, even in rare race condition in which exists a TaaModificationEarmark for same plan. If such case happens:
> 
>     * goal modification request itself should already ack for its corresponding new TAA. So either one of the goal modification or investment request will have correct ack
>     * investment orders will anyhow be generated much later by trading service - potentially using a different TAA at that time. As long as we guarantee all trading impact activities go thru latest ack check, it’s sufficient
>     
> * OTOH, CR calculation should lookup TAA honouring TaaModificationEarmark. This is because it can happen to another completely different plan, as CR breach is validation at customer level.
> 
> 
> 
> Conclusion, we don’t need to change anything here, except for maybe find a way to structure/comment code so that this logic is clear for reader. But we can revisit refactoring after we capture the essential logic \+ extensive test cases.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Final source decision distinguishes request-supplied TAA+corresponding ack for goal/investment from customer-levelCR requiring TaaModificationEarmark lookup; no change here beyond comments/refactor after tests.
- Related source rows 3124, 3126, 3127: Earmark-aware lookup proposal is revised: request-supplied TAA+ack here; customer-levelCR honors earmark.

**Evidence:** anon-2.jsonl:3127 · comment 336827575 · PR 4449 · 2022-10-11

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala`

> FYI…
> 
> I and

**Evidence:** anon-2.jsonl:3127 · comment 336827575 · PR 4449 · 2022-10-11

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala`

> chatted offline on this topic:
> 
> * The request provides the TAA together with corresponding acks for that specific TAA. We don’t need to look up again, even in rare race condition in which exists a TaaModificationEarmark for same plan. If such case happens:
> 
>     * goal modification request itself should already ack for its corresponding new TAA. So either one of the goal modification or investment request will have correct ack
>     * investment orders will anyhow be generated much later by trading service - potentially using a different TAA at that time. As long as we guarantee all trading impact activities go thru latest ack check, it’s sufficient
>     
> * OTOH, CR calculation should lookup TAA honouring TaaModificationEarmark. This is because it can happen to another completely different plan, as CR breach is validation at customer level.
> 
> ‌
> 
> Conclusion, we don’t need to change anything here, except for maybe find a way to structure/comment code so that this logic is clear for reader. But we can revisit refactoring after we capture the essential logic \+ extensive test cases.
> 
> ‌

**Evidence:** anon-2.jsonl:3127 · comment 336827575 · PR 4449 · 2022-10-11

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala`

**Explicit source context (hunk):**

> +  private def doCraCat2Checks(
> +    request: TradingRestrictionRequest,
> +    targetAllocation: Map[InstrumentProfile, BigDecimal],
> +    acks: Set[TradingAcknowledgementDto]
> +  ) (
> +    customerId: UUID,

## A3-1251 — CustomerTradingEarmarkManagerCommands.scala: release earmark command should just require BuyEarkmarkId - and we drop exactly that earmark, without checking amount

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/ces/CustomerTradingEarmarkManagerCommands.scala; PR: Feat/INV-551 release earmark

**Source-preserving request, proposal, or question:**

> I think release earmark command should just require BuyEarkmarkId - and we drop exactly that earmark, without checking amount

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3132 · comment 334802657 · PR 4377 · 2022-10-03

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/ces/CustomerTradingEarmarkManagerCommands.scala`

**Evidence:** anon-2.jsonl:3132 · comment 334802657 · PR 4377 · 2022-10-03

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/ces/CustomerTradingEarmarkManagerCommands.scala`

**Explicit source context (hunk):**

> }
>  
> +  case class ReleaseBuyEarmarkCmd(
> +    buyEarmarkId: BuyEarmarkId,
> +    reason: String,
> +    requestedBy: String
> +  ) extends CustomerTradingEarmarkManagerCmd with ReplyType[Done]

## A3-1252 — CustomerTradingEarmarkManagerCommands.scala: add `requestedBy` too. This is useful for manual flow. In normal subscriber flow, maybe we can set requestedBy = the subscriber class itself

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/ces/CustomerTradingEarmarkManagerCommands.scala; PR: Feat/INV-551 release earmark

**Source-preserving request, proposal, or question:**

> Maybe add `requestedBy` too. This is useful for manual flow. In normal subscriber flow, maybe we can set requestedBy = the subscriber class itself

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3133 · comment 334802878 · PR 4377 · 2022-10-03

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/ces/CustomerTradingEarmarkManagerCommands.scala`

**Evidence:** anon-2.jsonl:3133 · comment 334802878 · PR 4377 · 2022-10-03

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/ces/CustomerTradingEarmarkManagerCommands.scala`

**Explicit source context (hunk):**

> +  case class ReleaseBuyEarmarkCmd(
> +    buyEarmarkId: BuyEarmarkId,
> +    reason: String,
> +    requestedBy: String
> +  ) extends CustomerTradingEarmarkManagerCmd with ReplyType[Done]
> +

## A3-1253 — TradingEarmarkModificationRequest.scala: I’m thinking if we should just add DTO corresponding to BuyEarmarkId, and then have single request payload for the release request which contains buyE

**Source stance:** suggestion

**Context:**

> compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/earmarkUpdate/TradingEarmarkModificationRequest.scala; PR: Feat/INV-551 release earmark

**Source-preserving request, proposal, or question:**

> I’m thinking if we should just add DTO corresponding to BuyEarmarkId, and then have single request payload for the release request which contains buyEarmarkId \+ requestedBy \+ reason

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:3134 · comment 334803292 · PR 4377 · 2022-10-03

Source path: `compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/earmarkUpdate/TradingEarmarkModificationRequest.scala`

## A3-1254 — TradingEarmarkModificationRequest.scala: Also, are you adding the REST endpoint for this too? If so, let’s mark it as internal

**Source stance:** open-question

**Context:**

> compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/earmarkUpdate/TradingEarmarkModificationRequest.scala; PR: Feat/INV-551 release earmark

**Source-preserving request, proposal, or question:**

> Also, are you adding the REST endpoint for this too? If so, let’s mark it as internal

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:3135 · comment 334803542 · PR 4377 · 2022-10-03

Source path: `compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/earmarkUpdate/TradingEarmarkModificationRequest.scala`

## A3-1256 — CustomerTradingEarmarkManagerCommands.scala: I was thinking we should distinguish between releasing an earmark due to full utilisation \(when the investment is submitted externally for settlement

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/ces/CustomerTradingEarmarkManagerCommands.scala; PR: Feat/INV-551 release earmark

**Source-preserving request, proposal, or question:**

> I was thinking we should distinguish between releasing an earmark due to full utilisation \(when the investment is submitted externally for settlement\) VS due to drop \(when the investment is rejected or cancelled\).
> 
> But I guess that info is captured by the requestedBy / reason, and the end effect is same, the earmark is removed. So this should be good too.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3137 · comment 335025608 · PR 4377 · 2022-10-04

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/ces/CustomerTradingEarmarkManagerCommands.scala`

**Evidence:** anon-2.jsonl:3137 · comment 335025608 · PR 4377 · 2022-10-04

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/ces/CustomerTradingEarmarkManagerCommands.scala`

**Explicit source context (hunk):**

> implicit val format: Format[CreateBuyEarmarkCmd] = Json.format
>    }
>  
> +  case class ReleaseBuyEarmarkCmd(
> +    buyEarmarkId: BuyEarmarkId,
> +    reason: String,
> +    requestedBy: String

## A3-1257 — ReleaseEarmarkSpec.scala: Should we add another assertion checking the earmark state? Otherwise, we would always get a Done as result - whether the earmark is found or not

**Source stance:** open-question

**Context:**

> compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/releaseEarmark/ReleaseEarmarkSpec.scala; PR: Feat/INV-551 release earmark

**Concern stated in the source:** Otherwise, we would always get a Done as result - whether the earmark is found or not

**Source-preserving request, proposal, or question:**

> Should we add another assertion checking the earmark state? Otherwise, we would always get a Done as result - whether the earmark is found or not

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3138 · comment 335026059 · PR 4377 · 2022-10-04

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/releaseEarmark/ReleaseEarmarkSpec.scala`

**Evidence:** anon-2.jsonl:3138 · comment 335026059 · PR 4377 · 2022-10-04

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/releaseEarmark/ReleaseEarmarkSpec.scala`

**Explicit source context (hunk):**

> +
> +          Then("Process is successful")
> +          responseFut.map { response =>
> +            response shouldBe Done
> +          }
> +        }
> +

## A3-1258 — Earmark-release e2e: simulate failure, release, simulate success

**Source stance:** suggestion

**Context:**

> compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/releaseEarmark/ReleaseEarmarkSpec.scala; PR: Feat/INV-551 release earmark

**Concern stated in the source:** * setup state so that CR would fail
* call simulate and assert rejection
* call release earmark and assert success
* call simulate again and assert success

Otherwise I feel this test a bit useless by itself…

**Source-preserving request, proposal, or question:**

> Right ok, then maybe a better e2e is to do:
> 
> * setup state so that CR would fail
> * call simulate and assert rejection
> * call release earmark and assert success
> * call simulate again and assert success
> 
> 
> 
> Otherwise I feel this test a bit useless by itself…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3139 · comment 335026962 · PR 4377 · 2022-10-04

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/releaseEarmark/ReleaseEarmarkSpec.scala`

> Right ok, then maybe a better e2e is to do:
> 
> * setup state so that CR would fail
> * call simulate and assert rejection
> * call release earmark and assert success
> * call simulate again and assert success
> 
> ‌
> 
> Otherwise I feel this test a bit useless by itself…
> 
> ‌

**Evidence:** anon-2.jsonl:3139 · comment 335026962 · PR 4377 · 2022-10-04

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/service/releaseEarmark/ReleaseEarmarkSpec.scala`

**Explicit source context (hunk):**

> +
> +          Then("Process is successful")
> +          responseFut.map { response =>
> +            response shouldBe Done
> +          }
> +        }
> +

## A3-1279 — Recurring-instance acks belong to compliance persistence, not investment/trading request

**Source stance:** requested-change

**Context:**

> compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/tradingRestriction/TradingRestrictionRequest.scala; PR: Feat/INV-560 acknowledegement API Contract

**Source-preserving request, proposal, or question:**

> Whatever ack required during instance of recurring schedule should be stored by compliance, and looked up by compliance. The request initiated by investment/trading service should not need to carry the acks

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:3160 · comment 335701639 · PR 4423 · 2022-10-06

Source path: `compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/tradingRestriction/TradingRestrictionRequest.scala`

## A3-1280 — TradingRestrictionRequest.scala: So when customer create goal with recurring investment, that ack needs to be sent. Compliance would check and persist that ack. When time comes for `R

**Source stance:** explanation

**Context:**

> compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/tradingRestriction/TradingRestrictionRequest.scala; PR: Feat/INV-560 acknowledegement API Contract

**Source-preserving request, proposal, or question:**

> So when customer create goal with recurring investment, that ack needs to be sent. Compliance would check and persist that ack.
> 
> When time comes for `RecurringInvestmentIntention`, compliance should match against the persisted ack

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:3161 · comment 335702430 · PR 4423 · 2022-10-06

Source path: `compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/tradingRestriction/TradingRestrictionRequest.scala`

## A3-1292 — BuyEarmark sameID/amount idempotency validated in command, event appends only

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala; PR: Feat/INV-486 add goal earmark

**Concern stated in the source:** So that in event handler, we would simply add the earmark to the list

**Source-preserving request, proposal, or question:**

> So WDYT about this? IMO, we should:
> 
> * if brand new earmark, add it
> * if match existing id:
> 
>     * if amount is fine, do nothing
>     * if amount is different, it feels like we should reject the command here, since for same ID, we should not change at all
>     
> 
> This logic should ideally sit in the command handler, i.e. `handleCreateBuyEarmark`
> 
> So that in event handler, we would simply add the earmark to the list
> 
> 
> 
> In case of some error that requires changing amount of an existing earmark, let’s add separate command for it?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- New earmark emits; sameID+sameamount no-op; sameID+differentamount reject, separate correction command. Validate in command handler so event handler only appends.
- Related source rows 3174, 3178, 3180, 3185, 3200, 3201: Keep currentVersion check, no-op duplicateID+amount, reject changed amount, new event only for new earmark;3200 question does not override3201 matrix.

**Evidence:** anon-2.jsonl:3174 · comment 333428532 · PR 4344 · 2022-09-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

> So WDYT about this? IMO, we should:
> 
> * if brand new earmark, add it
> * if match existing id:
> 
>     * if amount is fine, do nothing
>     * if amount is different, it feels like we should reject the command here, since for same ID, we should not change at all
>     
> 
> This logic should ideally sit in the command handler, i.e. `handleCreateBuyEarmark`
> 
> So that in event handler, we would simply add the earmark to the list
> 
> ‌
> 
> In case of some error that requires changing amount of an existing earmark, let’s add separate command for it?

**Evidence:** anon-2.jsonl:3174 · comment 333428532 · PR 4344 · 2022-09-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

**Explicit source context (hunk):**

> +    case (evt: BuyEarmarkCreatedEvt, state) => state.copy(evt.buyEarmark +: state.buyEarmarks)
> +  }
> +
> +  private def handleCreateBuyEarmark(
> +                                      cmd: CreateBuyEarmarkCmd,
> +                                      ctx: CommandContext[Done],
> +                                      state: CustomerTradingEarmarkManagerState): Persist = {

## A3-1293 — ConcentrationRiskValidator.scala: This duplicate pattern matching on request type seems to suggest we should break down by type earlier. Example for the simulation flow: ```scala def v

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cr/ConcentrationRiskValidator.scala; PR: Feat/INV-486 add goal earmark

**Concern stated in the source:** This duplicate pattern matching on request type seems to suggest we should break down by type earlier.

**Source-preserving request, proposal, or question:**

> This duplicate pattern matching on request type seems to suggest we should break down by type earlier.
> 
> Example for the simulation flow:
> 
> ```scala
>   def validateSimulation(customerId: UUID, advisoryRiskProfile: RiskProfile, liquidNetWorth: BigDecimal)(
>     request: TradingSimulationRestrictionRequest,
>     requiresCat2Validation: Boolean
>   ): Future[Boolean] = {
>     val investmentValueCalculatorFn: CustomerTradingEarmarkManagerState => Future[Map[RiskLevel, BigDecimal]] = existingEarmarkState =>
>       request match {
>         ...
>       }
> 
>     validationSimulation(customerId, advisoryRiskProfile, liquidNetWorth)(investmentValueCalculatorFn, requiresCat2Validation)
>   }
> 
>   private def validationSimulation(customerId: UUID, advisoryRiskProfile: RiskProfile, liquidNetWorth: BigDecimal)(
>     investmentValueCalculatorFn: CustomerTradingEarmarkManagerState => Future[Map[RiskLevel, BigDecimal]],
>     requiresCat2Validation: Boolean
>   ): Future[Boolean] = {
>     for {
>       existingEarmarkState <- refProvider.getCustomerTradingEarmarkManagerEntity(customerId).ask(GetCustomerTradingEarmarksCmd)
>       investmentValuesByRiskLevel <- investmentValueCalculatorFn(existingEarmarkState)
>     } yield {
>       validateCat1CrLimit(liquidNetWorth, investmentValuesByRiskLevel) &&
>       (!requiresCat2Validation || validateCat2CrLimit(advisoryRiskProfile)(liquidNetWorth, investmentValuesByRiskLevel))
>     }
>   }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Preserve function-injected simulation skeleton and exact CAT1&&(!requiresCAT2||CAT2) condition; pattern-match request once outside.

**Evidence:** anon-2.jsonl:3175 · comment 333432324 · PR 4344 · 2022-09-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cr/ConcentrationRiskValidator.scala`

> This duplicate pattern matching on request type seems to suggest we should break down by type earlier.
> 
> Example for the simulation flow:
> 
> ```scala
>   def validateSimulation(customerId: UUID, advisoryRiskProfile: RiskProfile, liquidNetWorth: BigDecimal)(
>     request: TradingSimulationRestrictionRequest,
>     requiresCat2Validation: Boolean
>   ): Future[Boolean] = {
>     val investmentValueCalculatorFn: CustomerTradingEarmarkManagerState => Future[Map[RiskLevel, BigDecimal]] = existingEarmarkState =>
>       request match {
>         ...
>       }
> 
>     validationSimulation(customerId, advisoryRiskProfile, liquidNetWorth)(investmentValueCalculatorFn, requiresCat2Validation)
>   }
> 
>   private def validationSimulation(customerId: UUID, advisoryRiskProfile: RiskProfile, liquidNetWorth: BigDecimal)(
>     investmentValueCalculatorFn: CustomerTradingEarmarkManagerState => Future[Map[RiskLevel, BigDecimal]],
>     requiresCat2Validation: Boolean
>   ): Future[Boolean] = {
>     for {
>       existingEarmarkState <- refProvider.getCustomerTradingEarmarkManagerEntity(customerId).ask(GetCustomerTradingEarmarksCmd)
>       investmentValuesByRiskLevel <- investmentValueCalculatorFn(existingEarmarkState)
>     } yield {
>       validateCat1CrLimit(liquidNetWorth, investmentValuesByRiskLevel) &&
>       (!requiresCat2Validation || validateCat2CrLimit(advisoryRiskProfile)(liquidNetWorth, investmentValuesByRiskLevel))
>     }
>   }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:3175 · comment 333432324 · PR 4344 · 2022-09-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cr/ConcentrationRiskValidator.scala`

**Explicit source context (hunk):**

> +    instrumentWeights: InstrumentWeights,
> +    customerId: UUID,
> +    advisoryRiskProfile: RiskProfile,
> +    liquidNetWorth: BigDecimal
> +  )(
> +    request: TradingRestrictionRequest,
> +    requiresCat2Validation: Boolean

## A3-1294 — ConcentrationRiskValidator.scala: This way, for confirmation flow, the skeleton private method would accept 2 functions returning Future: * one for the investment values * another for 

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cr/ConcentrationRiskValidator.scala; PR: Feat/INV-486 add goal earmark

**Source-preserving request, proposal, or question:**

> This way, for confirmation flow, the skeleton private method would accept 2 functions returning Future:
> 
> * one for the investment values
> * another for the register earmarks if success
> 
> 
> 
> Then we pattern match by request type outside, once, and return tuple of the functions
> 
> ```scala
>     val blah: (CustomerTradingEarmarkManagerState => Future[Map[RiskLevel, BigDecimal]], () => Future[Done]) = request match {
>       case GoalCreateSimulationRestrictionRequest(targetInstrumentWeights, initialInvestmentAmount, _) =>
>         initialInvestmentAmount.filter(_ > 0) match {
>           case Some(amount) =>
>             (
>               existingEarmarkState => Future.successfule(Map()),
>               () => Future.successful(Done)
>             )
>           case None =>
>             throw ComplianceServiceException(
>               ComplianceServiceErrorType.InternalError,
>               s"Invalid state. Request [$request] not applicable for ConcentrationRisk validation"
>             )
>         }
> 
>       case _ =>
>         throw ComplianceServiceException(
>           ComplianceServiceErrorType.NotImplementedError,
>           s"Unsupported TradingRestrictionRequest of type ${request.getClass.getSimpleName}"
>         )
>     }
> ```
> 
> 
> 
> Need to name / extract this properly of course :grimacing:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Confirmation skeleton takes investment-values function and success-only earmark-registration function; code is illustrative proposal including placeholders.

**Evidence:** anon-2.jsonl:3176 · comment 333435934 · PR 4344 · 2022-09-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cr/ConcentrationRiskValidator.scala`

> This way, for confirmation flow, the skeleton private method would accept 2 functions returning Future:
> 
> * one for the investment values
> * another for the register earmarks if success
> 
> ‌
> 
> Then we pattern match by request type outside, once, and return tuple of the functions
> 
> ```scala
>     val blah: (CustomerTradingEarmarkManagerState => Future[Map[RiskLevel, BigDecimal]], () => Future[Done]) = request match {
>       case GoalCreateSimulationRestrictionRequest(targetInstrumentWeights, initialInvestmentAmount, _) =>
>         initialInvestmentAmount.filter(_ > 0) match {
>           case Some(amount) =>
>             (
>               existingEarmarkState => Future.successfule(Map()),
>               () => Future.successful(Done)
>             )
>           case None =>
>             throw ComplianceServiceException(
>               ComplianceServiceErrorType.InternalError,
>               s"Invalid state. Request [$request] not applicable for ConcentrationRisk validation"
>             )
>         }
> 
>       case _ =>
>         throw ComplianceServiceException(
>           ComplianceServiceErrorType.NotImplementedError,
>           s"Unsupported TradingRestrictionRequest of type ${request.getClass.getSimpleName}"
>         )
>     }
> ```
> 
> ‌
> 
> Need to name / extract this properly of course :grimacing:

**Evidence:** anon-2.jsonl:3176 · comment 333435934 · PR 4344 · 2022-09-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cr/ConcentrationRiskValidator.scala`

**Explicit source context (hunk):**

> +    instrumentWeights: InstrumentWeights,
> +    customerId: UUID,
> +    advisoryRiskProfile: RiskProfile,
> +    liquidNetWorth: BigDecimal
> +  )(
> +    request: TradingRestrictionRequest,
> +    requiresCat2Validation: Boolean

## A3-1296 — CustomerTradingEarmarkManagerEntity.scala: the idea is we validate and reject in command handler, so that event handler can be dumb and just append

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala; PR: Feat/INV-486 add goal earmark

**Concern stated in the source:** Yeah the idea is we validate and reject in command handler, so that event handler can be dumb and just append

**Source-preserving request, proposal, or question:**

> Yeah the idea is we validate and reject in command handler, so that event handler can be dumb and just append

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source rows 3174, 3178, 3180, 3185, 3200, 3201: Keep currentVersion check, no-op duplicateID+amount, reject changed amount, new event only for new earmark;3200 question does not override3201 matrix.

**Evidence:** anon-2.jsonl:3178 · comment 333436666 · PR 4344 · 2022-09-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

**Evidence:** anon-2.jsonl:3178 · comment 333436666 · PR 4344 · 2022-09-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

**Explicit source context (hunk):**

> +    case (evt: BuyEarmarkCreatedEvt, state) => state.copy(evt.buyEarmark +: state.buyEarmarks)
> +  }
> +
> +  private def handleCreateBuyEarmark(
> +                                      cmd: CreateBuyEarmarkCmd,
> +                                      ctx: CommandContext[Done],
> +                                      state: CustomerTradingEarmarkManagerState): Persist = {

## A3-1298 — Same earmarkID+amount returns Done without event

**Source stance:** requested-change

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala; PR: Feat/INV-486 add goal earmark

**Source-preserving request, proposal, or question:**

> If exists earmark with same ID and same amount, we don’t want to create another earmark - we want to reply done without any event, maybe can add some logs for troubleshooting purpose

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source rows 3174, 3178, 3180, 3185, 3200, 3201: Keep currentVersion check, no-op duplicateID+amount, reject changed amount, new event only for new earmark;3200 question does not override3201 matrix.

**Evidence:** anon-2.jsonl:3180 · comment 333680877 · PR 4344 · 2022-09-28

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

**Evidence:** anon-2.jsonl:3180 · comment 333680877 · PR 4344 · 2022-09-28

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

**Explicit source context (hunk):**

> +          if (existingEarmark.amount != cmd.buyEarmark.amount) {
> +            ctx.commandFailed(
> +              ComplianceServiceException(ComplianceServiceErrorType.ConcurrentModification,
> +                s"Earmark exists with same id ${cmd.buyEarmark.id} but with different amount, illegal operation!"
> +              )
> +            )
> +            ctx.done

## A3-1301 — CustomerTradingEarmarkManagerCommands.scala: Can we drop “Customer” here? We have “Customer” in entity name to suggest the aggregate is at customer level, but I think we don’t need it anymore in 

**Source stance:** open-question

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/ces/CustomerTradingEarmarkManagerCommands.scala; PR: Feat/INV-486 add goal earmark

**Source-preserving request, proposal, or question:**

> Can we drop “Customer” here? We have “Customer” in entity name to suggest the aggregate is at customer level, but I think we don’t need it anymore in Cmd, since it would be per individual earmark

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3183 · comment 333974737 · PR 4344 · 2022-09-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/ces/CustomerTradingEarmarkManagerCommands.scala`

**Evidence:** anon-2.jsonl:3183 · comment 333974737 · PR 4344 · 2022-09-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/ces/CustomerTradingEarmarkManagerCommands.scala`

**Explicit source context (hunk):**

> implicit val format: Format[GetCustomerTradingEarmarksCmd.type] = singletonFormat(GetCustomerTradingEarmarksCmd)
>    }
>  
> +  case class CreateBuyEarmarkCmd(
> +    buyEarmark: BuyEarmark,
> +    currentVersion: Long
> +  ) extends CustomerTradingEarmarkManagerCmd with ReplyType[Done]

## A3-1302 — CustomerTradingEarmarkManagerEvents.scala: Can we also drop “Trading” here? “TradingEarmark” was intended to be general name for all the earmark types.

**Source stance:** open-question

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/ces/CustomerTradingEarmarkManagerEvents.scala; PR: Feat/INV-486 add goal earmark

**Source-preserving request, proposal, or question:**

> Can we also drop “Trading” here? “TradingEarmark” was intended to be general name for all the earmark types.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3184 · comment 333988745 · PR 4344 · 2022-09-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/ces/CustomerTradingEarmarkManagerEvents.scala`

**Evidence:** anon-2.jsonl:3184 · comment 333988745 · PR 4344 · 2022-09-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/ces/CustomerTradingEarmarkManagerEvents.scala`

**Explicit source context (hunk):**

> AggregateEventTag.sharded[CustomerTradingEarmarkManagerEvent](NumShards)
>    }
>  
> +  case class BuyEarmarkCreatedEvt(
> +    buyEarmark: BuyEarmark
> +  ) extends CustomerTradingEarmarkManagerEvent
> +

## A3-1303 — CustomerTradingEarmarkManagerEntity.scala: How about we refactor this a bit? Using pattern match on the find? ```scala state.buyEarmarks.find(_.id == cmd.buyEarmark.id) match { case Some(existi

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala; PR: Feat/INV-486 add goal earmark

**Source-preserving request, proposal, or question:**

> How about we refactor this a bit? Using pattern match on the find?
> 
> ```scala
> state.buyEarmarks.find(_.id == cmd.buyEarmark.id) match {
>   case Some(existingEarmark) =>
>     if (existingEarmark.amount != cmd.buyEarmark.amount) {
>       // throw
>     } else {
>       // warn and reply done
>     }
>   case None =>
>     // emit event
> }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source rows 3174, 3178, 3180, 3185, 3200, 3201: Keep currentVersion check, no-op duplicateID+amount, reject changed amount, new event only for new earmark;3200 question does not override3201 matrix.

**Evidence:** anon-2.jsonl:3185 · comment 334015485 · PR 4344 · 2022-09-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

> How about we refactor this a bit? Using pattern match on the find?
> 
> ```scala
> state.buyEarmarks.find(_.id == cmd.buyEarmark.id) match {
>   case Some(existingEarmark) =>
>     if (existingEarmark.amount != cmd.buyEarmark.amount) {
>       // throw
>     } else {
>       // warn and reply done
>     }
>   case None =>
>     // emit event
> }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:3185 · comment 334015485 · PR 4344 · 2022-09-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

**Explicit source context (hunk):**

> +        )
> +      )
> +      ctx.done
> +    } else {
> +      state.buyEarmarks.find(_.id == cmd.buyEarmark.id) match {
> +        case Some(existingEarmark) =>
> +          if (existingEarmark.amount != cmd.buyEarmark.amount) {

## A3-1308 — CustomerTradingEarmarkEntityTest.scala: I think test is a bit clearer if we do this step 1 as state setup instead. Can use `withCustomizedEntitySetup`

**Source stance:** suggestion

**Context:**

> compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/cr/CustomerTradingEarmarkEntityTest.scala; PR: Feat/INV-486 add goal earmark

**Source-preserving request, proposal, or question:**

> Nit: I think test is a bit clearer if we do this step 1 as state setup instead. Can use `withCustomizedEntitySetup`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3190 · comment 334017714 · PR 4344 · 2022-09-29

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/cr/CustomerTradingEarmarkEntityTest.scala`

**Evidence:** anon-2.jsonl:3190 · comment 334017714 · PR 4344 · 2022-09-29

Source path: `compliance-impl/src/test/scala/com/endowus/silver/compliance/impl/logic/hk/cr/CustomerTradingEarmarkEntityTest.scala`

**Explicit source context (hunk):**

> +      driver.initialize(snapshotState = Some(
> +        initialState.copy(buyEarmarks = initialState.buyEarmarks :+ BuyEarmark(
> +          id = InitialInvestmentEarmarkId(
> +            goalId = goalId1,
> +            planId = planId1
> +          ),
> +          amount = 1000

## A3-1318 — CustomerTradingEarmarkManagerEntity.scala: I still want it to reject… what if caller will actually process that same command twice :grimacing: ?

**Source stance:** open-question

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala; PR: Feat/INV-486 add goal earmark

**Source-preserving request, proposal, or question:**

> I still want it to reject… what if caller will actually process that same command twice :grimacing: ?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source rows 3174, 3178, 3180, 3185, 3200, 3201: Keep currentVersion check, no-op duplicateID+amount, reject changed amount, new event only for new earmark;3200 question does not override3201 matrix.

**Evidence:** anon-2.jsonl:3200 · comment 334066329 · PR 4344 · 2022-09-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

**Evidence:** anon-2.jsonl:3200 · comment 334066329 · PR 4344 · 2022-09-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

**Explicit source context (hunk):**

> +                                      cmd: CreateBuyEarmarkCmd,
> +                                      ctx: CommandContext[Done],
> +                                      state: CustomerTradingEarmarkManagerState): Persist = {
> +    if (cmd.currentVersion != state.version) {
> +      ctx.commandFailed(
> +        ComplianceServiceException(ComplianceServiceErrorType.ConcurrentModification,
> +          s"Earmark have been modified, this request is stale! Request version ${cmd.currentVersion}, current version ${state.version}!"

## A3-1319 — BuyEarmark currentVersion then ID+amount branch matrix

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala; PR: Feat/INV-486 add goal earmark

**Source-preserving request, proposal, or question:**

> Hmm current logic is:
> 
> 1. if different version => you validate on stale data, reject due to concurrent request
> 2. if same version:
> 
>     1. if brand new id => event
>     2. same id exists:
>     
>         1. different amount => something is wrong, error \(if want to amend, then we need different command\)
>         2. same amount => it’s no-op, just reply Done
>         
>     
> 
> 
> 
> Which part are you suggesting to change? 2.b.ii?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Keep concurrency-version branch before ID+amount branch; same-version+newID emits, differentamount errors, sameamount no-op; question about which branch to alter remains open.
- Related source rows 3174, 3178, 3180, 3185, 3200, 3201: Keep currentVersion check, no-op duplicateID+amount, reject changed amount, new event only for new earmark;3200 question does not override3201 matrix.

**Evidence:** anon-2.jsonl:3201 · comment 334076151 · PR 4344 · 2022-09-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

> Hmm current logic is:
> 
> 1. if different version => you validate on stale data, reject due to concurrent request
> 2. if same version:
> 
>     1. if brand new id => event
>     2. same id exists:
>     
>         1. different amount => something is wrong, error \(if want to amend, then we need different command\)
>         2. same amount => it’s no-op, just reply Done
>         
>     
> 
> ‌
> 
> Which part are you suggesting to change? 2.b.ii?
> 
> ‌

**Evidence:** anon-2.jsonl:3201 · comment 334076151 · PR 4344 · 2022-09-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

**Explicit source context (hunk):**

> +                                      cmd: CreateBuyEarmarkCmd,
> +                                      ctx: CommandContext[Done],
> +                                      state: CustomerTradingEarmarkManagerState): Persist = {
> +    if (cmd.currentVersion != state.version) {
> +      ctx.commandFailed(
> +        ComplianceServiceException(ComplianceServiceErrorType.ConcurrentModification,
> +          s"Earmark have been modified, this request is stale! Request version ${cmd.currentVersion}, current version ${state.version}!"

## A3-1323 — TradingRestrictionResponse.scala: not leak this version I think…

**Source stance:** suggestion

**Context:**

> compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/tradingRestriction/TradingRestrictionResponse.scala; PR: Feat/INV-486 add goal earmark

**Source-preserving request, proposal, or question:**

> Let’s not leak this version I think…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:3205 · comment 333139599 · PR 4330 · 2022-09-26

Source path: `compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/tradingRestriction/TradingRestrictionResponse.scala`

## A3-1325 — CustomerTradingEarmarkManagerEvents.scala: Hmmm one action should only create one BuyEarmark I think. Only action that would trigger multiple earmark is modification of a multiple-plan goal. Bu

**Source stance:** open-question

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/ces/CustomerTradingEarmarkManagerEvents.scala; PR: Feat/INV-486 add goal earmark

**Source-preserving request, proposal, or question:**

> Hmmm one action should only create one BuyEarmark I think. Only action that would trigger multiple earmark is modification of a multiple-plan goal. But even then, we might want to emit multiple event instead. Let’s think a bit more on this.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3207 · comment 333140108 · PR 4330 · 2022-09-26

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/ces/CustomerTradingEarmarkManagerEvents.scala`

**Evidence:** anon-2.jsonl:3207 · comment 333140108 · PR 4330 · 2022-09-26

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/ces/CustomerTradingEarmarkManagerEvents.scala`

**Explicit source context (hunk):**

> }
>  
> +  case class BuyTradingEarmarkCreatedEvt(
> +    buyEarmark: BuyEarmark
> +  ) extends CustomerTradingEarmarkManagerEvent
> +
> +  object BuyTradingEarmarkCreatedEvt {

## A3-1326 — CustomerTradingEarmarkManagerEntity.scala: Ah I think the event should contain only the new earmark, and we append inside `handleEvents` instead of here

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala; PR: Feat/INV-486 add goal earmark

**Source-preserving request, proposal, or question:**

> Ah I think the event should contain only the new earmark, and we append inside `handleEvents` instead of here

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3208 · comment 333140369 · PR 4330 · 2022-09-26

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

**Evidence:** anon-2.jsonl:3208 · comment 333140369 · PR 4330 · 2022-09-26

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

**Explicit source context (hunk):**

> +    }else if (state.buyEarmarks.exists(e => e.id.equals(cmd.buyEarmark.id) && e.amount != cmd.buyEarmark.amount)) {
> +      ctx.commandFailed(
> +        ComplianceServiceException(ComplianceServiceErrorType.ConcurrentModification,
> +          s"Earmark exists with same id ${cmd.buyEarmark.id} but with different amount, illegal operation!"
> +        )
> +      )
> +      ctx.done

## A3-1329 — package.scala: Why do we need to return wrapped TransactionData?

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/ces/commands/package.scala; PR: INV-450 feat: Transaction Persistent Entity

**Source-preserving request, proposal, or question:**

> Why do we need to return wrapped TransactionData?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3212 · comment 333333496 · PR 4299 · 2022-09-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/ces/commands/package.scala`

**Evidence:** anon-2.jsonl:3212 · comment 333333496 · PR 4299 · 2022-09-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/ces/commands/package.scala`

**Explicit source context (hunk):**

> +    implicit val format: Format[InspectTransactionCmd.type] = singletonFormat(InspectTransactionCmd)
> +  }
> +
> +  case class GetTransactionCmd(transactionId: UUID) extends TransactionCmd with ReplyType[TransactionData]
> +
> +  object GetTransactionCmd {
> +    implicit val format: Format[GetTransactionCmd] = Json.format

## A3-1330 — TransactionState NotInitialized/Initialized alternative to Option

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/ces/state/package.scala; PR: INV-450 feat: Transaction Persistent Entity

**Source-preserving request, proposal, or question:**

> I normally do this… once again to avoid dealing with Option… make it a bit more explicit
> 
> ```
> sealed trait TransactionState
> case object NotInitialized extends TransactionState
> case class Initialized(transaction: Transaction) extends TransactionState
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3213 · comment 333333802 · PR 4299 · 2022-09-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/ces/state/package.scala`

> I normally do this… once again to avoid dealing with Option… make it a bit more explicit
> 
> ```
> sealed trait TransactionState
> case object NotInitialized extends TransactionState
> case class Initialized(transaction: Transaction) extends TransactionState
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:3213 · comment 333333802 · PR 4299 · 2022-09-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/ces/state/package.scala`

**Explicit source context (hunk):**

> +
> +package object state {
> +
> +  sealed trait TransactionState
> +
> +  object TransactionState {
> +    implicit val format: Format[TransactionState] = Json.format

## A3-1331 — package.scala: true. But using simple Option means State might go from Some to None, whereas using named state would make people think twice before trying to change 

**Source stance:** explanation

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/ces/state/package.scala; PR: INV-450 feat: Transaction Persistent Entity

**Source-preserving request, proposal, or question:**

> Yeah true. But using simple Option means State might go from Some to None, whereas using named state would make people think twice before trying to change from Initialized back to NotInitialized.
> 
> Anyway it’s just semantics thing :thumbsup:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Initialized/NotInitialized preference is explicitly semantic rather than a proven correctness requirement.

**Evidence:** anon-2.jsonl:3214 · comment 333345338 · PR 4299 · 2022-09-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/ces/state/package.scala`

**Evidence:** anon-2.jsonl:3214 · comment 333345338 · PR 4299 · 2022-09-27

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/ces/state/package.scala`

**Explicit source context (hunk):**

> +
> +package object state {
> +
> +  sealed trait TransactionState
> +
> +  object TransactionState {
> +    implicit val format: Format[TransactionState] = Json.format

## A3-1333 — HkServiceLogicImpl.scala: Ah this one is internal error with “invalid state” reason is because I expect VC / Expired status to be caught outside already. So this case should ne

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/impl/HkServiceLogicImpl.scala; PR: [INV-485] feat(compliance): Initial CR validation logic

**Concern stated in the source:** Ah this one is internal error with “invalid state” reason is because I expect VC / Expired status to be caught outside already.

**Source-preserving request, proposal, or question:**

> Ah this one is internal error with “invalid state” reason is because I expect VC / Expired status to be caught outside already. So this case should never happen

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3218 · comment 333057959 · PR 4189 · 2022-09-26

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/impl/HkServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:3218 · comment 333057959 · PR 4189 · 2022-09-26

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/impl/HkServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +            case _ =>
> +              Future.failed(
> +                ComplianceServiceException(
> +                  ComplianceServiceErrorType.InternalError,
> +                  s"Invalid state. AdvisoryProfile [${craDetailsResponse.advisoryProfile}] not applicable for ConcentrationRisk validation"
> +                )
> +              )

## A3-1337 — TransactionTypes.scala: This means `DepositBasedStatusDetailsDto` etc. must always be empty trait, and we simply use it to define the available statuses of a transaction type

**Source stance:** open-question

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala; PR: INV-235 feat: Transaction types modelling

**Source-preserving request, proposal, or question:**

> This means `DepositBasedStatusDetailsDto` etc. must always be empty trait, and we simply use it to define the available statuses of a transaction type?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3222 · comment 330807952 · PR 4256 · 2022-09-15

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

> This means `DepositBasedStatusDetailsDto` etc. must always be empty trait, and we simply use it to define the available statuses of a transaction type?
> 
> ‌

**Evidence:** anon-2.jsonl:3222 · comment 330807952 · PR 4256 · 2022-09-15

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Explicit source context (hunk):**

> +    transactionStatus: TransactionStatus,
> +    requestedAmount: BigDecimal,
> +    requestedAt: ZonedDateTime
> +  ) extends DepositBasedStatusDetailsDto
> +      with InvestmentBasedStatusDetailsDto {
> +    require(
> +      ApplicableTransactionStatuses.contains(transactionStatus)

## A3-1338 — TransactionTypes.scala: Any example of existing transaction types that doesn’t support a particular status?

**Source stance:** open-question

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala; PR: INV-235 feat: Transaction types modelling

**Source-preserving request, proposal, or question:**

> Any example of existing transaction types that doesn’t support a particular status?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3223 · comment 330809420 · PR 4256 · 2022-09-15

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Evidence:** anon-2.jsonl:3223 · comment 330809420 · PR 4256 · 2022-09-15

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Explicit source context (hunk):**

> +    transactionStatus: TransactionStatus,
> +    requestedAmount: BigDecimal,
> +    requestedAt: ZonedDateTime
> +  ) extends DepositBasedStatusDetailsDto
> +      with InvestmentBasedStatusDetailsDto {
> +    require(
> +      ApplicableTransactionStatuses.contains(transactionStatus)

## A3-1343 — TransactionTypes.scala: Just a thought. I may create a `RequestedAmountStatusDetailsDto` with `transactionStatus = SETTLEMENT_CONFIRMED` with this modelling? Mapping each tra

**Source stance:** open-question

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala; PR: INV-235 feat: Transaction types modelling

**Source-preserving request, proposal, or question:**

> Just a thought. I may create a `RequestedAmountStatusDetailsDto` with `transactionStatus = SETTLEMENT_CONFIRMED` with this modelling?
> 
> Mapping each transaction status to a case class is kinda messy too. But we should have some protection here at least I think

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3228 · comment 331136323 · PR 4256 · 2022-09-16

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Evidence:** anon-2.jsonl:3228 · comment 331136323 · PR 4256 · 2022-09-16

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Explicit source context (hunk):**

> +  //TODO: Add more traits for other transaction types when being defined
> +
> +  case class RequestedAmountStatusDetailsDto(
> +    transactionStatus: TransactionStatus,
> +    requestedAmount: BigDecimal,
> +    requestedAt: ZonedDateTime
> +  ) extends DepositBasedStatusDetailsDto

## A3-1353 — transactionTypes.scala: Just a thought, do we want to add a case class representing the status which contains amount \+ updatedAt field? Then we can get rid of these optional

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/transactionTypes.scala; PR: [WIP] INV-235 Transaction Service v2 models

**Source-preserving request, proposal, or question:**

> Just a thought, do we want to add a case class representing the status which contains amount \+ updatedAt field? Then we can get rid of these optional? And we would also get rid of the object level fields?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3239 · comment 329430532 · PR 4217 · 2022-09-09

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/transactionTypes.scala`

**Evidence:** anon-2.jsonl:3239 · comment 329430532 · PR 4217 · 2022-09-09

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/transactionTypes.scala`

**Explicit source context (hunk):**

> +    goalId: UUID,
> +    planId: UUID,
> +    requestedAmount: BigDecimal,
> +    assumedAmount: Option[BigDecimal] = None,
> +    settledAmount: Option[BigDecimal] = None,
> +    recurringTransactionId: Option[String] = None,
> +    assumedAt: Option[ZonedDateTime] = None,

## A3-1355 — transactionTypes.scala: on point \(3\), it’s not about losing data. Old data is still there in events, we just want latest snapshot in State \(ideally\). From readside point 

**Source stance:** explanation

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/transactionTypes.scala; PR: [WIP] INV-235 Transaction Service v2 models

**Source-preserving request, proposal, or question:**

> Yeah on point \(3\), it’s not about losing data. Old data is still there in events, we just want latest snapshot in State \(ideally\). From readside point of view, we can always have a read model providing snapshot, and potentially another read model providing all data, if needed. But as you pointed out, we don’t need this old data today. In fact, we store all fields, and then have to introduce object level fields like amount and statusUpdatedAt to merge the them again.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3241 · comment 329769641 · PR 4217 · 2022-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/transactionTypes.scala`

**Evidence:** anon-2.jsonl:3241 · comment 329769641 · PR 4217 · 2022-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/transactionTypes.scala`

**Explicit source context (hunk):**

> +    goalId: UUID,
> +    planId: UUID,
> +    requestedAmount: BigDecimal,
> +    assumedAmount: Option[BigDecimal] = None,
> +    settledAmount: Option[BigDecimal] = None,
> +    recurringTransactionId: Option[String] = None,
> +    assumedAt: Option[ZonedDateTime] = None,

## A3-1372 — ServiceLogicImpl.scala: Ah yes.. `withResult`… blind me

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/service/impl/ServiceLogicImpl.scala; PR: Feat/CE-488 compliance refactor service impl redo

**Source-preserving request, proposal, or question:**

> Ah yes.. `withResult`… blind me

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3261 · comment 322450184 · PR 4019 · 2022-08-10

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:3261 · comment 322450184 · PR 4019 · 2022-08-10

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +
> +  val IsComplianceCheckEnabledGlobally: Boolean = true
> +
> +  def `BadRequest`(message: String): ComplianceServiceException =
> +    ComplianceServiceException(ComplianceServiceErrorType.BadRequest, message)
> +
> +  def `NotFound`(message: String): ComplianceServiceException =

## R-3363 — We reuse this Cmd here which does not protect us from concurrent modification in entity logic. But should be ok for now, since we do not officially support

**Source stance:** explanation

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/GoalServiceImpl.scala; PR 3624: Fix/IA factors flagship remix

**Source-preserving request, proposal, or question:**

> We reuse this Cmd here which does not protect us from concurrent modification in entity logic. But should be ok for now, since we do not officially support changing productLine anywhere else

**Evidence:** anon-2.jsonl:3363 · comment 305858986 · PR 3624 · 2022-06-03

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/GoalServiceImpl.scala`

## R-3376 — At some point, I guess we should split PlanProfile out of Entity. Local cache built from Kafka should just be updated directly, no need to maintain event t

**Source stance:** suggestion

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/GoalTopicSubscriber.scala; PR 3524: adds product line and intent on charge and adds isAlternativeInvestment on fundsmart

**Source-preserving request, proposal, or question:**

> At some point, I guess we should split PlanProfile out of Entity. Local cache built from Kafka should just be updated directly, no need to maintain event traces I think

**Evidence:** anon-2.jsonl:3376 · comment 301716280 · PR 3524 · 2022-05-17

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/subscribers/GoalTopicSubscriber.scala`

## R-3378 — Oiii ctx.commandFailed

**Source stance:** observed-defect

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/FeeManagerEntity.scala; PR 3524: adds product line and intent on charge and adds isAlternativeInvestment on fundsmart

**Source-preserving request, proposal, or question:**

> Oiii ctx.commandFailed

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3378 · comment 301717079 · PR 3524 · 2022-05-17

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/FeeManagerEntity.scala`

## R-3390 — This is pure mapper method… it won’t know. I want this endpoint to force override as well, so it won’t know anything about the context of the overridden da

**Source stance:** explanation

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/package.scala; PR 3529: IAO-156: Add internal endpoint to allow override transaction data

**Source-preserving request, proposal, or question:**

> This is pure mapper method… it won’t know. I want this endpoint to force override as well, so it won’t know anything about the context of the overridden data

**Conditions and limits:**

- PR3529 sequence: simulation-only and real override evidence, identical/not-found errors, then a compare-and-set request/command check and the updated API/error response. Incidental UUIDs are omitted. Source rows: anon-2.jsonl:3387, anon-2.jsonl:3388, anon-2.jsonl:3389, anon-2.jsonl:3390, anon-2.jsonl:3391, anon-2.jsonl:3392.

**Evidence:** anon-2.jsonl:3390 · comment 301726088 · PR 3529 · 2022-05-17

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/package.scala`

## R-3391 — Override concurrency requires expected state and entity-side compare-and-set validation

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/TransactionServiceImpl.scala; PR 3529: IAO-156: Add internal endpoint to allow override transaction data

**Source-preserving request, proposal, or question:**

> That won’t “ensure no concurrent modification” right? If we want that, the request should take the expected existing state \+ \(the diff OR the new state\), the cmd handler check if state is same as provided existing state, otherwise reject.
> 
> I can do that too.

**Conditions and limits:**

- PR3529 sequence: simulation-only and real override evidence, identical/not-found errors, then a compare-and-set request/command check and the updated API/error response. Incidental UUIDs are omitted. Source rows: anon-2.jsonl:3387, anon-2.jsonl:3388, anon-2.jsonl:3389, anon-2.jsonl:3390, anon-2.jsonl:3391, anon-2.jsonl:3392.

**Evidence:** anon-2.jsonl:3391 · comment 301727064 · PR 3529 · 2022-05-17

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/TransactionServiceImpl.scala`

## R-3392 — Updated expectedExistingTransaction/targetTransaction request and stale-state BadRequest

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 3529: IAO-156: Add internal endpoint to allow override transaction data

**Source-preserving request, proposal, or question:**

> Updated the API to CAS style to protect the endpoint from concurrent modification
> 
> Request
> 
> ```json
> {
>     "expectedExistingTransaction": {
>         "transaction": {
>             "customerId": "[incidental identifier omitted]",
>             "tradingAccountType": "SINGAPORE_SRS_ACCOUNT",
>             "transactionId": "[incidental identifier omitted]",
>             "createdAt": "2022-04-28T00:17:23.022513+08:00[Asia/Singapore]",
>             "ccy": "SGD",
>             "transactionType": "INVESTMENT",
>             "status": "CREATED_AND_PENDING_INTERNAL_BROKER_SUBMISSION",
>             "goalId": "[incidental identifier omitted]",
>             "planId": "[incidental identifier omitted]",
>             "requestedAmount": 100,
>             "orders": [],
>             "convertedOrders": [],
>             "statusUpdatedDate": "2022-05-14T00:00:00Z"
>         }
>     },
>     "targetTransaction": {
>         "transaction": {
>             "customerId": "[incidental identifier omitted]",
>             "tradingAccountType": "SINGAPORE_SRS_ACCOUNT",
>             "transactionId": "[incidental identifier omitted]",
>             "createdAt": "2022-04-28T00:17:23.022513+08:00[Asia/Singapore]",
>             "ccy": "SGD",
>             "transactionType": "INVESTMENT",
>             "status": "SETTLEMENT_CONFIRMED",
>             "goalId": "[incidental identifier omitted]",
>             "planId": "[incidental identifier omitted]",
>             "requestedAmount": 100,
>             "settledAmount": 101.2,
>             "orders": [],
>             "convertedOrders": [],
>             "statusUpdatedDate": "2022-05-14T00:00:00Z"
>         },
>         "settledAt": "2022-05-14T22:10:00.000000+08:00[Asia/Singapore]"
>     },
>     "requestedBy": "<email>",
>     "reason": "Because I can",
>     "simulateOnly": true
> }
> ```
> 
> ‌
> 
> Response
> 
> ```json
> {
>     "simulateOnly": true,
>     "diff": [
>         {
>             "op": "add",
>             "path": "/settledAmount",
>             "value": 101.2
>         },
>         {
>             "op": "add",
>             "path": "/settledAt",
>             "value": "2022-05-14T22:10:00+08:00[Asia/Singapore]"
>         },
>         {
>             "op": "replace",
>             "path": "/status",
>             "value": "SETTLEMENT_CONFIRMED"
>         }
>     ]
> }
> ```
> 
> ‌
> 
> If existing state has changed, service will log the diff. Since it should be rare, log should be ok - not adding another field to complicate the exception
> 
> ```json
> {
>     "error_code": "",
>     "name": "BadRequest",
>     "detail": "Existing transaction does not match provided expected state. Check logs to find the unexpected diff."
> }
> ```
> 
> ‌

**Conditions and limits:**

- PR3529 sequence: simulation-only and real override evidence, identical/not-found errors, then a compare-and-set request/command check and the updated API/error response. Incidental UUIDs are omitted. Source rows: anon-2.jsonl:3387, anon-2.jsonl:3388, anon-2.jsonl:3389, anon-2.jsonl:3390, anon-2.jsonl:3391, anon-2.jsonl:3392.
- Only incidental reviewer mentions and customer/account UUID literals are omitted in the displayed source wording; symbols, predicates, dates, thresholds, and alternatives are retained.

**Evidence:** anon-2.jsonl:3392 · comment 301754890 · PR 3529 · 2022-05-17

> Updated the API to CAS style to protect the endpoint from concurrent modification
> 
> Request
> 
> ```json
> {
>     "expectedExistingTransaction": {
>         "transaction": {
>             "customerId": "

**Evidence:** anon-2.jsonl:3392 · comment 301754890 · PR 3529 · 2022-05-17

> ",
>             "tradingAccountType": "SINGAPORE_SRS_ACCOUNT",
>             "transactionId": "

**Evidence:** anon-2.jsonl:3392 · comment 301754890 · PR 3529 · 2022-05-17

> ",
>             "createdAt": "2022-04-28T00:17:23.022513+08:00[Asia/Singapore]",
>             "ccy": "SGD",
>             "transactionType": "INVESTMENT",
>             "status": "CREATED_AND_PENDING_INTERNAL_BROKER_SUBMISSION",
>             "goalId": "

**Evidence:** anon-2.jsonl:3392 · comment 301754890 · PR 3529 · 2022-05-17

> ",
>             "planId": "

**Evidence:** anon-2.jsonl:3392 · comment 301754890 · PR 3529 · 2022-05-17

> ",
>             "requestedAmount": 100,
>             "orders": [],
>             "convertedOrders": [],
>             "statusUpdatedDate": "2022-05-14T00:00:00Z"
>         }
>     },
>     "targetTransaction": {
>         "transaction": {
>             "customerId": "

**Evidence:** anon-2.jsonl:3392 · comment 301754890 · PR 3529 · 2022-05-17

> ",
>             "tradingAccountType": "SINGAPORE_SRS_ACCOUNT",
>             "transactionId": "

**Evidence:** anon-2.jsonl:3392 · comment 301754890 · PR 3529 · 2022-05-17

> ",
>             "createdAt": "2022-04-28T00:17:23.022513+08:00[Asia/Singapore]",
>             "ccy": "SGD",
>             "transactionType": "INVESTMENT",
>             "status": "SETTLEMENT_CONFIRMED",
>             "goalId": "

**Evidence:** anon-2.jsonl:3392 · comment 301754890 · PR 3529 · 2022-05-17

> ",
>             "planId": "

**Evidence:** anon-2.jsonl:3392 · comment 301754890 · PR 3529 · 2022-05-17

> ",
>             "requestedAmount": 100,
>             "settledAmount": 101.2,
>             "orders": [],
>             "convertedOrders": [],
>             "statusUpdatedDate": "2022-05-14T00:00:00Z"
>         },
>         "settledAt": "2022-05-14T22:10:00.000000+08:00[Asia/Singapore]"
>     },
>     "requestedBy": "<email>",
>     "reason": "Because I can",
>     "simulateOnly": true
> }
> ```
> 
> ‌
> 
> Response
> 
> ```json
> {
>     "simulateOnly": true,
>     "diff": [
>         {
>             "op": "add",
>             "path": "/settledAmount",
>             "value": 101.2
>         },
>         {
>             "op": "add",
>             "path": "/settledAt",
>             "value": "2022-05-14T22:10:00+08:00[Asia/Singapore]"
>         },
>         {
>             "op": "replace",
>             "path": "/status",
>             "value": "SETTLEMENT_CONFIRMED"
>         }
>     ]
> }
> ```
> 
> ‌
> 
> If existing state has changed, service will log the diff. Since it should be rare, log should be ok - not adding another field to complicate the exception
> 
> ```json
> {
>     "error_code": "",
>     "name": "BadRequest",
>     "detail": "Existing transaction does not match provided expected state. Check logs to find the unexpected diff."
> }
> ```
> 
> ‌

## R-3402 — PlanEventProcessor ServiceClient dependency moves wiring from Components to Application

**Source stance:** suggestion

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanEventProcessor.scala; PR 3398: Feat/IAO-93 block goal modification

**Source-preserving request, proposal, or question:**

> Yes this is fine. But you would have to move the wiring of this processor into \*Application, if it’s not already there.
> 
> By default, most of them will be wired in \*Components.
> 
> We need to move because it now depends on InstrumentService which is declared via `ServiceClient`. This is again available only in `LagomServiceClientComponents` which is extended by `LagomApplication`

**Evidence:** anon-2.jsonl:3402 · comment 295785007 · PR 3398 · 2022-04-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanEventProcessor.scala`

## R-3456 — Is it better to leave these kind of checks to the entity? I think I prefer input validation in cmd handler \+ state validation in entity

**Source stance:** open-question

**Context:**

> rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/RebateServiceImpl.scala; PR 3103: Fix Rebate service

**Source-preserving request, proposal, or question:**

> Is it better to leave these kind of checks to the entity? I think I prefer input validation in cmd handler \+ state validation in entity

**Evidence:** anon-2.jsonl:3456 · comment 282342199 · PR 3103 · 2022-02-24

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/RebateServiceImpl.scala`

## R-3457 — Want to include the result of `hasOnlyZeroRebateAmount` here? Or maybe split the if similar to how we check settledCcy?

**Source stance:** open-question

**Context:**

> rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/RebateDistributionEntity.scala; PR 3103: Fix Rebate service

**Source-preserving request, proposal, or question:**

> Want to include the result of `hasOnlyZeroRebateAmount` here? Or maybe split the if similar to how we check settledCcy?

**Evidence:** anon-2.jsonl:3457 · comment 282347084 · PR 3103 · 2022-02-24

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/RebateDistributionEntity.scala`

## R-3481 — I have one side question. This DB handler is not tied to any event processor, so we have to call `handler.createTables` here. If there is a readside event 

**Source stance:** open-question

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/ReportApplication.scala; PR 3038: SILVER-11957: Fix auto creation of report table

**Source-preserving request, proposal, or question:**

> I have one side question. This DB handler is not tied to any event processor, so we have to call `handler.createTables` here.
> 
> If there is a readside event processor, we could also call this as part of the global prepare.
> 
> Is there any preference / difference between them?

**Evidence:** anon-2.jsonl:3481 · comment 280642865 · PR 3038 · 2022-02-17

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/ReportApplication.scala`

## R-3506 — Take a step back, so if state has instrumentCcy, then we use it directly, and ignore the value from command. Otherwise we use from cmd This means we only r

**Source stance:** open-question

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/InstrumentMarketDataEntity.scala; PR 3010: Pass on Instrument Ccy while calling update-daily-price endpoint

**Source-preserving request, proposal, or question:**

> Take a step back, so if state has instrumentCcy, then we use it directly, and ignore the value from command. Otherwise we use from cmd
> 
> This means we only require instrumentCcy in Cmd if it is first time we manuallu upload it?
> 
> * should we make it optional in the request?
> * and validate after L192: if after resolved, and still blank then fail the command
> 
> ‌

**Evidence:** anon-2.jsonl:3506 · comment 278392627 · PR 3010 · 2022-02-09

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/InstrumentMarketDataEntity.scala`

## R-3517 — Added `Deleted` to the cases in `deleteRelatedTransaction` I see `DeleteCmd` is already handled correctly by the entity if in `Deleted` state

**Source stance:** reported-verification

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/common/DividendDeleter.scala; PR 2835: SILVER-11314: Fetch DividendState from entity before deleting to handle lag between DividendJdbcEventProcessor and DividendEventProcessor

**Source-preserving request, proposal, or question:**

> Added `Deleted` to the cases in `deleteRelatedTransaction`
> 
> I see `DeleteCmd` is already handled correctly by the entity if in `Deleted` state

**Evidence:** anon-2.jsonl:3517 · comment 272457921 · PR 2835 · 2022-01-13

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/common/DividendDeleter.scala`

## R-3527 — I mark this deprecated, and will remove after we verify everything is fixed in prod. For same reason, I will reuse existing `DividendReinvestedEvt` since t

**Source stance:** requested-change

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/DividendServiceImpl.scala; PR 2833: SILVER-11229: Fix settlement date for dividend reinvestment

**Source-preserving request, proposal, or question:**

> I mark this deprecated, and will remove after we verify everything is fixed in prod.
> 
> For same reason, I will reuse existing `DividendReinvestedEvt` since this is only temporary.
> 
> We can consider adding an OverrideDividendStateEvt in future, if the need to sync with Investment service comes back. But then, we should implement all cases properly, rather than just Reinvested state

**Conditions and limits:**

- PR2833 preserves separate historical migration, Confirmed-only sync, date/timestamp meanings, and optional-field alternatives. Naming evolves through priceDate to settlementDate. The final comment defers optional-forever versus mandatory-plus-migration to a later decision. Source rows: anon-2.jsonl:3522, anon-2.jsonl:3523, anon-2.jsonl:3524, anon-2.jsonl:3525, anon-2.jsonl:3526, anon-2.jsonl:3527, anon-2.jsonl:3528, anon-2.jsonl:3531, anon-2.jsonl:3533, anon-2.jsonl:3535, anon-2.jsonl:3536, anon-2.jsonl:3537, anon-2.jsonl:3538.

**Evidence:** anon-2.jsonl:3527 · comment 272781190 · PR 2833 · 2022-01-14

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/DividendServiceImpl.scala`

## R-3528 — No we sync only Confirmed ones. Assumed dividends \(if any\) would eventually be confirmed, and get processed by new logic

**Source stance:** requested-change

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/ces/DividendCommands.scala; PR 2833: SILVER-11229: Fix settlement date for dividend reinvestment

**Source-preserving request, proposal, or question:**

> No we sync only Confirmed ones. Assumed dividends \(if any\) would eventually be confirmed, and get processed by new logic

**Conditions and limits:**

- PR2833 preserves separate historical migration, Confirmed-only sync, date/timestamp meanings, and optional-field alternatives. Naming evolves through priceDate to settlementDate. The final comment defers optional-forever versus mandatory-plus-migration to a later decision. Source rows: anon-2.jsonl:3522, anon-2.jsonl:3523, anon-2.jsonl:3524, anon-2.jsonl:3525, anon-2.jsonl:3526, anon-2.jsonl:3527, anon-2.jsonl:3528, anon-2.jsonl:3531, anon-2.jsonl:3533, anon-2.jsonl:3535, anon-2.jsonl:3536, anon-2.jsonl:3537, anon-2.jsonl:3538.

**Evidence:** anon-2.jsonl:3528 · comment 272788902 · PR 2833 · 2022-01-14

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/ces/DividendCommands.scala`

## R-3594 — As chatted, I’ll check how we can write svcImplTest with real entity \(and hopefully without too much saga about mock entity > test driver > real entity :f

**Source stance:** requested-change

**Context:**

> advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/AdvisoryServiceImplTest.scala; PR 2643: SILVER-10408: Minor rename/refactor ProductLine implementation to better express the design pattern. Implement ExistingGoalDetail for Income

**Source-preserving request, proposal, or question:**

> As chatted,
> 
>   
> I’ll check how we can write svcImplTest with real entity \(and hopefully without too much saga about mock entity > test driver > real entity :fingers_crossed: \)  
>   
> For this API, everything happens in svc, and entity is only involved to return current state. Ok-ish to use mock.

**Conditions and limits:**

- These historical testing comments distinguish service orchestration mocks, entity-driver tests, and possible end-to-end tests; they do not state a universal no-mocks or embedded-database mandate. Source rows: anon-2.jsonl:3594, anon-2.jsonl:3597, anon-2.jsonl:3604, anon-2.jsonl:3605.

**Evidence:** anon-2.jsonl:3594 · comment 264683558 · PR 2643 · 2021-12-02

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/AdvisoryServiceImplTest.scala`

## R-3604 — ServiceImplTest mocks client boundaries; EntityTest checks command, state, events and response

**Source stance:** requested-change

**Context:**

> advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/AdvisoryServiceImplTest.scala; PR 2612: SILVER-10375: Support addAdvisoryTag for Income. Add /advisory/edge/income/portfolios

**Source-preserving request, proposal, or question:**

> [incidental identifier omitted] So we have 2 types of test:
> 
> * \*ServiceImplTest: use mock/stub for everything, and test the processing logic in \*ServiceImpl, e.g. request-to-command transformation, API composition
> * \*EntityTest: use persistence entity driver and test using command, verifying state \+ event\(s\) \+ response
> 
> ‌
> 
> I see ChargeServiceImplTest also follows this pattern.
> 
> The added AdvisoryServiceImplTest here also also follows that.
> 
> ‌
> 
> In scope of this PR, there is no change at entity level, hence no new tests added.

**Conditions and limits:**

- These historical testing comments distinguish service orchestration mocks, entity-driver tests, and possible end-to-end tests; they do not state a universal no-mocks or embedded-database mandate. Source rows: anon-2.jsonl:3594, anon-2.jsonl:3597, anon-2.jsonl:3604, anon-2.jsonl:3605.
- Only incidental reviewer mentions and customer/account UUID literals are omitted in the displayed source wording; symbols, predicates, dates, thresholds, and alternatives are retained.

**Evidence:** anon-2.jsonl:3604 · comment 264025007 · PR 2612 · 2021-11-30

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/AdvisoryServiceImplTest.scala`

>  So we have 2 types of test:
> 
> * \*ServiceImplTest: use mock/stub for everything, and test the processing logic in \*ServiceImpl, e.g. request-to-command transformation, API composition
> * \*EntityTest: use persistence entity driver and test using command, verifying state \+ event\(s\) \+ response
> 
> ‌
> 
> I see ChargeServiceImplTest also follows this pattern.
> 
> The added AdvisoryServiceImplTest here also also follows that.
> 
> ‌
> 
> In scope of this PR, there is no change at entity level, hence no new tests added.

## R-3605 — Historical e2e exploration from ServiceImpl avoids committing to flaky EmbeddedCassandra

**Source stance:** suggestion

**Context:**

> advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/AdvisoryServiceImplTest.scala; PR 2612: SILVER-10375: Support addAdvisoryTag for Income. Add /advisory/edge/income/portfolios

**Source-preserving request, proposal, or question:**

> e2e tests, if any, should have entry point starting from \*ServiceImpl, and somehow use actual entity. It seems Lagom recommends using EmbeddedCassandra to glue these, but from my experience, EmbeddedCassandra is a hot mess - flaky and slow.
> 
> I will think about this in the background.

**Conditions and limits:**

- These historical testing comments distinguish service orchestration mocks, entity-driver tests, and possible end-to-end tests; they do not state a universal no-mocks or embedded-database mandate. Source rows: anon-2.jsonl:3594, anon-2.jsonl:3597, anon-2.jsonl:3604, anon-2.jsonl:3605.

**Evidence:** anon-2.jsonl:3605 · comment 264025311 · PR 2612 · 2021-11-30

Source path: `advisory-impl/src/test/scala/com/endowus/silver/advisory/impl/AdvisoryServiceImplTest.scala`

